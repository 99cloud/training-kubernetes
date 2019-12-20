# AWS 环境部署高可用 Kubernetes 集群

两种方案 [https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/)：

+ 堆叠 etcd 拓扑，在 master 节点上托管 etcd 集群
    ![](https://d33wubrfki0l68.cloudfront.net/d1411cded83856552f37911eb4522d9887ca4e83/b94b2/images/kubeadm/kubeadm-ha-topology-stacked-etcd.svg)
+ 外置 etcd 集群，etcd 与 master 节点分离
    ![](https://d33wubrfki0l68.cloudfront.net/ad49fffce42d5a35ae0d0cc1186b97209d86b99c/5a6ae/images/kubeadm/kubeadm-ha-topology-external-etcd.svg)

**这里采用堆叠 etcd 拓扑也就是第一种。**

## 集群架构与设施（AWS）

![](https://docs.aws.amazon.com/zh_cn/vpc/latest/userguide/images/nat-gateway-diagram.png)

+ VPC 10.0.0.0/16
+ 子网

    | subnet | CIDR | 路由表 |
    | --- | --- | --- |
    | sub1 | 10.0.0.0/24 | custom |
    | sub2 | 10.0.1.0/24 | main |
+ 网关
    + Internet 网关
    + NAT 网关（选中 sub1 子网，需要分配弹性 IP）
+ 配置路由表
    + main

        | Destination | Target |
        | --- | --- |
        | 10.0.0.0/16 | local |
        | 0.0.0.0/0 | NAT 网关 |
    + custom

        | Destination | Target |
        | --- | --- |
        | 10.0.0.0/16 | local |
        | 0.0.0.0/0 | Internet 网关 |
+ 实例（推荐 3 master 节点 3+ worker 节点）

    | hostname | 私有 IP | 公有 IP | OS |
    | --- | --- | --- | --- |
    | bastion | 10.0.0.100 | 3.114.12.155 | CentOS |
    | kube-master-1 | 10.0.1.100 | | CentOS |
    | kube-master-2 | 10.0.1.101 | | CentOS |
    | kube-master-3 | 10.0.1.102 | | CentOS |
    | kube-worker-1 | 10.0.1.200 | | CentOS |
    | kube-worker-2 | 10.0.1.201 | | CentOS |
+ 负载均衡器（必须使用）
    + 内部使用
    + VPC 选中 sub2
    + 添加侦听器 TCP 6443 端口
    + 目标组选择 IP 10.0.1.100（master0）

**需要确保负载均衡器只路由到 master0 上的 6443 端口。这是因为 kubeadm 将使用负载均衡器 IP 执行健康检查。由于 master0 是第一个单独配置的，其他 master 不会运行 apiserver，这将导致 kubeadm 无限期地挂起。**

## 部署前准备（手动或者使用 Ansible 来完成）

### 1. Docker

1. 安装 Docker

        yum install -y yum-utils \
            device-mapper-persistent-data \
            lvm2
        yum-config-manager \
            --add-repo \
            https://download.docker.com/linux/centos/docker-ce.repository
        yum install -y docker-ce

2. 配置 Docker 使用 systemd 作为默认 Cgroup 驱动

        cat <<EOF > /etc/docker/daemon.json
        {
            "exec-opts": ["native.cgroupdriver=systemd"]
        }
        EOF

3. 启动 Docker

        systemctl start docker
        systemctl enable docker

### 2. Kubernetes

1. 安装 Kubernetes 相关应用程序

        cat <<EOF > /etc/yum.repos.d/kubernetes.repo
        [kubernetes]
        name=Kubernetes
        baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
        enabled=1
        gpgcheck=1
        repo_gpgcheck=1
        gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
        exclude=kube*
        EOF
        setenforce 0 # disable SELinux
        sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
        yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
        systemctl enable --now kubelet

2. 关闭系统交换区

        swapoff -a
        sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab

> 或者使用 [kubeadm-ansible](https://github.com/crazytaxii/kubeadm-ansible) 完成部署前准备（可选）

## 部署高可用集群

### 1. 初始化 master0 节点

**与单主节点集群部署不同，需要先编写 Kubeadm 的配置文件：**

    $ cat kubeadm-config.yaml
    apiVersion: kubeadm.k8s.io/v1beta2
    kind: ClusterConfiguration
    kubernetesVersion: stable
    controlPlaneEndpoint: "${LOAD_BALANCER_DNS}:6443"
    networking:
    podSubnet: ${CIDR}

+ `kubernetesVersion` 设置想要使用的 Kubernetes 版本，推荐使用 `stable`
+ `controlPlaneEndpoint` 设置负载均衡器的 DNS 域名或地址和端口

> 有些 CNI 网络插件比如 [Calico](https://github.com/projectcalico/calico) 需要另外设置一个 CIDR，[Weave](https://www.weave.works/) 这样的就不需要。

    sudo kubeadm init --config=kubeadm-config.yaml --upload-certs

+ `--upload-certs` 用来把控制节点所共享的证书上传到集群。

安装完成后 Kubeadm 的输出：

    Your Kubernetes control-plane has initialized successfully!

    To start using your cluster, you need to run the following as a regular user:

    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config

    You should now deploy a pod network to the cluster.
    Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
    https://kubernetes.io/docs/concepts/cluster-administration/addons/

    You can now join any number of the control-plane node running the following command on each as root:

    kubeadm join api-lb-574e65695cb56b54.elb.ap-northeast-1.amazonaws.com:6443 --token dum7wt.8wwa3mpfzmum1620 \
        --discovery-token-ca-cert-hash sha256:52a3719a16e2f6e2417afd0a8c8be709ec4f28442491be4c89835db47e49b2b3 \
        --control-plane --certificate-key 77d7258ce9581174082cabb9905e0e28adf3f0e8238edfa035545de8203b4b30

    Please note that the certificate-key gives access to cluster sensitive data, keep it secret!
    As a safeguard, uploaded-certs will be deleted in two hours; If necessary, you can use
    "kubeadm init phase upload-certs --upload-certs" to reload certs afterward.

    Then you can join any number of worker nodes by running the following on each as root:

    kubeadm join api-lb-574e65695cb56b54.elb.ap-northeast-1.amazonaws.com:6443 --token dum7wt.8wwa3mpfzmum1620 \
        --discovery-token-ca-cert-hash sha256:52a3719a16e2f6e2417afd0a8c8be709ec4f28442491be4c89835db47e49b2b3

+ 把两个 `join` 命令记下来，其他节点加入集群要用到
+ 当 `kubeadm init` 带上 `--upload-certs` 时，master0 节点的证书会被加密并保存在 `kubeadm-certs` Secret 中

> `kubeadm-certs` Secret 两小时后将失效

### 2. 部署 CNI 网络插件

+ Calico `kubectl apply -f https://docs.projectcalico.org/v3.8/manifests/calico.yaml`
+ Flannel `kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml`

测试 master0 节点是否正常：

    kubectl get nodes
    kubectl get pod -n kube-system -w

### 3. 将其它 master 节点加入集群

执行刚才保存下来的第一段 `kubeadm join` 命令：

    kubeadm join api-lb-574e65695cb56b54.elb.ap-northeast-1.amazonaws.com:6443 --token dum7wt.8wwa3mpfzmum1620 \
        --discovery-token-ca-cert-hash sha256:52a3719a16e2f6e2417afd0a8c8be709ec4f28442491be4c89835db47e49b2b3 \
        --control-plane --certificate-key 77d7258ce9581174082cabb9905e0e28adf3f0e8238edfa035545de8203b4b30

+ `--control-plane` 使 `kubeadm join` 创建一个新的控制节点
+ `--certificate-key ...` 将从集群中的 `kubeadm-certs` Secret 下载证书并解密

### 4. 将其他工作节点加入集群

执行刚才保存下来的第二段 `kubeadm join` 命令：

    kubeadm join api-lb-574e65695cb56b54.elb.ap-northeast-1.amazonaws.com:6443 --token dum7wt.8wwa3mpfzmum1620 \
        --discovery-token-ca-cert-hash sha256:52a3719a16e2f6e2417afd0a8c8be709ec4f28442491be4c89835db47e49b2b3

测试集群是否正常：

    $ kubectl get nodes
    NAME            STATUS   ROLES    AGE    VERSION
    kube-master-1   Ready    master   142m   v1.15.3
    kube-master-2   Ready    master   116m   v1.15.3
    kube-master-3   Ready    master   113m   v1.15.3
    kube-worker-1   Ready    <none>   31s    v1.15.3
    kube-worker-2   Ready    <none>   31s    v1.15.3
    $ kubectl get pods --all-namespaces
    kubectl get pod -n kube-system -w
    NAME                                    READY   STATUS    RESTARTS   AGE
    coredns-5c98db65d4-25k5n                1/1     Running   0          3h33m
    coredns-5c98db65d4-jpq5r                1/1     Running   0          3h33m
    etcd-kube-master-1                      1/1     Running   0          3h32m
    etcd-kube-master-2                      1/1     Running   0          3h7m
    etcd-kube-master-3                      1/1     Running   0          3h4m
    kube-apiserver-kube-master-1            1/1     Running   0          3h32m
    kube-apiserver-kube-master-2            1/1     Running   0          3h7m
    kube-apiserver-kube-master-3            1/1     Running   0          3h4m
    kube-controller-manager-kube-master-1   1/1     Running   1          3h32m
    kube-controller-manager-kube-master-2   1/1     Running   0          3h7m
    kube-controller-manager-kube-master-3   1/1     Running   0          3h4m
    kube-flannel-ds-amd64-5q77t             1/1     Running   0          3h6m
    kube-flannel-ds-amd64-cz4wt             1/1     Running   0          71m
    kube-flannel-ds-amd64-hd79k             1/1     Running   0          71m
    kube-flannel-ds-amd64-p4c5d             1/1     Running   0          3h6m
    kube-flannel-ds-amd64-pn6zk             1/1     Running   0          3h4m
    kube-proxy-66jsj                        1/1     Running   0          3h33m
    kube-proxy-btqnz                        1/1     Running   0          71m
    kube-proxy-kwnkx                        1/1     Running   0          3h7m
    kube-proxy-nfrfw                        1/1     Running   0          71m
    kube-proxy-xdr9d                        1/1     Running   0          3h4m
    kube-scheduler-kube-master-1            1/1     Running   1          3h32m
    kube-scheduler-kube-master-2            1/1     Running   0          3h7m
    kube-scheduler-kube-master-3            1/1     Running   0          3h4m

## 参考文档

+ [Options for Highly Available topology](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/)
+ [Creating Highly Available clusters with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/)
