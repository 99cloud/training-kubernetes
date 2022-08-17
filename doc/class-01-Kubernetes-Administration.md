# Kubernetes-Administration

## 1. Prefix

- 授课时长：
    - 上午：9:30 至 12:00
    - 下午：13:30 至 16:00
- Prerequisite
    - vi 基础操作 -- 编辑、修改、保存文件
    - 网络基础知识 -- 网段 cidr、vlan、vxlan、配置 linux 网卡等等
    - 基础的 linux 知识 -- 权限、文件系统、服务
    - systemd 的基础操作 -- 重启、关闭、启动、重载、查看 systemd 的服务

## 2. Catalog

| Date | Time | Title | Content |
| ---- | ---- | ----- | ------- |
| 第 1 天 | 上午 | [1. Linux 容器和 Docker](#lesson-01lxc--docker) | [1.1 什么是 Linux 容器？](#11-什么是-linux-容器) |
| | | | [1.2 容器和虚拟机有何区别？](#12-容器和虚拟机有何区别) |
| | | | [1.3 Docker 和容器技术有什么关系？](#13-docker-和容器技术有什么关系) |
| | | | [1.4 Docker 的架构和概念空间是怎样的？](#14-docker-的架构和概念空间是怎样的) |
| | | | [1.5 什么是所谓的安全容器技术？](#15-什么是所谓的安全容器技术) |
| | | | [1.6 实验：Docker Quick Start](#16-实验docker-quick-start) |
| | 下午 | | [1.7 Docker 的网络模型](#17-docker-的网络模型) |
| | | | [1.8 Docker 的存储模型](#18-docker-的存储模型) |
| | | [2. Kubernetes 的快速入门](#lesson-02kubernetes-concepts) | [2.1 什么是 K8S？](#21-什么是-k8s) |
| | | | [2.2 K8S 是为了解决什么问题？](#22-k8s-是为了解决什么问题) |
| | | | [2.3 K8S 不解决什么问题？](#23-k8s-不解决什么问题) |
| | | | [2.4 K8S 的模块架构是怎样的？](#24-k8s-的模块架构是怎样的) |
| | | | [2.5 K8S 有哪些竞争产品？](#25-k8s-有哪些竞争产品) |
| | | | [2.6 怎么部署出一个 K8S 群集？](#26-怎么部署出一个-k8s-群集) |
| | | | [2.7 实验：K8S 的部署](#27-实验k8s-的部署) |
| | | | [2.8 什么是 Pod？](#28-什么是-pod) |
| | | | [2.9 实验：启动一个 pod ](#29-启动一个-pod) |
| 第 2 天 | 上午 | [3. K8S 的概念空间](#lesson-03k8s-concepts) | [3.1 什么是 YAML？](#31-什么是-yaml) |
| | | | [3.2 什么是 Namespace & Quota？](#32-什么是-namespace--quota) |
| | | | [3.3 什么是 Deployment & ReplicaSet？](#33-什么是-deployment--replicaset) |
| | | | [3.4 什么是 Services？](#34-什么是-services) |
| | | | [3.5 实验：K8S Dashboard](#35-实验k8s-dashboard) |
| | | | [3.6 实验：K8S 怎么发布服务和扩缩容？](#36-实验k8s-怎么发布服务和扩缩容) |
| | | | [3.7 DaemonSet & StatefulSet](#37-daemonset--statefulset) |
| | 下午 | | [3.8 实验：ETCD 操作](#38-实验etcd-操作) |
| | | | [3.9 什么是静态 Pod？](#39-什么是静态-pod) |
| | | [4. K8S 的认证和安全](#lesson-04k8s-auth--security) | [4.1 什么是 K8S 的 3A？](#41-什么是-k8s-的-3a) |
| | | | [4.2 怎么配置 kubectl？](#42-怎么配置-kubectl) |
| | | | [4.3 K8S 怎么保证网络安全？](#43-k8s-怎么保证网络安全) |
| | | | [4.4 什么是用户和角色？](#44-什么是用户和角色) |
| | | | [4.5 实验：添加用户 & 绑定角色](#45-实验添加用户--绑定角色) |
| 第 3 天 | 上午 | [5. K8S 的调度](#lesson-05-k8s-schedule) | [5.1 怎么部署一个多节点的 K8S 群集？](#51-怎么部署多节点的-k8s-集群) |
| | | | [5.2 怎么把应用部署到指定的 Node？](#52-怎么把应用部署到指定的-node) |
| | | | [5.3 什么是 Taints & Toleration？](#53-什么是-taints--toleration) |
| | | | [5.4 什么是 Node Affinity？](#54-什么是-node-affinity) |
| | | | [5.5 什么是 Pod Affinity？](#55-什么是-pod-affinity) |
| | | | [5.6 实验：Pod 调度](#56-实验pod-调度) |
| | 下午 | [6. K8S 的数据持久化](#lesson-06-k8s-storage) | [6.1 什么是 ConfigMap & Secret？](#61-什么是-configmap--secret) |
| | | | [6.2 什么是 PV / PVC？](#62-什么是-pv--pvc) |
| | | | [6.3 什么是 Storage Class？](#63-什么是-storage-class) |
| | | | [6.4 实验：ConfigMap / Secret / PV & PVC / StorageClass](#64-实验configmap--secret--pv--pvc--storageclass) |
| | | [7. 服务发布](#lesson-07-service) | [7.1 Service 在底层是怎么实现的？](#71-service-在底层是怎么实现的) |
| | | | [7.2 实验：发布服务](#72-实验发布服务) |
| | | | [7.3 什么是 Ingress？](#73-什么是-ingress) |
| | | | [7.4 实验：对集群外发布服务](#74-实验对集群外发布服务) |
| | | [8. 其它](#lesson-08advance) | [8.1 监控、日志、排错](#81-监控日志排错) |
| | | | [8.2 什么是 HPA / CA / VA？](#82-什么是-hpa--ca--va) |
| | | | [8.3 什么是 Federation？](#83-什么是-federation) |
| | | | [8.4 K8S 怎么处理有状态服务？](#84-k8s-怎么处理有状态服务) |
| | | | [8.5 其它参考](#85-其它参考) |
| 第 4 天 | 上午 | [9. CKA 考试讲解](#lesson-09cka) | [9.1 考试注意事项](#91-考试注意事项) |
| | | | [9.2 模拟题讲解](#92-模拟题讲解) |
| | 下午 | | [9.3 实验：做模拟题](#93-实验做模拟题) |

## Lesson 01：LXC & Docker

### 1.1 什么是 Linux 容器？

- 开发技术的演进

    ![](../images/container-evolution.png)

- 演进（虚拟化和容器技术）是为了解决什么问题？资源隔离 & 资源限制
- 什么是 Linux 容器？namespace & cgroup
- 什么是 lxc namespace？

    ![](../images/kernel-user-mode.png)

- 什么是 CGroup？
- Mac 和 Win 上 有容器技术么？

### 1.2 容器和虚拟机有何区别？

- 原理
  - 一个 KVM 虚拟机就是一个 KVM 进程，N Core 就是 N 个线程
  - 一个容器是一组被 LXC API 隔离+限制约束的进程组，容器中的进程就是宿主机操作系统中的进程，一一对应
- 应用场景
  - 不同的内核
  - 不同的操作系统
  - 不同的 CPU 指令集

### 1.3 Docker 和容器技术有什么关系？

- 什么是 [Docker](https://docs.docker.com/engine/docker-overview/#namespaces)（ [QuickStart](https://docs.docker.com/get-started/) ）？

    ![](../images/docker-undertech.png)

- Docker 和容器有什么关系（ why Linus don't care docker ）？
- Docker 有哪些竞争产品？[CRI-O ？](https://zhuanlan.zhihu.com/p/30667806)

### 1.4 Docker 的架构和概念空间是怎样的？

- 概念空间

    ![](../images/docker-arch.png)

- 模块架构

### 1.5 什么是所谓的安全容器技术？

- 容器的天然不安全与天然安全
- [Kata Container](https://katacontainers.io/learn/)，[PDF](https://katacontainers.io/collateral/kata-containers-1pager.pdf)

    ![](../images/katacontainers_traditionalvskata_diagram.jpg)

- 竞争者：gVisor / firecracker / rustVM

### 1.6 实验：Docker Quick Start

- 在 Ubuntu 18.04 / Ubuntu 20.04 / CentOS 7 上配置 Docker

    ```bash
    # 更新依赖仓库
    apt-get update -y || yum update -y

    # 安装 Docker
    apt-get install docker.io -y || yum install docker -y
    systemctl enable docker
    systemctl start docker

    # 检查 docker 服务状态
    systemctl status docker

    # ubuntu 中需要把 docker 的 cgroup driver 改成 systemd
    # !! centos 默认就是 systemd，不要修改这个文件，改了 docker 会起不来，保持 {} 就好
    vi /etc/docker/daemon.json

    {
      "exec-opts": ["native.cgroupdriver=systemd"]
    }

    systemctl restart docker

    # run hello-world
    docker run hello-world
    ```

  >Note：2021 年 7 月之后，ubuntu 环境 kubeadmin 默认都是 1.22+ 版本，因此需要将 docker 的 cgroup driver 改成 systemd（原来是 cgroup）。如果不改，后续 kubeadm init 时，会报错：`[kubelet-check] The HTTP call equal to 'curl -sSL http://localhost:10248/healthz' failed with error: Get "http://localhost:10248/healthz": dial tcp [::1]:10248: connect: connection refused.`
  >
  >检查 journalctl -x -u kubelet，可以看到：`Aug 07 15:10:45 ckalab2 kubelet[11394]: E0807 15:10:45.179485   11394 server.go:294] "Failed to run kubelet" err="failed to run Kubelet: misconfiguration: kubelet cgroup driver: \"systemd\" is different from docker cgroup driver: \"cgroupfs\""`
  >
  >看官方文档：<https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/>：`In v1.22, if the user is not setting the cgroupDriver field under KubeletConfiguration, kubeadm will default it to systemd.`
  >
  > 所以我们需要把 docker 的 cgroup driver 改成 systemd
  >
  > 修改步骤参考：<https://stackoverflow.com/questions/43794169/docker-change-cgroup-driver-to-systemd>
  >
  > 修改完成后，检查一下 docker cgroup，确保 docker cgroup 是 systemd 了：`sudo docker info | grep -i cgroup`

- 如何创建一个镜像？如何启动和调试容器？[Github](https://github.com/99cloud/lab-openstack/tree/master/src/docker-quickstart) 或 [Gitee](https://gitee.com/dev-99cloud/lab-openstack/tree/master/src/docker-quickstart)

    ```console
    $ mkdir ~/test
    $ cd ~/test
    $ wget https://gitee.com/dev-99cloud/lab-openstack/raw/master/src/docker-quickstart/app.py
    $ wget https://gitee.com/dev-99cloud/lab-openstack/raw/master/src/docker-quickstart/requirements.txt
    $ wget https://gitee.com/dev-99cloud/lab-openstack/raw/master/src/docker-quickstart/Dockerfile

    # 如果是 CentOS 7.x 需要安装下 python3
    $ yum install python3 python3-pip

    # pip3 install -r requirements.txt
    $ pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

    $ python3 app.py
     * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)

    # 此时可以从浏览器访问 http://<ip>/

    $ docker build --tag=friendlyhello .

    # 可以看一下本地镜像列表
    $ docker images

    # 删除已存在的 testFlask 容器
    $ docker rm testFlask 2>/dev/null

    # 以 99cloud/friendlyhello:3.9.6 镜像启动 testFlask 容器，容器内的 80 端口映射到宿主机的 4000 端口
    # 如果带 --rm 参数，stop 之后，就会直接 rm 容器
    $ docker run -p 4000:80 --name=testFlask 99cloud/friendlyhello:3.9.6
     * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)

    # 此时可以从浏览器访问 http://<ip>:4000

    # 如果要跑在后台，可以加 -d 参数
    $ docker run -d -p 4000:80 --name=testFlask 99cloud/friendlyhello:3.9.6

    # 进入容器调试
    $ docker exec -it testFlask /bin/bash
    root@4224b69e7ee3:/app# env
    HOSTNAME=4224b69e7ee3
    PWD=/app
    HOME=/root
    NAME=World
    ...

    root@4224b69e7ee3:/app# ps -ef

    # 查看容器日志
    $ docker logs -f testFlask

    # 结束容器
    $ docker stop testFlask

    # 启动容器
    $ docker start testFlask

    # 从容器生成新的镜像
    $ docker stop testFlask
    $ docker commit testFlask test-new

    # 删除容器
    $ docker rm testFlask

    # 删除镜像
    $ docker rmi friendlyhello
    $ docker rmi 99cloud/friendlyhello:3.9.6
    ```

- [Docker 官方入门参考资料](https://docs.docker.com/get-started/)

### 1.7 Docker 的网络模型

- Bridge 模式

    ![](images/bridge_network.jpeg)

    ```console
    # docker 容器实现没有把 network namespaces 放到标准路径 `/var/run/netns` 下，所以 `ip netns list` 命令看不到

    # 但是可以看 `ll /proc/<pid>/ns`，两个进程的 namespaces id 相同说明在同一个 namespaces

    [root@cloud025 ns]# ll /proc/2179/ns/
    total 0
    lrwxrwxrwx 1 root root 0 Aug 10 11:58 ipc -> ipc:[4026531839]
    lrwxrwxrwx 1 root root 0 Aug 10 11:58 mnt -> mnt:[4026531840]
    lrwxrwxrwx 1 root root 0 Aug 10 11:58 net -> net:[4026531956]
    lrwxrwxrwx 1 root root 0 Aug 10 11:58 pid -> pid:[4026531836]
    lrwxrwxrwx 1 root root 0 Aug 10 11:58 user -> user:[4026531837]
    lrwxrwxrwx 1 root root 0 Aug 10 11:58 uts -> uts:[4026531838]

    # 做个软链接，就可以看到 netns 了

    [root@cloud025 ns]# docker ps
    CONTAINER ID        IMAGE                         COMMAND                  CREATED             STATUS              PORTS                  NAMES
    07297a3ac7ea        nginx:latest                  "/docker-entrypoin..."   29 minutes ago      Up 29 minutes       80/tcp                 devtest
    0935b08509a4        test-new                      "python app.py"          35 minutes ago      Up 35 minutes       0.0.0.0:5000->80/tcp   testNew
    c23c76dd779c        99cloud/friendlyhello:3.9.6   "python app.py"          37 minutes ago      Up 36 minutes       0.0.0.0:4000->80/tcp   testFlask

    [root@cloud025 ns]# docker inspect testFlask | grep -i pid
                "Pid": 1159,
                "PidMode": "",
                "PidsLimit": 0,
    [root@cloud025 ns]# mkdir -p /var/run/netns
    [root@cloud025 ns]# ln -s /proc/1159/ns/net /var/run/netns/testFlask
    [root@cloud025 ns]# ip netns list
    testFlask (id: 0)
    devtest (id: 2)
    testNew (id: 1)

    # 进入对应的 namespaces，看 ip，pod namespace 里虚拟网卡的 link-netnsid 始终等于 0
    [root@cloud025 ns]# ip netns exec testNew ip a
    ...
    44: eth0@if45: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
        link/ether 02:42:ac:11:00:03 brd ff:ff:ff:ff:ff:ff link-netnsid 0
        inet 172.17.0.3/16 scope global eth0
          valid_lft forever preferred_lft forever
        inet6 fe80::42:acff:fe11:3/64 scope link
          valid_lft forever preferred_lft forever

    # 在 root namespaces 中 ip a，可以看到 link-netnsid = 1，1 是前面 ip netns list 里的 namespaces id
    [root@cloud025 ns]# ip a
    45: vethb6d08be@if44: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP group default
        link/ether 0e:d9:14:d1:86:98 brd ff:ff:ff:ff:ff:ff link-netnsid 1
        inet6 fe80::cd9:14ff:fed1:8698/64 scope link
          valid_lft forever preferred_lft forever

    # 这是一对 veth pair，看他们的序号和 if 可以发现

    # 看网桥，可以看到这个 root namespaces 的虚拟网卡绑在 docker0 网桥上
    # 在 CentOS 上，需要安装一下：yum install bridge-utils
    [root@cloud025 ~]# brctl show
    bridge name	bridge id		STP enabled	interfaces
    docker0		8000.02428c25c112	no		vethb6d08be
    virbr0		8000.525400d583b9	yes		virbr0-nic
    ```

    [可以尝试对虚拟网卡抓包，看进出容器的流量](#81-监控日志排错)

- Host 模式
- CNM

### 1.8 Docker 的存储模型

- [Mount 模式](https://docs.docker.com/storage/)

    ```console
    [root@cka-studenta-1 ~]# mkdir testhaha
    [root@cka-studenta-1 ~]# docker run -d -it --name devtest -v "$(pwd)"/testhaha:/app nginx:latest
    Unable to find image 'nginx:latest' locally
    Trying to pull repository docker.io/library/nginx ...
    latest: Pulling from docker.io/library/nginx
    ...
    7897813b7065a0390db335656443782895155655f263de6ee8264a6f2185fe16

    [root@cka-studenta-1 ~]# docker ps
    CONTAINER ID        IMAGE                         COMMAND                  CREATED             STATUS              PORTS                  NAMES
    7897813b7065        nginx:latest                  "/docker-entrypoin..."   6 seconds ago       Up 4 seconds        80/tcp                 devtest
    b667b8e2f90b        99cloud/friendlyhello:3.9.6   "python app.py"          3 hours ago         Up 3 hours          0.0.0.0:4000->80/tcp   testFlask
    [root@cka-studenta-1 ~]# docker exec -it 7897813b7065 /bin/sh

    # ls
    app  bin  boot  dev  docker-entrypoint.d  docker-entrypoint.sh  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
    # cd app
    # ls
    # echo fsdfasfdasdfsa > xxxxxxxx.txt
    # exit

    [root@cka-studenta-1 ~]# ls
    test  testhaha
    [root@cka-studenta-1 ~]# cd testhaha/
    [root@cka-studenta-1 testhaha]# ls
    xxxxxxxx.txt
    [root@cka-studenta-1 testhaha]# cat xxxxxxxx.txt
    fsdfasfdasdfsa
    ```

- Volumn 模式

## Lesson 02：Kubernetes Concepts

### 2.1 什么是 K8S？

- 什么是 Kubernetes？容器编排工具。为什么叫 K8S？
- K8S 和 Docker 有什么关系？参考：[Container runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)
    - Orchestration API -> Container API (cri-runtime) -> Kernel API(oci-runtime)
    - OCI：runC / Kata（ 及其前身 runV 和 Clear Containers ），gVisor，Rust railcar
        - 容器镜像的制作标准，即 ImageSpec。大致规定：容器镜像这个压缩了的文件夹里以 xxx 结构放 xxx 文件
        - 容器要需要能接收哪些指令，以及这些指令的行为，即 RuntimeSpec。这里面的大致内容就是“容器”要能够执行 “create”，“start”，“stop”，“delete” 这些命令，并且行为要规范。
        - Docker 则把 libcontainer 封装了一下，变成 runC 捐献出来作为 OCI 的参考实现。
    - CRI：Docker（ 借助 dockershim ），containerd（ 借助 CRI-containerd ），CRI-O，Frakti。是一组 gRPC 接口，[cri-api/pkg/apis/services.go](https://github.com/kubernetes/cri-api/blob/master/pkg/apis/services.go)：
        - 一套针对容器操作的接口，包括创建，启停容器等等
        - 一套针对镜像操作的接口，包括拉取镜像删除镜像等
        - 一套针对 PodSandbox（容器沙箱环境）的操作接口
    - 正常的 K8S 调用 Docker 流程

        ![](../images/k8s-CRI-OCI-docker.png)

    - containerd-1.0，对 CRI 的适配通过一个单独的进程 CRI-containerd 来完成

        ![](../images/k8s-containerd-1-0.png)

    - containerd-1.1，把适配逻辑作为插件放进了 containerd 主进程中

        ![](../images/k8s-containerd-1-1.png)

    - CRI-O，更为专注的 cri-runtime，非常纯粹，兼容 CRI 和 OCI，做一个 Kubernetes 专用的运行时

        ![](../images/k8s-cri-o-flow.png)

- [CRI-O](https://cri-o.io/) 的架构：

    ![](../images/k8s-cri-o-arch-1.png)

    ![](../images/k8s-cri-o-arch-2.jpg)

- K8S 和 Borg 有何关系？Start from Borg, however completely different!

    ![](../images/borg-arch.png)

### 2.2 K8S 是为了解决什么问题？

- K8S 有什么优势？适用于哪些场景？自动化编排：自愈，快速缩放，一键部署和升降级，备份恢复
- 如何查文档？[K8S](https://kubernetes.io/)，[OpenShift Origin](https://www.okd.io/)
- 其它资料：slack、cncf、quay.io

### 2.3 K8S 不解决什么问题？

- 用户管理
- 限流熔断：istio
- 监控审计：prometheus / grafana / alertmanager / elasticsearch / fluent / kibana
- 用户界面
- 中间件
- 底层云平台支持

### 2.4 K8S 的模块架构是怎样的？

- [K8S 有哪些组件](https://kubernetes.io/zh/docs/concepts/architecture/#)？api-server、kube-scheduler、kube-controller、etcd、coredns、kubelete、kubeproxy

- 整体结构图

    ![](../images/k8s-architecture.png)

### 2.5 K8S 有哪些竞争产品？

- [OpenShift](https://www.openshift.com/learn/what-is-openshift-x)
    - 和 K8S 相比，OpenShift（ 红帽最有价值的产品 ）有哪些优势？

        ![](../images/openshift-k8s.svg)

- VMware
- KubeSphere
- Rancher

### 2.6 怎么部署出一个 K8S 群集？

- kubeadm
- Ansible

### 2.7 实验：K8S 的部署

Ubuntu 18.04 / 20.04 (CentOS 7 见后面)

1. [安装 kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)

    ```bash
    # iptables 看到 bridged 流量
    cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
    net.bridge.bridge-nf-call-ip6tables = 1
    net.bridge.bridge-nf-call-iptables = 1
    EOF
    sudo sysctl --system

    # Install kubeadm
    apt-get update && apt-get install -y apt-transport-https curl
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
    deb https://apt.kubernetes.io/ kubernetes-xenial main
    EOF
    apt-get update -y && apt-get install -y kubelet kubeadm kubectl

    # 重启 kubelet
    systemctl daemon-reload
    systemctl restart kubelet

    # 检查 kubelet 状态，在加入 k8s 集群之前，kubelet 状态会一直处于 activating 状态
    systemctl status kubelet
    ```

1. [用 kubeadm 创建一个 k8s 群集](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)

    ```bash
    # 拉起 k8s 群集
    kubeadm init --pod-network-cidr 192.168.1.90/16

    # 配置 kubectl 客户端
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config
    ```

1. 此时可以观察到 node 并未 ready，导致 coredns 无法调度。接下来需要：[安装网络插件](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#pod-network)，[插件列表](https://kubernetes.io/docs/concepts/cluster-administration/addons/)，这里我们用 [Calico](https://docs.projectcalico.org/getting-started/kubernetes/quickstart)。

    ```bash
    # 添加网络插件
    # Install the Tigera Calico operator and custom resource definitions
    kubectl create -f https://docs.projectcalico.org/manifests/tigera-operator.yaml
    # Install Calico by creating the necessary custom resource
    kubectl create -f https://docs.projectcalico.org/manifests/custom-resources.yaml

    # 查看 pods 和 nodes 状态
    kubectl get pods --all-namespaces
    kubectl get nodes
    ```

1. 如果希望在国内环境中安装 K8S（不使用代理访问 gcr），步骤如下（环境是 CentOS 7）：

    ```bash
    # 3. 关闭防火墙（默认就是关闭的，不用做）
    # systemctl stop firewalld.service
    # systemctl disable firewalld.service

    # 4. 关闭 selinux（默认就是关闭的，不用做）
    # vi /etc/selinux/config
    # 将 SELINUX=enforcing 改为 SELINUX=disabled

    # 5. 关闭 swap（默认就是关闭的，不用做）
    # swapoff /dev/sda2
    # vi /etc/fstab
    # 在 swap 分区这行前加 # 禁用掉，保存退出
    # reboot

    # 6. 配置系统相关属性
    cat <<EOF > /etc/sysctl.d/k8s.conf
    net.bridge.bridge-nf-call-ip6tables = 1
    net.bridge.bridge-nf-call-iptables = 1
    net.ipv4.ip_forward = 1
    EOF

    sysctl -p
    sysctl --system

    # 7. 配置yum源
    cat <<EOF > /etc/yum.repos.d/kubernetes.repo
    [kubernetes]
    name=Kubernetes
    baseurl=http://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
    enabled=1
    gpgcheck=0
    repo_gpgcheck=0
    gpgkey=http://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg
            http://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
    EOF

    # 8. 安装 docker
    yum install docker -y
    systemctl enable docker --now

    # 9. 修改 docker 镜像代理仓库
    # vi /etc/docker/daemon.json
    # {
    #  "registry-mirrors": ["http://hub-mirror.c.163.com"]
    # }

    # systemctl daemon-reload
    # systemctl restart docker

    # 10. 下载 kubernetes
    # export k8s_version="1.20.1"
    export k8s_version="1.23.3"

    yum install -y kubelet-${k8s_version}-0 kubeadm-${k8s_version}-0 kubectl-${k8s_version}-0  --disableexcludes=kubernetes

    # 11. 启动 kubelet
    systemctl restart kubelet
    systemctl enable kubelet

    # 12. 用 kubeadm 初始化创建 K8S 集群
    kubeadm init --image-repository registry.aliyuncs.com/google_containers --kubernetes-version=v${k8s_version} --pod-network-cidr=10.244.0.0/16

    # 13. 配置 .kube/config 用于使用 kubectl
    mkdir -p $HOME/.kube
    cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    chown $(id -u):$(id -g) $HOME/.kube/config

    # 15. 安装 calico
    kubectl apply -f https://gitee.com/dev-99cloud/lab-openstack/raw/master/src/ansible-cloudlab-centos/playbooks/roles/init04-prek8s/files/calico-${k8s_version}.yml

    # 看到 node Ready 就 OK
    kubectl get nodes
    ```

1. 集群安装/加入 GPU 节点

    ```bash
    # 1. 节点安装显卡驱动
    # 可以参考 https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#abstract

    # 2. 安装 docker
    # 见上文

    # 3. 安装 nvidia-docker
    distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \ && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | sudo tee /etc/yum.repos.d/nvidia-docker.repo

    yum install -y nvidia-docker2
    # ubuntu 等其他系统安装参考文档 https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installing-on-centos-7-8

    # 4. 更改默认容器运行时
    # 编辑 `/etc/docker/daemon.json`， 添加如下字段:
    {
        "default-runtime": "nvidia",
        "runtimes": {
            "nvidia": {
                "path": "nvidia-container-runtime",
                "runtimeArgs": []
            }
        }
    }
    systemctl daemon-reload && systemctl restart docker

    # 5. 安装 k8s 集群或将集群加入节点即可

    # 6. 安装 vgpu 插件
    # * Nvidia 官方的插件只能在 k8s 上整卡调度，调度力度太大，在我们的场景中没有太大实际意义
    # * 阿里云 gpushare 是阿里云公有云使用的 cgpu 的部分开源项目，能对 gpu 进行显存划分，多容器调度，但是没有实现显存隔离
    # * 第四范式 vgpu 是第四范式开源的 vgpu 上层实现，底层核心逻辑是 libvgpu.so提供的，没有开源，可以实现对物理 gpu 的切分，实现了显存隔离。
    # 安装第四范式 vgpu 参考 `https://github.com/4paradigm/k8s-device-plugin/blob/master/README_cn.md#Kubernetes%E5%BC%80%E5%90%AFvGPU%E6%94%AF%E6%8C%81`
    ```

### 2.8 什么是 Pod？

- Pod 和容器的关系是什么？

    ```bash
    # pod 里的 pause 容器和业务容器共享 ipc / net / user namespaces
    [root@cloud025 ~]# ll /proc/10982/ns/
    total 0
    lrwxrwxrwx 1 root root 0 Aug 10 16:14 ipc -> ipc:[4026532513]
    lrwxrwxrwx 1 root root 0 Aug 10 15:33 mnt -> mnt:[4026532592]
    lrwxrwxrwx 1 root root 0 Aug 10 15:33 net -> net:[4026532516]
    lrwxrwxrwx 1 root root 0 Aug 10 15:33 pid -> pid:[4026532594]
    lrwxrwxrwx 1 root root 0 Aug 10 16:14 user -> user:[4026531837]
    lrwxrwxrwx 1 root root 0 Aug 10 16:14 uts -> uts:[4026532593]

    [root@cloud025 ~]# ll /proc/10893/ns/
    total 0
    lrwxrwxrwx 1 root root 0 Aug 10 15:33 ipc -> ipc:[4026532513]
    lrwxrwxrwx 1 root root 0 Aug 10 15:33 mnt -> mnt:[4026532511]
    lrwxrwxrwx 1 root root 0 Aug 10 15:33 net -> net:[4026532516]
    lrwxrwxrwx 1 root root 0 Aug 10 16:15 pid -> pid:[4026532514]
    lrwxrwxrwx 1 root root 0 Aug 10 16:15 user -> user:[4026531837]
    lrwxrwxrwx 1 root root 0 Aug 10 16:15 uts -> uts:[4026532512]
    ```

- 为什么调度的基本单位是 pod 不是容器？

### 2.9 启动一个 pod

- [Pod YAML](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      labels:
        env: test
    spec:
      containers:
      - name: nginx
        image: nginx
    ```

- 启动一个 Pod

    ```bash
    # 起 nginx pod
    kubectl apply -f nginx.yaml

    # 可以看到 pod 无法被调度，进行诊断
    kubectl describe pod nginx

    # 去污点、允许 pod 调度到 master
    kubectl taint nodes $(hostname) node-role.kubernetes.io/master:NoSchedule-

    # 查看 pods
    kubectl get pods

    # 查看容器
    docker ps | grep nginx
    ```

- 在容器平台上发布 Python 应用
    - 我们将要做什么？
        - 下载应用代码，并且在本地跑起来
        - 为应用构建一个 Docker 镜像，然后启动一个 Docker 容器来运行此应用
        - 创建一个 Deployment 对象，将应用运行在 K8S 平台上
        - 参考：<https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/>
        - 对应的原始代码在：<https://github.com/JasonHaley/hello-python>
    - 预置条件有哪些？
        - 本地具备 Python 3.6+ 的运行环境
        - 安装了 Git（非必须）
        - 安装了 Docker
        - 一个 Kubernetes 平台
    - [代码](../src/hello-python)
        - 其中 `requirements.txt` 里只有一行：flask，是依赖包列表文件
        - 另一个文件是 `main.py`，是应用的逻辑代码

            ```python
            from flask import Flask
            import os
            import socket

            app = Flask(__name__)

            @app.route("/")
            def hello():
                html = "<h3>Hello {name}!</h3>" \
                       "<b>Hostname:</b> {hostname}<br/>"
                return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

            if __name__ == "__main__":
                app.run(host='0.0.0.0')
            ```

    - 下载代码

        ```bash
        mkdir ~/test-hello-world
        cd ~/test-hello-world/

        wget https://gitee.com/dev-99cloud/training-kubernetes/raw/master/src/hello-python/main.py
        wget https://gitee.com/dev-99cloud/training-kubernetes/raw/master/src/hello-python/requirements.txt
        wget https://gitee.com/dev-99cloud/training-kubernetes/raw/master/src/hello-python/Dockerfile
        wget https://gitee.com/dev-99cloud/training-kubernetes/raw/master/src/hello-python/deployment.yaml
        ```

    - 本地运行：
        - 安装依赖：`pip3 install -r requirements.txt`
        - 本地运行：`python3 main.py`，会在本地启动一个用于开发的 web 服务器。
        - 你可以打开浏览器，访问 `http://<IP>:5000` 端口
    - Docker 镜像构建文件，目录下有一个 Dockerfile 文件

        ```dockerfile
        FROM python:3.7

        RUN mkdir /app
        WORKDIR /app
        ADD . /app/
        RUN pip install -r requirements.txt

        EXPOSE 5000
        CMD ["python", "/app/main.py"]
        ```

    - 构建 Docker 镜像并运行
        - 运行命令构建镜像：`docker build -f Dockerfile -t hello-python:latest .`
        - 构建完成后，可以通过 `docker image ls` 看到刚才构建的镜像
        - 然后运行此镜像：`docker run -p 5001:5000 hello-python`
        - 然后访问 `http://<IP>:5001`，同样可以看到 `Hello form Python!` 字符串
    - 确定 Kubernetes 和 kubectl 运行正常
        - 运行命令：`kubectl version`，如果该命令不报错，就说明 kubectl 安装完成。
        - 运行命令：`kubectl get nodes`，如果返回节点信息，说明 K8S 运行正常，kubectl 配置正常。
    - K8S deployment YAML 文件：

        ```yaml
        apiVersion: v1
        kind: Service
        metadata:
          name: hello-python-service
        spec:
          type: NodePort
          selector:
            app: hello-python
          ports:
          - protocol: "TCP"
            port: 6000
            targetPort: 5000
            nodePort: 31000

        ---
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: hello-python
        spec:
          selector:
            matchLabels:
              app: hello-python
          replicas: 4
          template:
            metadata:
              labels:
                app: hello-python
            spec:
              containers:
              - name: hello-python
                image: hello-python:latest
                imagePullPolicy: Never
                ports:
                - containerPort: 5000
        ```

    - 将 Deployment 部署到 K8S 平台
        - 运行命令：`kubectl apply -f deployment.yaml`
        - 运行命令：`kubectl get pods，检查 pods`
        - 然后可以打开浏览器，在 `http://<IP>:31000` 看到 `Hello form Python!` 信息

    - 实验

        ```bash
        # 观察 service / deployment 和 pod 的关系，通过 label 关联
        kubectl get pods -l app=hello-python
        kubectl get deploy
        kubectl get deployment

        kubectl get svc
        kubectl get service
        kubectl get pods -l app=hello-python -o wide

        # 访问应用
        curl http://<pod-ip>:5000
        curl http://<cluster-ip>:6000
        curl http://<host-ip>:31000
        ```

## Lesson 03：K8S concepts

### 3.1 什么是 YAML？

- 怎么理解 YAML？列表 / 字典 / 数字 / 字符串 / Bool

### 3.2 什么是 Namespace & Quota？

- Namespace & 租户隔离
- [实验：namespace & quota](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)

    ```bash
    # 创建一个 namespace
    kubectl create namespace quota-mem-cpu-example

    # 为这个 namespace 限定配额
    kubectl apply -f https://k8s.io/examples/admin/resource/quota-mem-cpu.yaml --namespace=quota-mem-cpu-example

    # 查看配额的详细信息
    kubectl get resourcequota mem-cpu-demo --namespace=quota-mem-cpu-example --output=yaml

    # 创建一个 pod，并限制它的资源使用
    kubectl apply -f https://k8s.io/examples/admin/resource/quota-mem-cpu-pod.yaml --namespace=quota-mem-cpu-example

    # 确认 pod 已经启动
    kubectl get pod quota-mem-cpu-demo --namespace=quota-mem-cpu-example

    # 再次查看配额信息，检查已用部分
    kubectl get resourcequota mem-cpu-demo --namespace=quota-mem-cpu-example --output=yaml

    # 尝试启动第二个 pod，因为配额原因，失败
    kubectl apply -f https://k8s.io/examples/admin/resource/quota-mem-cpu-pod-2.yaml --namespace=quota-mem-cpu-example

    # Error from server (Forbidden): error when creating "examples/admin/resource/quota-mem-cpu-pod-2.yaml":pods "quota-mem-cpu-demo-2" is forbidden: exceeded quota: mem-cpu-demo, requested: requests.memory=700Mi,used: requests.memory=600Mi, limited: requests.memory=1Gi

    # 删除命名空间
    kubectl delete namespace quota-mem-cpu-example
    ```

### 3.3 什么是 Deployment & ReplicaSet？

- 实验：Pod Label 和 Replica Controller
- [实验：Deployment 相关](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

    ```bash
    kubectl apply -f https://k8s.io/examples/controllers/nginx-deployment.yaml
    kubectl get pods
    kubectl get deployments

    kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1 --record
    kubectl get pods

    kubectl set image deployment.v1.apps/nginx-deployment nginx=nginx:1.161 --record=true
    kubectl get pods

    kubectl rollout history deployment.v1.apps/nginx-deployment
    kubectl rollout history deployment.v1.apps/nginx-deployment --revision=2
    kubectl rollout undo deployment.v1.apps/nginx-deployment --to-revision=2
    kubectl get pods
    # 如果原来的 ErrorImagePull 的 pod 一直失败，可以 kuctl delete pod <pod-name> 删除掉

    kubectl scale deployment.v1.apps/nginx-deployment --replicas=10
    kubectl get pods
    ```

### 3.4 什么是 Services？

- 基本概念：Service
- 实验：Service

    创建文件 service.yaml，内容如下：

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: hello-python-service
    spec:
      type: NodePort
      selector:
        app: nginx
      ports:
      - protocol: "TCP"
        port: 6000
        targetPort: 80
        nodePort: 31000
    ```

    ```bash
    kubectl apply -f service.yaml
    ```

    ```console
    # 建好 services 后，可以看 iptables
    $ iptables -t nat -n -L -v

    # 能看到如下字样，进入 service IP 的请求按比例分给各个 pod
    Chain KUBE-SVC-C5I534CP62HG2LN3 (2 references)
    pkts bytes target     prot opt in     out     source               destination
        0     0 KUBE-SEP-FBKE4RDEE4U4O7NI  all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* default/hello-python-service */ statistic mode random probability 0.50000000000
        0     0 KUBE-SEP-ZIK7TOCY5OVWTBMA  all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* default/hello-python-service */

    kubectl get pods -o wide
    kubectl run curl --image=radial/busyboxplus:curl -i --tty

    nslookup hello-python-service
    curl http://hello-python-service.default.svc.cluster.local:6000

    # 在不同的 namespaces 或者宿主机节点上，需要 FQDN 长名
    nslookup hello-python-service.default.svc.cluster.local 10.96.0.10
    ```
- LB 类型的 Service：[metallb](https://metallb.universe.tf/)

### 3.5 实验：K8S Dashboard

### 3.6 实验：K8S 怎么发布服务和扩缩容？

- [实验：通过 Service 发布服务](https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/)
- 实验：通过 Deployment 扩缩容

### 3.7 DaemonSet & StatefulSet

- [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)

    ```yaml
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: fluentd-elasticsearch
      namespace: kube-system
      labels:
        k8s-app: fluentd-logging
    spec:
      selector:
        matchLabels:
          name: fluentd-elasticsearch
      template:
        metadata:
          labels:
            name: fluentd-elasticsearch
        spec:
          containers:
          - name: fluentd-elasticsearch
            image: quay.io/fluentd_elasticsearch/fluentd:v2.5.2
            resources:
              limits:
                memory: 200Mi
              requests:
                cpu: 100m
                memory: 200Mi
          terminationGracePeriodSeconds: 30
    ```

- [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: nginx
      labels:
        app: statefulset
    spec:
      ports:
      - port: 80
        name: web
      clusterIP: None
      selector:
        app: statefulset
    ---
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: web
    spec:
      selector:
        matchLabels:
          app: statefulset # has to match .spec.template.metadata.labels
      serviceName: "nginx"
      replicas: 3 # by default is 1
      template:
        metadata:
          labels:
            app: statefulset # has to match .spec.selector.matchLabels
        spec:
          terminationGracePeriodSeconds: 10
          containers:
          - name: nginx
            image: nginx
            ports:
            - containerPort: 80
              name: web
    ```

    ```bash
    kubectl apply -f test-statefulset.yaml
    kubectl get pods

    # headless 服务，没有 service IP
    kubectl run curl --image=radial/busyboxplus:curl -i --tty
    nslookup nginx

    # 多执行几次 nslookup nginx 命令，可以看到每次返回的顺序都不一样
    # headless 服务就是通过 dns 返回顺序变化来实现负载均衡
    ```

### 3.8 实验：ETCD 操作

 - Set & Get

    ```console
    # Ubuntu 环境上用 apt-get 安装
    root@ckalab001:~# apt install etcd-client

    # 其它环境直接 https://github.com/etcd-io/etcd/releases 下载二进制文件

    root@ckalab001:~# ps -ef | grep api | grep -i etcd
    root       24761   24743  3 10:17 ?        00:06:53 kube-apiserver --advertise-address=172.31.43.206 --allow-privileged=true --authorization-mode=Node,RBAC --client-ca-file=/etc/kubernetes/pki/ca.crt --enable-admission-plugins=NodeRestriction --enable-bootstrap-token-auth=true --etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt --etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt --etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key --etcd-servers=https://127.0.0.1:2379 --insecure-port=0 --kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt --kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname --proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.crt --proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client.key --requestheader-allowed-names=front-proxy-client --requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-ca.crt --requestheader-extra-headers-prefix=X-Remote-Extra- --requestheader-group-headers=X-Remote-Group --requestheader-username-headers=X-Remote-User --secure-port=6443 --service-account-issuer=https://kubernetes.default.svc.cluster.local --service-account-key-file=/etc/kubernetes/pki/sa.pub --service-account-signing-key-file=/etc/kubernetes/pki/sa.key --service-cluster-ip-range=10.96.0.0/12 --tls-cert-file=/etc/kubernetes/pki/apiserver.crt --tls-private-key-file=/etc/kubernetes/pki/apiserver.key

    # 设置环境变量，ETCDCTL_API=3
    root@ckalab001:~# export ETCDCTL_API=3

    root@ckalab001:~# etcdctl --cert="/etc/kubernetes/pki/apiserver-etcd-client.crt" --key="/etc/kubernetes/pki/apiserver-etcd-client.key" --cacert="/etc/kubernetes/pki/etcd/ca.crt" --endpoints=https://127.0.0.1:2379 put /firstkey trystack
    OK

    root@ckalab001:~# etcdctl --cert="/etc/kubernetes/pki/apiserver-etcd-client.crt" --key="/etc/kubernetes/pki/apiserver-etcd-client.key" --cacert="/etc/kubernetes/pki/etcd/ca.crt" --endpoints=https://127.0.0.1:2379 get /firstkey
    /firstkey
    trystack
    ```

    ```bash
    # list 所有的 key
    etcdctl --cert="/etc/kubernetes/pki/apiserver-etcd-client.crt" --key="/etc/kubernetes/pki/apiserver-etcd-client.key" --cacert="/etc/kubernetes/pki/etcd/ca.crt" --endpoints=https://127.0.0.1:2379 get --prefix --keys-only ""

    # list 所有的 key & value
    etcdctl --cert="/etc/kubernetes/pki/apiserver-etcd-client.crt" --key="/etc/kubernetes/pki/apiserver-etcd-client.key" --cacert="/etc/kubernetes/pki/etcd/ca.crt" --endpoints=https://127.0.0.1:2379 get --prefix ""

    # backup & restore
    etcdctl --cert="/etc/kubernetes/pki/apiserver-etcd-client.crt" --key="/etc/kubernetes/pki/apiserver-etcd-client.key" --cacert="/etc/kubernetes/pki/etcd/ca.crt" --endpoints=https://127.0.0.1:2379 snapshot save a.txt
    # etcdctl --cert="/etc/kubernetes/pki/apiserver-etcd-client.crt" --key="/etc/kubernetes/pki/apiserver-etcd-client.key" --cacert="/etc/kubernetes/pki/etcd/ca.crt" --endpoints=https://127.0.0.1:2379 snapshot restore a.txt
    ```

### 3.9 什么是静态 Pod？

- [Static Pod](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/)
- /etc/kubernetes/manifests

    ```console
    root@CKA003:~# ps -ef | grep kubelet
    root     10572     1  2 09:37 ?        00:07:41 /usr/bin/kubelet --bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf --config=/var/lib/kubelet/config.yaml --cgroup-driver=cgroupfs --network-plugin=cni --pod-infra-container-image=k8s.gcr.io/pause:3.2 --resolv-conf=/run/systemd/resolve/resolv.conf

    root@CKA003:~# grep mani /var/lib/kubelet/config.yaml
    staticPodPath: /etc/kubernetes/manifests

    root@CKA003:~# cd /etc/kubernetes/manifests
    root@CKA003:/etc/kubernetes/manifests# ls
    etcd.yaml  kube-apiserver.yaml  kube-controller-manager.yaml  kube-scheduler.yaml  static-web.yaml

    root@CKA003:/etc/kubernetes/manifests# cat static-web.yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: static-web
    labels:
      role: myrole
    spec:
      containers:
      - name: web
        image: nginx
        ports:
          - name: web
            containerPort: 80
            protocol: TCP

    root@CKA003:/etc/kubernetes/manifests# kubectl get pods
    NAME                READY   STATUS    RESTARTS   AGE
    dnsutils            1/1     Running   4          4h17m
    static-web          1/1     Running   0          98m
    static-web-cka003   1/1     Running   0          98m
    web-0               0/1     Pending   0          116m

    root@CKA003:/etc/kubernetes/manifests# kubectl delete pod static-web
    pod "static-web" deleted
    root@CKA003:/etc/kubernetes/manifests# kubectl get pods
    NAME                READY   STATUS    RESTARTS   AGE
    dnsutils            1/1     Running   4          4h17m
    static-web-cka003   1/1     Running   0          99m
    web-0               0/1     Pending   0          117m

    root@CKA003:/etc/kubernetes/manifests# kubectl delete pod static-web-cka003
    pod "static-web-cka003" deleted
    root@CKA003:/etc/kubernetes/manifests# kubectl get pods
    NAME                READY   STATUS    RESTARTS   AGE
    dnsutils            1/1     Running   4          4h18m
    static-web-cka003   1/1     Running   0          10s
    web-0               0/1     Pending   0          117m

    root@CKA003:/etc/kubernetes/manifests# ls
    etcd.yaml  kube-apiserver.yaml  kube-controller-manager.yaml  kube-scheduler.yaml  static-web.yaml
    root@CKA003:/etc/kubernetes/manifests# rm -rf static-web.yaml
    root@CKA003:/etc/kubernetes/manifests# kubectl get pods
    NAME       READY   STATUS    RESTARTS   AGE
    dnsutils   1/1     Running   4          4h18m
    web-0      0/1     Pending   0          117m
    ```

## Lesson 04：K8S Auth & Security

### 4.1 什么是 K8S 的 3A？

- Authentication / Authorization / Admission
- K8S 的认证过程？Authentication、Authorization（ RBRA / ABAC / WebHook ）、Admission Controller

### 4.2 怎么配置 kubectl？

###	4.3 K8S 怎么保证网络安全？

- Kubernetes 的网络选型？flannel、calico、ovs、ovn

### 4.4 什么是用户和角色？

### 4.5 实验：添加用户 & 绑定角色

- 实验：创建 Normal 用户使用 kubectl 工具

    ```console
    root@CKA003:~# kubectl config get-contexts
    CURRENT   NAME                          CLUSTER      AUTHINFO           NAMESPACE
    *         kubernetes-admin@kubernetes   kubernetes   kubernetes-admin

    root@CKA003:~# kubectl create namespace ns1
    namespace/ns1 created
    root@CKA003:~# kubectl create namespace ns2
    namespace/ns2 created

    root@CKA003:~# useradd -m -d /home/poweruser -s /bin/bash poweruser
    root@CKA003:~# passwd poweruser
    Enter new UNIX password:
    Retype new UNIX password:
    passwd: password updated successfully
    root@CKA003:~# cd /home/poweruser

    root@CKA003:/home/poweruser# openssl genrsa -out poweruser.key 2048
    Generating RSA private key, 2048 bit long modulus (2 primes)
    ......................+++++
    ..........................................................+++++
    e is 65537 (0x010001)

    root@CKA003:/home/poweruser# openssl req -new -key poweruser.key -out poweruser.csr -subj "/CN=poweruser/O=ns1"
    Can't load /root/.rnd into RNG
    139904427348416:error:2406F079:random number generator:RAND_load_file:Cannot open file:../crypto/rand/randfile.c:88:Filename=/root/.rnd

    root@CKA003:/home/poweruser# cat poweruser.key
    -----BEGIN RSA PRIVATE KEY-----
    MIIEowIBAAKCAQEAt07RnBpZFkux9vEmSUDiHsVFtAu1FmJQjia0ls2A/fbMBt2T
    ...
    njzqykeT5cLiixwUf6x35nF2r5VydsZMHypk6dgPgC6LikTbfsL0
    -----END RSA PRIVATE KEY-----

    root@CKA003:/home/poweruser# cat poweruser.csr
    -----BEGIN CERTIFICATE REQUEST-----
    MIICZzCCAU8CAQAwIjESMBAGA1UEAwwJcG93ZXJ1c2VyMQwwCgYDVQQKDANuczEw
    ...
    O5+ia4aC6Hn/lMsRNYzeSK/ovjMuzH7gjnYEogG8QdpIVLFF1a1D2/S1kQ==
    -----END CERTIFICATE REQUEST-----

    root@CKA003:/home/poweruser# openssl x509 -req -in poweruser.csr -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -out poweruser.crt -days 60
    Signature ok
    subject=CN = poweruser, O = ns1
    Getting CA Private Key

    root@CKA003:/home/poweruser# chmod 777 poweruser.*
    root@CKA003:/home/poweruser# cd

    root@CKA003:~# kubectl config set-credentials poweruser --client-certificate=/home/poweruser/poweruser.crt --client-key=/home/poweruser/poweruser.key
    User "poweruser" set.
    root@CKA003:~# mkdir /home/poweruser/.kube
    root@CKA003:~# cp .kube/config /home/poweruser/.kube
    root@CKA003:~# chown -R poweruser:poweruser /home/poweruser/.kube
    root@CKA003:~# su poweruser

    poweruser@CKA003:/root$ cd
    poweruser@CKA003:~$ cd .kube/
    poweruser@CKA003:~/.kube$ vi config

    # 打开并编辑 /home/poweruser/.kube/config 文件
    # 删除用户: kubernetes-admin 和他的证书，包括
    root@CKA003:~# vi /home/poweruser/.kube/config
    # 删除以下内容
    #- name: kubernetes-admin
    #  user:
    #    client-certificate-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUM4akNDQWRxZ0F3SUJBZ0lJS2xBVjZ0SGg0R3d3RFFZSktvWklodmNOQVFFTEJRQXdGVEVUTUJFR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB5TVRBNE1Ea3dOREkyTVRaYUZ3MHlNakE0TURrd05ESTJNVGhhTURReApGekFWQmdOVkJBb1REbk41YzNSbGJUcHRZWE4wWlhKek1Sa3dGd1lEVlFRREV4QnJkV0psY201bGRHVnpMV0ZrCmJXbHVNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTNQT2J2Ly9JK2FrQkFzR3YKeERPRlpEYnF6c1AwWCtTOExRa1dmMGhCKzBOc3dySHhQR0VTcmw0OXhhbUI4RVVod0NQTG9BTTVWZkRxOVNXWApsV1A0ZE1qM1cyclFFdmp4ZnlZZDhjbWdReTNVWndJSE1tUCtRS0NJNVdwV0tRcldlTE8rTXZUd1hjM0wwcWUyClRiMEhlQ0FjMy9FdWlZcFVvRjFrVndESGl5N3BpQTVTSVpsbGhub1Q1NjAyb3RDV0RYWDg1L09UOGRtWEViQTAKSlpkeDdhM2krT3I5dVdHQk1aaldEQms2dk02U3QxQm00MGhIcGM4VGpQSERZOVdwcldoVXZOUXpuNEtTSDdYQQpJQ1h1d3VmVVRVQXpGVWdobm5yZXc5MzFXd3NXejJpUlN6dldzUGdDOE8xMllNQmZQWGhoeXRRazFMSTdQaUVHCm1qbGw2UUlEQVFBQm95Y3dKVEFPQmdOVkhROEJBZjhFQkFNQ0JhQXdFd1lEVlIwbEJBd3dDZ1lJS3dZQkJRVUgKQXdJd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFGN3hOdWs5eEhtUDUydjh6REU3Uk9MTEU5cVlTMVhrd3I5Zgp2eTEvMVZKTklXV2Jlc3hQMUsvTm1JMTVJUS9TWWtoKzVoMWE4eGppRkc4dk5ia3BMNDAxUVpKTy93SEJYWU5WCkdXR0V4ZXRpdG5KSlpSam81NWN2NHpwTUNSOWZadmIvaGc3RzBCQmw2RW84MHNzSDJYdG5Ca04vV0VPY0VoZk8KQ2pFYkNGREVmbzFMRG9aTDZjZGwxU3dnTFlWZ3l6ZlQrcjdJVmNaZEVuWXZjMDhZNThLKzVPL3dMZnBaSjQxdwpVbWtQdzE3R0sxUjVUQUJrWHBRRFE5M3pwTnZ6M1k3ZUZlQTM5V2ZocGthZU4yRUpTQ3ZwdzdNaGQyTCtVUHFYCkdOSVpkNVYyOGF3d21GUUhURm9DdlZ0SUszMEFYMWQyTTkvNkpwMEUvNDdNZE1meWFNWT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=
    #    client-key-data: LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb2dJQkFBS0NBUUVBM1BPYnYvL0krYWtCQXNHdnhET0ZaRGJxenNQMFgrUzhMUWtXZjBoQiswTnN3ckh4ClBHRVNybDQ5eGFtQjhFVWh3Q1BMb0FNNVZmRHE5U1dYbFdQNGRNajNXMnJRRXZqeGZ5WWQ4Y21nUXkzVVp3SUgKTW1QK1FLQ0k1V3BXS1FyV2VMTytNdlR3WGMzTDBxZTJUYjBIZUNBYzMvRXVpWXBVb0Yxa1Z3REhpeTdwaUE1UwpJWmxsaG5vVDU2MDJvdENXRFhYODUvT1Q4ZG1YRWJBMEpaZHg3YTNpK09yOXVXR0JNWmpXREJrNnZNNlN0MUJtCjQwaEhwYzhUalBIRFk5V3ByV2hVdk5Rem40S1NIN1hBSUNYdXd1ZlVUVUF6RlVnaG5ucmV3OTMxV3dzV3oyaVIKU3p2V3NQZ0M4TzEyWU1CZlBYaGh5dFFrMUxJN1BpRUdtamxsNlFJREFRQUJBb0lCQUYvUmtYaTVMMm45dmI5NQpTWVUzcHFCb0pIb1lockRUWER2WGxoY0t1ZnFDS2ZkZy9iSG1reGhsTERxOUlPbVd3V1UyNE1aNnYzR2lzZkl3CkpFV1gvaFovVks0amF5cmZKTE8wVHdZZEgxQWkzdHJ4Q1RmMEh6M2RvS0NFOWVxRWxhL3dtd28wS00wMVF6QU8KcFVPZk4wOEQ5aUd6MFMrNmVxcTA5Wis1YWMvVWNLQWgyczNzL2hjSHlEUk9yeFpCd1JDY3RoTXlGdU03SklIaQp3dXZKTEJqZkdXVnhGNGdkWWRiMXdIMFdNZ2txanhkVDEvcWthSEE2TmtNTEZrRnZNdzRSTDdpbUdmMmcrVDBGCnB1WVorRW9oRGVtTEpCVGF5ZTM3ZjlST3pRRTBtTFNEa1E5WnRmZDBMOE5telJ2eUIzTTdXV0FtVXhaM2FuTk4KSE5RV0k1VUNnWUVBM3RNZVNUcEhyMU1YcmhzdTZ6SlNwUEh6a3hQVE95VlE3NjY5cjJ6ay9UeDNVUUFzSktoSAovNFlTWUNyTzh6Q09HY09va1EzWUNCQlJBU2dlNmp5ekR3L0duRmxzT3o4MVdIYWp0NlRjKzVzVFh3dk9EUkxrCmxCSDBHblhIbHJ0M2FzV1JBRS9xVVlzeVJhUEs4a0tzRHRidlk4RllnbzB0NHFCYnBTelo2VHNDZ1lFQS9ka1oKSGtNZG5OWHFYTk9jTnJ0YzlDaGRjeUpXR2ppMEpPQ3dSVVNyNzMxMGFhcm1JU2tOR0Q1NTNUSlhnRlBRb2t3QQpRaWNVQ2VUY0t3SkM0VUUrWEVYaEZKU3RwNmR4VDJlR1AyU2ZtMUxENUp2cWZiU2xuOU81Ni9MTTY1Ym9BbVJCCmtjMVl1M0ZjZ1BiYlRIMXI4K2FqK1IxUG5NdTBsT2ZRNUJHeUd5c0NnWUJ2MTZvSStXN0h5cjVGRHJIakxmUWIKaExKTXJaUEZ5VG94eEJURHU3WElnaFFsblIrTEdzaGdzbXdBeHh2dkp2ejhZNS8xaHV4YlI4MVE5bEZtSXllQgpOTnJzMlZtZzkxNFFWQ1JpNWlaaFIvcFdKN2U2Q2pTZk9jKzdoRWkxR00yYzB5T3Y4MnphbHpLWmo5Z3E5MW9qCmJMRGw4a001N0NFTzhveHRnUEN6eHdLQmdCQXZ6c1U2UEdJcTFkWHpmR3VWQ1BsY3RaREk2THFsVVA5bEFIaDYKUjRodTlJUmtiR1pDNnQzWDVnZHYxVnFPZmFoTHRseUJoMnFXR0YvNXRmQU5LLy9RU09qNkRoUzV2YVQxa2Y3cQoySzZiMlhmelpVRjh5bTdsbmw1b1RoN2JzWkd0ZU96bUxqbE5vanRyQWxMZlVJbnQ5QmpIZ0xNYjNqajhpenB2CjBtNmZBb0dBUGtqY0lhWE93dnhXdFhReCttWEVQWkQxUEoyeElWN240am9hNHJ4L0pqNmx6dmRhQ2xmZzlSYjEKVC81QjREcWViNC9udlA0WUpBSTR4RUxCTVI0N1EvbVBHVkFldXc0SmgyZ3RBdmx3S0RDOGliaTg0NzlKSi9qOQo2T2gzNkR1UVpoeU56QU1namxCZG5oNEk0UitYYmZZcEo2UjNSUE5jM2dWT1cvVkFPc009Ci0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0tCg==

    # 尝试获取 pod, 会失败因为我们没有给他设置 rbac 的权限
    poweruser@CKA003:~/.kube$ kubectl get pods
    Error from server (Forbidden): pods is forbidden: User "poweruser" cannot list resource "pods" in API group "" in the namespace "default"
    ```

    为 poweruser 用户绑定权限

    ```console
    root@CKA003:~# vi pod-read.yaml
    root@CKA003:~# cat pod-read.yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      namespace: ns1
      name: pod-reader
    rules:
    - apiGroups: [""] # "" indicates the core API group
      resources: ["pods"]
      verbs: ["get", "watch", "list"]

    root@CKA003:~# kubectl apply -f pod-read.yaml
    role.rbac.authorization.k8s.io/pod-reader created

    root@CKA003:~# vi role-binding.yaml
    root@CKA003:~# cat role-binding.yaml
    apiVersion: rbac.authorization.k8s.io/v1
    # This role binding allows "jane" to read pods in the "default" namespace.
    # You need to already have a Role named "pod-reader" in that namespace.
    kind: RoleBinding
    metadata:
      name: read-pods
      namespace: ns1
    subjects:
    # You can specify more than one "subject"
    - kind: User
      name: poweruser # "name" is case sensitive
      apiGroup: rbac.authorization.k8s.io
    roleRef:
    # "roleRef" specifies the binding to a Role / ClusterRole
      kind: Role #this must be Role or ClusterRole
      name: pod-reader # this must match the name of the Role or ClusterRole you wish to bind to
      apiGroup: rbac.authorization.k8s.io

    root@CKA003:~# kubectl apply -f role-binding.yaml
    rolebinding.rbac.authorization.k8s.io/read-pods created
    ```

    现在 poweruser 在默认的 default namespace 下获取 pod 列表会出现错误的情况

    ```console
    # 错误--没有 default namespace 下获取 pod 列表的权限,这是我们所希望得到的结果
    poweruser@CKA003:~/.kube$ kubectl get pods
    # 返回: Error from server (Forbidden): pods is forbidden: User "poweruser" cannot list resource "pods" in API group "" in the namespace "default"

    # ok
    poweruser@CKA003:~/.kube$ kubectl get pods -n ns1
    ```

- 实验：创建 Normal 用户并给予超级管理员组

    ```console
    root@CKA003:~# openssl genrsa -out superuser.key 2048
    Generating RSA private key, 2048 bit long modulus (2 primes)
    ..........................+++++
    ........................................................................................+++++
    e is 65537 (0x010001)

    root@CKA003:~# openssl req -new -key superuser.key -out superuser.csr -subj "/CN=superuser/O=system:masters"
    Can't load /root/.rnd into RNG
    139767359660480:error:2406F079:random number generator:RAND_load_file:Cannot open file:../crypto/rand/randfile.c:88:Filename=/root/.rnd

    root@CKA003:~# openssl x509 -req -in superuser.csr -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -out superuser.crt -days 60
    Signature ok
    subject=CN = "superuser", O = system:masters
    Getting CA Private Key
    ```

    system:masters 是默认的 [cluster-rolebinding group](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles)，参考：[How to view members of subject with Group kind](https://stackoverflow.com/questions/51612976/how-to-view-members-of-subject-with-group-kind)

    ```console
    root@CKA003:~# kubectl get clusterrolebindings -o go-template='{{range .items}}{{range .subjects}}{{.kind}}-{{.name}} {{end}} {{" - "}} {{.metadata.name}} {{"\n"}}{{end}}' | grep "^Group-system:masters"
    Group-system:masters   -  cluster-admin
    ```

    设置 kubectl config

    ```console
    root@CKA003:~# kubectl config set-credentials superuser --client-certificate=superuser.crt --client-key=superuser.key
    User "superuser" set.
    root@CKA003:~# tail -f .kube/config
    ...
    - name: poweruser
    user:
        client-certificate: /home/poweruser/poweruser.crt
        client-key: /home/poweruser/poweruser.key
    - name: superuser
    user:
        client-certificate: /root/superuser.crt
        client-key: /root/superuser.key

    root@CKA003:~# kubectl config set-context superuser-context --cluster=kubernetes --user=superuser
    Context "superuser-context" created.

    root@CKA003:~# kubectl config get-contexts
    CURRENT   NAME                          CLUSTER      AUTHINFO           NAMESPACE
    *         kubernetes-admin@kubernetes   kubernetes   kubernetes-admin
            superuser-context             kubernetes   superuser

    root@CKA003:~# kubectl config use-context superuser-context
    Switched to context "superuser-context".

    root@CKA003:~# kubectl config get-contexts
    CURRENT   NAME                          CLUSTER      AUTHINFO           NAMESPACE
            kubernetes-admin@kubernetes   kubernetes   kubernetes-admin
    *         superuser-context             kubernetes   superuser

    root@CKA003:~# kubectl get pods
    NAME       READY   STATUS    RESTARTS   AGE
    dnsutils   1/1     Running   4          4h49m
    web-0      0/1     Pending   0          149m
    ```

- 实验：创建 Service Account 并绑定角色

    ```console
    root@CKA003:~# kubectl create serviceaccount sa-cluster-admin --namespace=kube-system
    serviceaccount/sa-cluster-admin created

    root@CKA003:~# kubectl get secret --all-namespaces | grep sa-cluster-admin
    kube-system             sa-cluster-admin-token-k9xfp                     kubernetes.io/service-account-token   3      53s

    root@CKA003:~# kubectl describe secret -n kube-system sa-cluster-admin-token-k9xfp
    Name:         sa-cluster-admin-token-k9xfp
    Namespace:    kube-system
    Labels:       <none>
    Annotations:  kubernetes.io/service-account.name: sa-cluster-admin
                kubernetes.io/service-account.uid: 11deb8dd-5625-4d75-ad44-3beef1bcd995
    Type:  kubernetes.io/service-account-token
    Data
    ====
    ca.crt:     1025 bytes
    namespace:  11 bytes
    token:      eyJhbGciOiJSUzI1NiIsImtpZCI6InRBUkJ6bkxQMHNHSi1MejR4T2ZtYk43b1Y0S2M3MXZOMTMtQmtOaHpsbXMifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJzYS1jbHVzdGVyLWFkbWluLXRva2VuLWs5eGZwIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6InNhLWNsdXN0ZXItYWRtaW4iLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIxMWRlYjhkZC01NjI1LTRkNzUtYWQ0NC0zYmVlZjFiY2Q5OTUiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06c2EtY2x1c3Rlci1hZG1pbiJ9.Dr1aOVdwAXO_BPXlJAohKBjoxRhMmTWyfVy2AP3-D0V-2jzdzWKoEP_17wnAS3FP-hxuOtTr3XWN0zM4oAI8-CeXtP7AdB0sqZ9P7Wnp2s88DqDUNK0JUuYGke3js9xd44Bt5vhtRovNEMYEnLXj_NLOunW33f4g46ep4NvQpNGTd48BcgzFhiiWuXLKKGGoOZGrWlkXqyofE4li83B3D08oW-hjP4S0JBBXqmzpa0_PYi-hkPbirmn9J7F-oQd0So05uAzZROHSd7n8INlYwbJx2zRF8PKipscxu47ddEumr6R9b8qDDVolP5iawqFPeDTt9lOY7OdgEaVcL651UQ

    root@CKA003:~# vi sa-cluster-admin-rolebinding.yaml

    root@CKA003:~# cat sa-cluster-admin-rolebinding.yaml
    apiVersion: rbac.authorization.k8s.io/v1
    # This cluster role binding allows anyone in the "manager" group to read secrets in any namespace.
    kind: ClusterRoleBinding
    metadata:
      name: read-secrets-global
    subjects:
    - kind: User
      name: sa-cluster-admin
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: ClusterRole
      name: cluster-admin
      apiGroup: rbac.authorization.k8s.io

    root@CKA003:~# kubectl create -f sa-cluster-admin-rolebinding.yaml
    clusterrolebinding.rbac.authorization.k8s.io/read-secrets-global created

    root@CKA003:~# kubectl apply -f nginx-deployment.yaml --token=eyJhbGciOiJSUzI1NiIsImtpZCI6InRBUkJ6bkxQMHNHSi1MejR4T2ZtYk43b1Y0S2M3MXZOMTMtQmtOaHpsbXMifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJzYS1jbHVzdGVyLWFkbWluLXRva2VuLWs5eGZwIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6InNhLWNsdXN0ZXItYWRtaW4iLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIxMWRlYjhkZC01NjI1LTRkNzUtYWQ0NC0zYmVlZjFiY2Q5OTUiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06c2EtY2x1c3Rlci1hZG1pbiJ9.Dr1aOVdwAXO_BPXlJAohKBjoxRhMmTWyfVy2AP3-D0V-2jzdzWKoEP_17wnAS3FP-hxuOtTr3XWN0zM4oAI8-CeXtP7AdB0sqZ9P7Wnp2s88DqDUNK0JUuYGke3js9xd44Bt5vhtRovNEMYEnLXj_NLOunW33f4g46ep4NvQpNGTd48BcgzFhiiWuXLKKGGoOZGrWlkXqyofE4li83B3D08oW-hjP4S0JBBXqmzpa0_PYi-hkPbirmn9J7F-oQd0So05uAzZROHSd7n8INlYwbJx2zRF8PKipscxu47ddEumr6R9b8qDDVolP5iawqFPeDTt9lOY7OdgEaVcL651UQ
    deployment.apps/nginx-deployment created
    ```

## Lesson 05: K8S Schedule

### 5.1 怎么部署多节点的 k8s 集群？

- 参考资料
    - 官方文档：[如何利用 kubeadm 创建高可用集群？](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/)
    - [怎么部署一个 Multi-Node 的 K8S 环境？](deploy-k8s-manual.md)
    - [怎么部署一个 Dual Stack HA 的 K8S 环境？](basic.md)
    - [基于 AWS 部署高可用 Kubernetes 集群](deploy-aws-ha-k8s-cluster.md)
    - [openshift-container-platform-reference-architecture-implementation-guides](https://blog.openshift.com/openshift-container-platform-reference-architecture-implementation-guides/)

        ![](../images/openshift-ha-deployment.png)

        ![](../images/openshift-network-arch-azure.png)

    - 网络多平面

        ![](../images/k8s-deploy-ha-multus.png)

- 步骤

    1. 在 master 节点上取得 token 和 ca_hash

        ```console
        root@ckamaster003:~# kubeadm token create
        b6k3qj.avofghaucefqe0a8

        root@ckamaster003:~# kubeadm token list | grep -v TOKEN | awk '{print $1}' | head -n -1
        b6k3qj.avofghaucefqe0a8

        root@ckamaster003:~# openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'
        d7d0906ebe29f607587e404ef6c393169a51e5f6c81e22a2a48f30ef8702e12a

        root@ckamaster003:~# ifconfig | grep eth0 -A 1
        eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
                inet 172.31.43.105  netmask 255.255.240.0  broadcast 172.31.47.255
        ```

    2. 可以用 kubeadm 命令将新节点加入 k8s cluster，先在 master 节点上生成命令

        ```bash
        kubeadm token create
        master_ip=$(ifconfig | grep eth0 -A 1 | grep inet | awk '{print $2}')
        token=$(kubeadm token list | grep -v TOKEN | awk '{print $1}' | head -n 1)
        ca_hash=$(openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //')

        echo kubeadm join $master_ip:6443 --token $token --discovery-token-ca-cert-hash sha256:$ca_hash
        ```

    3. 然后将生成的命令复制到 worker 节点上执行，**执行之前，worker 节点上应该先安装 docker 和 kubeadm**
      - 参考 1.6 节，[在 Ubuntu 18.04 上配置 Docker](#16-实验docker-quick-start)
      - 参考 2.7 节，[安装 kubeadm](#27-实验k8s-的部署)
      - 然后将之前在 master 上生成的命令复制到 worker 节点上执行：`kubeadm join $master_ip:6443 --token $token --discovery-token-ca-cert-hash sha256:$ca_hash`

    4. 在新节点上配置 kubectl

        ```bash
        mkdir -p $HOME/.kube
        scp root@$master_ip:/etc/kubernetes/admin.conf $HOME/.kube/config
        chown $(id -u):$(id -g) $HOME/.kube/config
        ```

    5. 然后在新节点上用 kubectl 命令可以看到 node 已经 ready

        ```console
        root@ckaslave003:~# kubectl get nodes
        NAME           STATUS   ROLES    AGE   VERSION
        ckamaster003   Ready    master   20m   v1.18.3
        ckaslave003    Ready    <none>   33s   v1.18.3
        ```

### 5.2 怎么把应用部署到指定的 Node？

- 参考：[Labels and Selectors](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: label-demo
      labels:
        environment: production
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
    ```

    ```bash
    # 创建一个带 label 的 pod 对象 label-pod.yaml，内容如上

    kubectl apply -f label-pod.yaml
    ```

    ```console
    root@ckatest:~# kubectl get pods -l environment=production
    NAME         READY   STATUS    RESTARTS   AGE
    label-demo   1/1     Running   0          4m16s
    root@ckatest:~# kubectl get pods -l environment=production,tier=frontend
    No resources found in default namespace.

    root@ckatest:~# kubectl get pods -l 'environment in (production),tier in (frontend)'
    No resources found in default namespace.
    root@ckatest:~# kubectl get pods -l 'environment in (production, qa)'
    NAME         READY   STATUS    RESTARTS   AGE
    label-demo   1/1     Running   0          4m42s
    root@ckatest:~# kubectl get pods -l 'environment,environment notin (frontend)'
    NAME         READY   STATUS    RESTARTS   AGE
    label-demo   1/1     Running   0          4m50s
    ```

- 参考：[Assigning Pods to Nodes](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/)
- 实验：
  1. 如何根据 label 选择 node 启动 pod？（参考上方示例）
  1. 如何根据 node 名称选择 node 启动 pod？

      ```yaml
      apiVersion: v1
      kind: Pod
      metadata:
        name: nginx
      spec:
        nodeName: foo-node # schedule pod to specific node
        containers:
        - name: nginx
          image: nginx
          imagePullPolicy: IfNotPresent
      ```

Node Selector 实际是节点亲和，用于将 pod 部署到特定节点

### 5.3 什么是 Taints & Toleration？

- 参考: [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
- 实验

    为 master 节点打上 taint

    ```bash
    kubectl taint nodes k8s-masterXXX key=value:NoSchedule
    ```

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx5
    spec:
      containers:
      - name: nginx
        image: nginx
        imagePullPolicy: IfNotPresent
      nodeSelector:
        node-role.kubernetes.io/master: ""
      tolerations:
      - key: "key"
        operator: "Equal"
        value: "value"
        effect: "NoSchedule"
    ```

- 如果不用 node selector，而是直接用 nodeName，可以无视 NoSchedule Taint，可以被调度。但调度上去之后，会被 NoExcute Taint 驱逐。

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
    spec:
      nodeName: ckamaster003
      containers:
      - name: nginx
        image: nginx
        imagePullPolicy: IfNotPresent
    ```

Taint 实际上是节点反亲和，不允许 pod 部署到带 taint 的节点。

Toleration 和 Taint 结合，可以让特定节点只允许运行特定 pod，专节点专用。

### 5.4 什么是 Node Affinity？

- 参考：[Assign Pods to Nodes using Node Affinity](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)

思考：

1. Node Affinity 和 Node Selector 的关系？

### 5.5 什么是 Pod Affinity？

- [Inter-pod affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity)

### 5.6 实验：Pod 调度

## Lesson 06: K8S Storage

### 6.1 什么是 ConfigMap & Secret？

- [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/)
    - 参考：[Configure a Pod to Use a ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)
    - 参考：[Configuring Redis using a ConfigMap](https://kubernetes.io/docs/tutorials/configuration/configure-redis-using-configmap/)

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: example
    data:
      example.property.1: hello
      example.property.2: world
      example.property.file: |-
        property.1=value-1
        property.2=value-2
        property.3=value-3
    ```

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: configmap-demo-pod
    spec:
      containers:
        - name: nginx
          image: nginx
          env:
            - name: TEST1
              valueFrom:
                configMapKeyRef:
                  name: example
                  key: example.property.2
          volumeMounts:
          - name: config
            mountPath: "/config"
            readOnly: true
      volumes:
        - name: config
          configMap:
            name: example
    ```

    ```console
    root@ckamaster003:~# kubectl exec -it configmap-demo-pod /bin/sh

    # env | grep TEST
    TEST1=world

    # ls /config
    example.property.1  example.property.2	example.property.file
    ```

- [Secret](https://kubernetes.io/docs/concepts/configuration/secret/)

    Secret 和 ConfigMap 都用于配置，但 Secret 会对内容编码或加密

### 6.2 什么是 PV / PVC？

- [Types of Volumes](https://kubernetes.io/docs/concepts/storage/volumes/#types-of-volumes)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Configure a Pod to Use a Volume for Storage](https://kubernetes.io/docs/tasks/configure-pod-container/configure-volume-storage/)
- [Configure a Pod to Use a PersistentVolume for Storage](https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/)，注意 hostpath 对应到 node 上的路径，要看好 pod 跑在哪个 node 上，最好事先 taint slave node，或者 node select 指定 pod 跑在 master 上，这样就没问题了。

### 6.3 什么是 Storage Class？

- [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
- [Dynamic Volume Provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/)
    - [NFS](../src/config-lab/README.md#3-集成-nfs-存储) storage class

### 6.4 实验：ConfigMap / Secret / PV & PVC / StorageClass

## Lesson 07: Service

### 7.1 Service 在底层是怎么实现的？

- [Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Connecting Applications with Services](https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/)
- [A Guide to the Kubernetes Networking Model](https://sookocheff.com/post/kubernetes/understanding-kubernetes-networking-model/)

### 7.2 实验：发布服务

- Cluster IP
- Service FQDN
- Nodeport
- LB Type Service

```bash
# Taint slave 节点，因为在有些环境中没有放开隧道防火墙，我们强制让 pod 都跑在 master 上
kubectl taint node ckaslave001 key=value:NoExecute

# 创建 Deployment
kubectl apply -f https://raw.githubusercontent.com/kubernetes/website/master/content/en/examples/service/networking/run-my-nginx.yaml
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  selector:
    matchLabels:
      run: my-nginx
  replicas: 2
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: nginx
        ports:
        - containerPort: 80
```

```bash
# 创建 Service
kubectl apply -f https://raw.githubusercontent.com/kubernetes/website/master/content/en/examples/service/networking/nginx-svc.yaml
```

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-nginx
  labels:
    run: my-nginx
spec:
  ports:
  - port: 80
    protocol: TCP
  selector:
    run: my-nginx
```

```console
root@ckamaster001:~# kubectl get svc --all-namespaces -o wide
NAMESPACE     NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                  AGE   SELECTOR
default       kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP                  8h    <none>
default       my-nginx     ClusterIP   10.98.172.84   <none>        80/TCP                   36m   run=my-nginx
kube-system   kube-dns     ClusterIP   10.96.0.10     <none>        53/UDP,53/TCP,9153/TCP   8h    k8s-app=kube-dns

root@ckamaster001:~# dig @10.96.0.10 my-nginx.default.svc.cluster.local

; <<>> DiG 9.11.3-1ubuntu1.12-Ubuntu <<>> @10.96.0.10 my-nginx.default.svc.cluster.local
; (1 server found)
;; global options: +cmd
;; Got answer:
;; WARNING: .local is reserved for Multicast DNS
;; You are currently testing what happens when an mDNS query is leaked to DNS
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 23475
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
; COOKIE: 2661e0af4b0ce87e (echoed)
;; QUESTION SECTION:
;my-nginx.default.svc.cluster.local. IN	A

;; ANSWER SECTION:
my-nginx.default.svc.cluster.local. 30 IN A	10.98.172.84

;; Query time: 0 msec
;; SERVER: 10.96.0.10#53(10.96.0.10)
;; WHEN: Sat Jun 13 16:15:23 CST 2020
;; MSG SIZE  rcvd: 125
```

### 7.3 什么是 Ingress？

- [Ingress Controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)
  - [安装 Nginx Ingress Controller](https://kubernetes.github.io/ingress-nginx/deploy/#bare-metal)

    ```bash
    # 下载 ingress controller 的 yaml 文件
    # wget https://raw.githubusercontent.com/kubernetes/ingress-nginx/nginx-0.30.0/deploy/static/mandatory.yaml
    wget https://gitee.com/dev-99cloud/training-kubernetes/raw/master/src/amd-lab/mandatory.yaml
    ```

    新版本默认不监听80、443端口，需自行进行配置

    ```bash
    # 查看端口是否被占用
    lsof -i :xxx
    # 修改 mandatory.yaml 文件，在 spec.template.spec 处添加如下语句可监听本地端口
    hostNetwork: true
    # 一般443会被 calico 占用，80端口不会被占用，可将文件下方 ports 处关于443的注释掉, controller 不会再监听443端口

    # 安装 ingress controller
    kubectl apply -f mandatory.yaml
    # 查看
    kubectl get pods -n ingress-nginx
    ```
- [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)

  - 部署后端服务

    ```console
    [root@iZuf6g226c4titrnrwds2tZ ~]# vim deploy-demo.yaml
    ```
    ``` yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: myapp
      namespace: default
    spec:
      selector:
        app: myapp
        release: canary
      ports:
      - name: http
        targetPort: 80
        port: 80
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: myapp-backend-pod
      namespace: default
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: myapp
          release: canary
      template:
        metadata:
          labels:
            app: myapp
            release: canary
        spec:
          containers:
          - name: myapp
            image: ikubernetes/myapp:v2
            ports:
            - name: http
              containerPort: 80
    ```

    ```console
    [root@iZuf6g226c4titrnrwds2tZ ~]# kubectl apply -f deploy-demo.yaml
    [root@iZuf6g226c4titrnrwds2tZ ~]# kubectl get pods
    NAME                                 READY   STATUS    RESTARTS   AGE
    myapp-backend-pod-58b7f5cf77-krmzh   1/1     Running   2          17h
    myapp-backend-pod-58b7f5cf77-vqlgl   1/1     Running   2          17h
    myapp-backend-pod-58b7f5cf77-z7j7z   1/1     Running   2          17h
    ```

  - 通过 ingress-controller 对外提供服务，还要为其建立一个 service

    ```bash
    #下载 yaml 文件
    wget https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/provider/baremetal/service-nodeport.yaml
    vim service-nodeport.yaml
    ```

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: ingress-nginx
      namespace: ingress-nginx
      labels:
        app.kubernetes.io/name: ingress-nginx
        app.kubernetes.io/part-of: ingress-nginx
    spec:
      type: NodePort
      ports:
        - name: http
          port: 80
          targetPort: 80
          protocol: TCP
          nodePort: 30080
        - name: https
          port: 443
          targetPort: 443
          protocol: TCP
          nodePort: 30443
      selector:
        app.kubernetes.io/name: ingress-nginx
        app.kubernetes.io/part-of: ingress-nginx

    ---
    ```

    ```console
    [root@iZuf6g226c4titrnrwds2tZ ~]# kubectl apply -f service-nodeport.yaml
    [root@iZuf6g226c4titrnrwds2tZ ~]# kubectl get svc -n ingress-nginx
    NAME            TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
    ingress-nginx   NodePort   10.105.153.191   <none>        80:30080/TCP,443:30443/TCP   9h
    ```

  - 部署 Ingress

    ```console
    [root@iZuf6g226c4titrnrwds2tZ ~]# vim ingress-myapp.yaml
    ```
    ```yaml
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: ingress-myapp
      namespace: default
      annotations:
        kubernetes.io/ingress.class: "nginx"
    spec:
      rules:
      - host: myapp.test.com
        http:
          paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: myapp
                port:
                  number: 80
    ```
    ```console
    [root@iZuf6g226c4titrnrwds2tZ ~]# kubectl apply -f ingress-myapp.yaml
    [root@iZuf6g226c4titrnrwds2tZ ~]# kubectl get ingress
    NAME            CLASS    HOSTS            ADDRESS          PORTS   AGE
    ingress-myapp   <none>   myapp.test.com   10.105.153.191   80      17h
    ```

  - 结果测试

    ```bash
    # 修改本地 host 文件
    sudo vi /etc/hosts
    # 添加
    xxx.xxx.xxx.xxx myapp.test.com
    # 终端访问
    curl http://myapp.test.com
    # 结果
    Hello MyApp | Version: v2 | <a href="hostname.html">Pod Name</a>
    # 在外部访问时可能出现网站未备案的问题，多次尝试即可
    # 在内部也需配置 hosts 通过域名进行访问
    ```

  - k8s.gcr.io 网络问题导致镜像 pull 失败
    - 将 yaml 文件下载到本地
    - 在 docker hub 上搜索对应的images
    - 将文件内对应的 image 修改为 docker hub 上搜索到的对应 image ，如：

      ```console
      #image: k8s.gcr.io/ingress-nginx/controller:v0.47.  0@sha256:52f0058bed0a17ab0fb35628ba97e8d52b5d32299fbc03cc0f6c7b9ff036b61a
      image: willdockerhub/ingress-nginx-controller:v0.47.0
      ```

    - kubectl apply -f xxx `

## Lesson 08：Advance

### 8.1 监控、日志、排错

- 监控：Grafana / Prometheus / AlertManager
- 日志：ElasticSearch / Fluent ( Logstash ) / Kibana
- 排错：
    - 怎么对 pod 的网口抓包？

        ```bash
        # 查看指定 pod 运行在那个 node 上
        kubectl describe pod <pod> -n <namespace>

        # 获得容器的 pid
        docker inspect -f {{.State.Pid}} <container>

        # 进入该容器的 network namespace
        nsenter --target <PID> -n

        # 使用 tcpdump 抓包，指定 eth0 网卡
        tcpdump -i eth0 tcp and port 80 -vvv

        # 或者抓包并导出到文件
        tcpdump -i eth0 -w ./out.cap

        # 退出 nsenter，要记得退出！！
        exit
        ```

    - Debug tools

        ```bash
        apiVersion: v1
        kind: Pod
        metadata:
          name: demo-pod
          labels:
            app: demo-pod
        spec:
          containers:
            - name: nginx
              image: nginx
              ports:
                - containerPort: 80
              env:
                - name: DEMO_GREETING
                  value: "Hello from the environment"
                - name: DEMO_FAREWELL
                  value: "Such a sweet sorrow"
            - name: busybox
              image: busybox
              args:
                - sleep
                - "1000000"
        ```

        ```console
        root@ckatest001:~# kubectl exec -it demo-pod -c busybox -- /bin/sh
        / # ping 192.168.209.193
        PING 192.168.209.193 (192.168.209.193): 56 data bytes
        64 bytes from 192.168.209.193: seq=0 ttl=63 time=0.099 ms
        64 bytes from 192.168.209.193: seq=1 ttl=63 time=0.093 ms
        64 bytes from 192.168.209.193: seq=2 ttl=63 time=0.089 ms
        ```

        ```console
        root@ckalab001:~# tcpdump -i eth0 udp
        12:34:10.972395 IP 45.77.183.254.vultr.com.42125 > 45.32.33.135.vultr.com.4789: VXLAN, flags [I] (0x08), vni 4096
        IP 192.168.208.4 > 192.168.209.193: ICMP echo request, id 3072, seq 0, length 64
        12:34:10.972753 IP 45.32.33.135.vultr.com.41062 > 45.77.183.254.vultr.com.4789: VXLAN, flags [I] (0x08), vni 4096
        IP 192.168.209.193 > 192.168.208.4: ICMP echo reply, id 3072, seq 0, length 64
        12:34:11.972537 IP 45.77.183.254.vultr.com.42125 > 45.32.33.135.vultr.com.4789: VXLAN, flags [I] (0x08), vni 4096
        IP 192.168.208.4 > 192.168.209.193: ICMP echo request, id 3072, seq 1, length 64
        ```

        在阿里云上比较特别，阿里云把 calico / flannel 的 vxlan 魔改成路由协议了，因此需要在 VPC 上加路由才行，每个节点一条路由协议。该节点的 pod 网段都发给该节点的 node ip。[这篇 KB](https://yq.aliyun.com/articles/704175) 非常含糊其辞，翻译一下就是不支持 vxlan，魔改 vxlan，底层用路由协议实现，所以需要在 VPC 上加路由。

        正常的 vxlan，
        ```console
        root@ckalab001:~# ip r
        default via 45.77.182.1 dev ens3 proto dhcp src 45.77.183.254 metric 100
        192.168.208.1 dev cali65a032ad3e5 scope link
        192.168.209.192/26 via 192.168.209.192 dev vxlan.calico onlink

        root@ckalab001:~# ip a
        2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
            link/ether 56:00:02:d8:35:5a brd ff:ff:ff:ff:ff:ff
            inet 45.77.183.254/23 brd 45.77.183.255 scope global dynamic ens3
              valid_lft 73639sec preferred_lft 73639sec
            inet6 fe80::5400:2ff:fed8:355a/64 scope link
              valid_lft forever preferred_lft forever
        4: cali65a032ad3e5@if3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1410 qdisc noqueue state UP group default
            link/ether ee:ee:ee:ee:ee:ee brd ff:ff:ff:ff:ff:ff link-netnsid 0
            inet6 fe80::ecee:eeff:feee:eeee/64 scope link
              valid_lft forever preferred_lft forever
        9: vxlan.calico: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1410 qdisc noqueue state UNKNOWN group default
            link/ether 66:f1:80:3e:ea:c6 brd ff:ff:ff:ff:ff:ff
            inet 192.168.208.0/32 brd 192.168.208.0 scope global vxlan.calico
              valid_lft forever preferred_lft forever
            inet6 fe80::64f1:80ff:fe3e:eac6/64 scope link
              valid_lft forever preferred_lft forever
        ```

        阿里云魔改的 vxlan：`192.168.209.192/26 via 172.31.43.146 dev eth0 proto 80 onlink`，80 是 IGRP 网关间路由协议。所以跨 node 的 pod 间发 ping 包时，tcpdump 抓 tcp 包抓不到，抓 icmp 包可以抓到。

        ```console
        root@ckalab001:~# ip r
        default via 172.31.47.253 dev eth0 proto dhcp src 172.31.43.145 metric 100
        192.168.208.1 dev cali77bffbebec8 scope link
        192.168.209.192/26 via 172.31.43.146 dev eth0 proto 80 onlink

        root@ckalab001:~# ip a
        2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
            link/ether 00:16:3e:08:2e:5f brd ff:ff:ff:ff:ff:ff
            inet 172.31.43.145/20 brd 172.31.47.255 scope global dynamic eth0
              valid_lft 315356000sec preferred_lft 315356000sec
            inet6 fe80::216:3eff:fe08:2e5f/64 scope link
              valid_lft forever preferred_lft forever
        4: cali77bffbebec8@if3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1410 qdisc noqueue state UP group default
            link/ether ee:ee:ee:ee:ee:ee brd ff:ff:ff:ff:ff:ff link-netnsid 0
            inet6 fe80::ecee:eeff:feee:eeee/64 scope link
              valid_lft forever preferred_lft forever
        8: vxlan.calico: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1410 qdisc noqueue state UNKNOWN group default
            link/ether 66:f1:80:3e:ea:c6 brd ff:ff:ff:ff:ff:ff
            inet 192.168.208.0/32 brd 192.168.208.0 scope global vxlan.calico
              valid_lft forever preferred_lft forever
            inet6 fe80::64f1:80ff:fe3e:eac6/64 scope link
              valid_lft forever preferred_lft forever
        ```

### 8.2 什么是 HPA / CA / VA？

- 怎么理解 HPA / CA / VPA？
- 配置 metrics server

  ```bash
  mkdir metrics
  cd metrics
  # 在 github 对应仓库中下载全部 yaml 文件
  # for file in auth-delegator.yaml auth-reader.yaml metrics-apiservice.yaml metrics-server-deployment.yaml metrics-server-service.yaml resource-reader.yaml ; do wget https://raw.githubusercontent.com/kubernetes/kubernetes/master/cluster/addons/metrics-server/$file;done
  # 最新版本可能会出现无法通过健康检查的问题，可以根据自己的 kubernetes 版本，选择相同的 metrics server 版本
  # v1.20.1 版本国内仓库下载
  for file in auth-delegator.yaml auth-reader.yaml metrics-apiservice.yaml metrics-server-deployment.yaml metrics-server-service.yaml resource-reader.yaml ; do wget https://gitee.com/dev-99cloud/training-kubernetes/raw/master/src/amd-lab/metrics-server/$file;done
  kubectl apply -f .
  ```

  修改 metrics-server-deployment.yaml

  ```yaml
  apiVersion: v1
  kind: ServiceAccount
  metadata:
    name: metrics-server
    namespace: kube-system
    labels:
      kubernetes.io/cluster-service: "true"
      addonmanager.kubernetes.io/mode: Reconcile
  ---
  apiVersion: v1
  kind: ConfigMap
  metadata:
    name: metrics-server-config
    namespace: kube-system
    labels:
      kubernetes.io/cluster-service: "true"
      addonmanager.kubernetes.io/mode: EnsureExists
  data:
    NannyConfiguration: |-
      apiVersion: nannyconfig/v1alpha1
      kind: NannyConfiguration
  ---
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: metrics-server-v0.3.6
    namespace: kube-system
    labels:
      k8s-app: metrics-server
      kubernetes.io/cluster-service: "true"
      addonmanager.kubernetes.io/mode: Reconcile
      version: v0.3.6
  spec:
    selector:
      matchLabels:
        k8s-app: metrics-server
        version: v0.3.6
    template:
      metadata:
        name: metrics-server
        labels:
          k8s-app: metrics-server
          version: v0.3.6
      spec:
        securityContext:
          seccompProfile:
            type: RuntimeDefault
        priorityClassName: system-cluster-critical
        serviceAccountName: metrics-server
        nodeSelector:
          kubernetes.io/os: linux
        containers:
        - name: metrics-server
          # image: k8s.gcr.io/metrics-server-amd64:v0.3.6
          image: opsdockerimage/metrics-server-amd64:v0.3.6
          command:
          - /metrics-server
          - --metric-resolution=30s
          # These are needed for GKE, which doesn't support secure communication yet.
          # Remove these lines for non-GKE clusters, and when GKE supports token-based auth.
          # - --kubelet-port=10255
          # - --deprecated-kubelet-completely-insecure=true
          - --kubelet-insecure-tls
          - --kubelet-preferred-address-types=InternalIP
          # - --kubelet-preferred-address-types=InternalIP,Hostname,InternalDNS,ExternalDNS,ExternalIP
          ports:
          - containerPort: 443
            name: https
            protocol: TCP
        - name: metrics-server-nanny
          # image: k8s.gcr.io/addon-resizer:1.8.11
          image: opsdockerimage/addon-resizer:1.8.11
          resources:
            limits:
              cpu: 100m
              memory: 300Mi
            requests:
              cpu: 5m
              memory: 50Mi
          env:
            - name: MY_POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: MY_POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
          volumeMounts:
          - name: metrics-server-config-volume
            mountPath: /etc/config
          command:
            - /pod_nanny
            - --config-dir=/etc/config
            # - --cpu={{ base_metrics_server_cpu }}
            - --extra-cpu=0.5m
            # - --memory={{ base_metrics_server_memory }}
            # - --extra-memory={{ metrics_server_memory_per_node }}Mi
            - --threshold=5
            - --deployment=metrics-server-v0.3.6
            - --container=metrics-server
            - --poll-period=300000
            - --estimator=exponential
            # Specifies the smallest cluster (defined in number of nodes)
            # resources will be scaled to.
            # - --minClusterSize={{ metrics_server_min_cluster_size }}
            - --minClusterSize=2
            # Use kube-apiserver metrics to avoid periodically listing nodes.
            - --use-metrics=true
        volumes:
          - name: metrics-server-config-volume
            configMap:
              name: metrics-server-config
        tolerations:
          - key: "CriticalAddonsOnly"
            operator: "Exists"
  ```

  修改 resource-reader.yaml

  ```yaml
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRole
  metadata:
    name: system:metrics-server
    labels:
      kubernetes.io/cluster-service: "true"
      addonmanager.kubernetes.io/mode: Reconcile
  rules:
  - apiGroups:
    - ""
    resources:
    - pods
    - nodes
    # 添加 nodes/stats
    - nodes/stats
    - namespaces
    verbs:
    - get
    - list
    - watch
  - apiGroups:
    - "apps"
    resources:
    - deployments
    verbs:
    - get
    - list
    - update
    - watch
  - nonResourceURLs:
    - /metrics
    verbs:
    - get
  ---
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRoleBinding
  metadata:
    name: system:metrics-server
    labels:
      kubernetes.io/cluster-service: "true"
      addonmanager.kubernetes.io/mode: Reconcile
  roleRef:
    apiGroup: rbac.authorization.k8s.io
    kind: ClusterRole
    name: system:metrics-server
  subjects:
  - kind: ServiceAccount
    name: metrics-server
    namespace: kube-system
  ```

- 检查 metrics 是否可用

  ```bash
  # 查看 pod 是否正常运行
  kubectl get pods -n kube-system
  # 查看 api-versions ，正常情况下应当多出 metrics.k8s.io/v1beta1
  kubectl api-versions
  # 查看 node 监控指标
  kubectl top nodes
  NAME                      CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
  izuf6g226c4titrnrwds2tz   129m         6%     1500Mi          42%
  # 查看 pod 监控指标
  kubectl top pods
  NAME                                 CPU(cores)   MEMORY(bytes)
  myapp-backend-pod-58b7f5cf77-krmzh   0m           1Mi
  myapp-backend-pod-58b7f5cf77-vqlgl   0m           1Mi
  myapp-backend-pod-58b7f5cf77-z7j7z   0m           1Mi
  ```

  - 如果 metrics 不可用，报错 unable to fully collect metrics: unable to fully scrape metrics from source kubelet_summary ，可以尝试修改证书

    ```bash
    mkdir certs; cd certs
    cp /etc/kubernetes/pki/ca.crt ca.pem
    cp /etc/kubernetes/pki/ca.key ca-key.pem
    ```

    创建文件 kubelet-csr.json

    ```json
    {
      "CN": "kubernetes",
      "hosts": [
        "127.0.0.1",
        "<node_name>",
        "kubernetes",
        "kubernetes.default",
        "kubernetes.default.svc",
        "kubernetes.default.svc.cluster",
        "kubernetes.default.svc.cluster.local"
      ],
      "key": {
        "algo": "rsa",
        "size": 2048
      },
      "names": [{
        "C": "US",
        "ST": "NY",
        "L": "City",
        "O": "Org",
        "OU": "Unit"
      }]
    }
    ```

    创建文件 ca-config.json

    ```json
    {
      "signing": {
        "default": {
          "expiry": "8760h"
        },
        "profiles": {
          "kubernetes": {
            "usages": [
              "signing",
              "key encipherment",
              "server auth",
              "client auth"
            ],
            "expiry": "8760h"
          }
        }
      }
    }
    ```

    更新证书

    ```bash
    cfssl gencert -ca=ca.pem -ca-key=ca-key.pem --config=ca-config.json -profile=kubernetes kubelet-csr.json | cfssljson -bare kubelet
    scp kubelet.pem <nodeip>:/var/lib/kubelet/pki/kubelet.crt
    scp kubelet-key.pem <nodeip>:/var/lib/kubelet/pki/kubelet.key
    systemctl restart kubelet
    ```

- 定制 docker 镜像

  ```console
  FROM php:5-apache
  COPY index.php /var/www/html/index.php
  RUN chmod a+rx index.php
  ```

  index.php 文件内容如下：

  ```php
  <?php
    $x = 0.0001;
    for ($i = 0; $i <= 1000000; $i++) {
        $x += sqrt($x);
    }
  ?>
  ```

- 配置 Deployment 运行镜像并暴露服务

  php-apache.yaml:

  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: php-apache
  spec:
    selector:
      matchLabels:
        run: php-apache
    replicas: 1
    template:
      metadata:
        labels:
          run: php-apache
      spec:
        containers:
        - name: php-apache
          #image: k8s.gcr.io/hpa-example
          image: 0layfolk0/hpa-example
          ports:
          - containerPort: 80
          resources:
            limits:
              cpu: 50m
            requests:
              cpu: 20m

  ---

  apiVersion: v1
  kind: Service
  metadata:
    name: php-apache
    labels:
      run: php-apache
  spec:
    ports:
    - port: 80
    selector:
      run: php-apache
  ```

- 创建 HPA

  ```bash
  # 实验过程中副本、 CPU 负载等变化需要一定的时间，不会即时改变，一般耗时几分钟
  # 创建一个 HPA 控制上一步骤中的 Deployment ，使副本数量维持在1-10之间，平均 CPU 利用率50%
  kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10
  horizontalpodautoscaler.autoscaling/php-apache autoscaled
  # 查看Autoscaler状态
  kubectl get hpa
  # 在新终端中启动容器，增加负载
  kubectl run -i --tty load-generator --rm --image=busybox --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"
  # 回到旧终端
  # 查看 CPU 负载情况，升高
  kubectl get hpa
  # 查看 deployment 的副本数量，增多
  kubectl get deployment php-apache
  # 新终端ctrl+C终止容器运行，旧终端检查负载状态， CPU 利用率应当降为0，副本数量变为1
  kubectl get hpa
  kubectl get deployment php-apache
  ```

### 8.3 什么是 Federation？

- Kubenetes Federation vs ManageIQ

### 8.4 K8S 怎么处理有状态服务？

- [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [StatefulSet Examples](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/)
- CRD & Operator

### 8.5 其它参考

- [K8S 测试](https://jimmysong.io/kubernetes-handbook/develop/testing.html)
- 搭建 OpenStack 测试环境
  - [vultr](https://www.vultr.com/) 开 Ubuntu 18.04 / 20.4 Bare Metal 服务器
  - [安装 DevStack](https://docs.openstack.org/devstack/latest/)
  - [下载云镜像](https://docs.openstack.org/image-guide/obtain-images.html)

      ```bash
      wget http://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud-2009.qcow2
      wget https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64.img
      wget https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64.img
      ```

  - [上传云镜像](https://docs.openstack.org/murano/pike/reference/appendix/articles/image_builders/upload.html)

      ```bash
      openstack image create --public --disk-format qcow2 --file focal-server-cloudimg-amd64.img ubuntu-20.04
      openstack image create --public --disk-format qcow2 --file bionic-server-cloudimg-amd64.img ubuntu-18.04
      openstack image create --public --disk-format qcow2 --file CentOS-7-x86_64-GenericCloud-2009.qcow2 centos-7.8
      ```

  - [启用 ipip](https://www.infoq.cn/article/mqluyhvsdw8xopdwp17v)
- [k3s 环境搭建](https://github.com/k3s-io/k3s#quick-start---install-script)
- [KubeEdge Demo](https://kubeedge.io/zh/blog/kubeedge-deployment-manual/)

##	Lesson 09：CKA

### 9.1 考试注意事项

### 9.2 模拟题讲解

### 9.3 实验：做模拟题

## Lesson 10: FAQ

1. 什么是配置 egress ip？[红帽方案](https://docs.openshift.com/container-platform/4.1/networking/openshift_sdn/assigning-egress-ips.html)，[开源方案](https://github.com/nirmata/kube-static-egress-ip)
