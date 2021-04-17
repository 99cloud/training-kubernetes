# 1. 实验环境拓扑：

客户端 ---> 阿里云上海跳板机 ---> Azure东亚跳板机 ---> 阿里云香港实验环境

```bash
ssh root@106.15.4.212
ssh apple@13.70.46.16
ssh root@cka0XX-ip
```

# 2. 免密码登陆步骤

1. 配置翻墙碉堡机

    ```
    Host cka-bastion
        HostName        106.15.4.212
        User            root

    Host cka-fq
        HostName        13.70.46.16
        User            apple
        ProxyCommand    ssh cka-bastion -W %h:%p
    ```

1. 阿里云导出 Name、公网 IP、内网 IP 等 3 列，复制到 ckalab.txt
1. 生成 .ssh/config 文件配置：`python gen-ssh-config.py`
1. 配置密钥：`cat ckalab.txt | awk '{print $1}' | xargs -I{} ssh-copy-id -i ~/.ssh/id_rsa_lab.pub {}`
1. 配置 bastion ssh：

    ```
    Host cka-master001
        HostName        47.242.70.202
        User            root
        IdentityFile    ~/.ssh/id_rsa_lab
        ProxyCommand    ssh cka-fq -W %h:%p
    ```

1. 配置 cka 机器 ssh 选项（避免频繁断开和连接慢问题）：`ansible-playbook -i hosts config-01-lab.yml`
1. 配置好之后，就可以直接：`ssh cka-master001`

# 3. 集成 NFS 存储

## 3.1 搭建 NFS Server

1. 准备好 NFS server 机器（另开一台 CentOS 7.9，单独配一块数据盘），机器规格按需指定。最好挂载一块单独的磁盘。
1. 保证需要使用 NFS 存储的客户端机器与 NFS server 机器的网络互通性
1. 部署步骤
    1. 下载相关包，并启动相关服务

        ```bash
        yum install nfs-utils -y
        ```

    1. 创建 NFS 数据路径

        ```bash
        mkdir -p /nfs/data
        chmod -R 777 /nfs/data
        ```

    1. 格式化磁盘并挂载（建议添加一块磁盘作为 NFS 数据盘），比如 vdb

        ```bash
        mkfs.xfs /dev/vdb
        mount /dev/vdb /nfs/data
        echo "/dev/vdb /nfs/data xfs defaults 0 0" >> /etc/fstab
        ```

    1. 编辑 NFS 配置文件

        ```bash
        # echo "/nfs/data *(rw,no_root_squash,sync)" > /etc/exports
        echo "/nfs/data *(rw,sync,no_subtree_check,no_root_squash,no_all_squash,insecure)" > /etc/exports
        # 首次登入Internal error occurred: account is not active 的问题，https://kubesphere.com.cn/forum/d/2058-kk-internal-error-occurred-account-is-not-active
        exportfs -r
        ```

    1. 启动 rpcbind、nfs 服务

        ```bash
        systemctl restart rpcbind && systemctl enable rpcbind
        systemctl restart nfs && systemctl enable nfs
        ```

    1. 查看 RPC 服务的注册状况

        ```bash
        rpcinfo -p localhost
        program vers proto   port  service
            ...
            100003    3   tcp   2049  nfs
            100003    4   tcp   2049  nfs
            100227    3   tcp   2049  nfs_acl
            100003    3   udp   2049  nfs
            100003    4   udp   2049  nfs
            100227    3   udp   2049  nfs_acl
            ...
        ```

## 3.2 使用动态 PersistentVolume

1. 创建 RBAC.yaml 文件，内容如下。

    ```yaml
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: nfs-client-provisioner
      # replace with namespace where provisioner is deployed
      namespace: default
    ---
    kind: ClusterRole
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: nfs-client-provisioner-runner
    rules:
      - apiGroups: [""]
        resources: ["persistentvolumes"]
        verbs: ["get", "list", "watch", "create", "delete"]
      - apiGroups: [""]
        resources: ["persistentvolumeclaims"]
        verbs: ["get", "list", "watch", "update"]
      - apiGroups: ["storage.k8s.io"]
        resources: ["storageclasses"]
        verbs: ["get", "list", "watch"]
      - apiGroups: [""]
        resources: ["events"]
        verbs: ["create", "update", "patch"]
    ---
    kind: ClusterRoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: run-nfs-client-provisioner
    subjects:
      - kind: ServiceAccount
        name: nfs-client-provisioner
        # replace with namespace where provisioner is deployed
        namespace: default
    roleRef:
      kind: ClusterRole
      name: nfs-client-provisioner-runner
      apiGroup: rbac.authorization.k8s.io
    ---
    kind: Role
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: leader-locking-nfs-client-provisioner
      # replace with namespace where provisioner is deployed
      namespace: default
    rules:
      - apiGroups: [""]
        resources: ["endpoints"]
        verbs: ["get", "list", "watch", "create", "update",     "patch"]
    ---
    kind: RoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: leader-locking-nfs-client-provisioner
      # replace with namespace where provisioner is deployed
      namespace: default
    subjects:
      - kind: ServiceAccount
        name: nfs-client-provisioner
        # replace with namespace where provisioner is deployed
        namespace: default
    roleRef:
      kind: Role
      name: leader-locking-nfs-client-provisioner
      apiGroup: rbac.authorization.k8s.io
    ```

1. 执行命令创建 RBAC

    ```bash
    kubectl create -f RBAC.yaml
    ```

1. 创建 deployment.yaml 文件，内容如下:

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nfs-client-provisioner
      labels:
        app: nfs-client-provisioner
      namespace: default
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: nfs-client-provisioner
      strategy:
        type: Recreate
      selector:
        matchLabels:
          app: nfs-client-provisioner
      template:
        metadata:
          labels:
            app: nfs-client-provisioner
        spec:
          serviceAccountName: nfs-client-provisioner
          containers:
            - name: nfs-client-provisioner
              image: quay.io/external_storage/nfs-client-provisioner:latest
              volumeMounts:
                - name: nfs-client-root
                  mountPath: /persistentvolumes
              env:
                - name: PROVISIONER_NAME
                  value: fuseim.pri/ifs
                - name: NFS_SERVER
                  value: ${NODE_IP}
                - name: NFS_PATH
                  value: /nfs/data
          volumes:
            - name: nfs-client-root
              nfs:
                server: ${NODE_IP}
                path: /nfs/data
    ```

    > 其中 ${NODE_IP} 请替换成 NFS Server 的地址

    如果 driver 起不来，多半是 client 端没有安装 nfs-common(ubuntu) 或者 nfs-utils(centos)

1. 部署deploy

    ```bash
    kubectl create -f deployment.yaml
    ```

1. 创建 storageclass.yaml 文件

    ```yaml
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: nfs
    provisioner: fuseim.pri/ifs
    parameters:
      archiveOnDelete: "false"
    reclaimPolicy: Delete
    ```

    > provisioner 要对应 驱动所传入的环境变量 PROVISIONER_NAME 的值。

1. 创建 storage class

    ```bash
    kubectl apply -f storageclass.yaml
    ```

1. 如果要把 nfs 设置成默认 StorageClass：(option)

    ```
    kubectl patch storageclass nfs -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class":"true"}}}'
    ```

## 3.3 测试

1. 创建 pvc.yaml 文件

    ```yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: test-pvc
      annotations:
        volume.beta.kubernetes.io/storage-class: "nfs"
    spec:
      accessModes:
        - ReadWriteMany
      resources:
        requests:
          storage: 1Gi
    ```

1. 创建 pvc

    ```bash
    kubectl apply -f pvc.yaml
    ```

    此时可以看一下 pvc 状态，应该是 Bound，如果是 pending，看一下 nfs driver pod 的 log。K8S 1.20 以后，会有这个报错：`unexpected error getting claim reference: selfLink was empty, can't make reference`，有两个办法，参考：<https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner/issues/25>，在 api-server 的 static pod 里添加启动参数：`--feature-gates=RemoveSelfLink=false`，或者更新 NFS 驱动镜像：`gcr.io/k8s-staging-sig-storage/nfs-subdir-external-provisioner:v4.0.0`

2. 测试

    ```yaml
    kind: Pod
    apiVersion: v1
    metadata:
      name: test-pod
    spec:
      containers:
      - name: test-pod
        image: gcr.io/google_containers/busybox:1.24
        command:
          - "/bin/sh"
        args:
          - "-c"
          - "touch /mnt/SUCCESS && exit 0 || exit 1"
        volumeMounts:
          - name: nfs-pvc
            mountPath: "/mnt"
      restartPolicy: "Never"
      volumes:
        - name: nfs-pvc
          persistentVolumeClaim:
            claimName: test-pvc
    ```

    > 其中 gcr.io/google_containers/busybox:1.24 换成任意的镜像即可。

# 4 安装 KubeSphere

## 4.1 安装步骤

参考 <https://kubesphere.io/docs/quick-start/minimal-kubesphere-on-k8s/>

```bash
kubectl apply -f https://github.com/kubesphere/ks-installer/releases/download/v3.0.0/kubesphere-installer.yaml   
kubectl apply -f https://github.com/kubesphere/ks-installer/releases/download/v3.0.0/cluster-configuration.yaml
```

## 4.2 Inspect the logs of installation

```
kubectl logs -n kubesphere-system $(kubectl get pod -n kubesphere-system -l app=ks-install -o jsonpath='{.items[0].metadata.name}') -f

kubectl get pods --all-namespaces
kubectl get svc/ks-console -n kubesphere-system
```

## 4.3 访问 Dashboard

访问 `http://<K8S-NODE-IP>:30880/`，默认用户密码：`admin / P@88w0rd`

如果登陆不了，可以看下是不是 K8S 版本太高了。<https://kubesphere.com.cn/forum/d/2217-account-is-not-active>
安装特定版本的 K8S，参考：<https://stackoverflow.com/questions/49721708/how-to-install-specific-version-of-kubernetes>

```bash
curl -s https://packages.cloud.google.com/apt/dists/kubernetes-xenial/main/binary-amd64/Packages | grep Version | awk '{print $2}'
sudo apt-get install -qy kubelet=1.9.6-00 kubectl=1.9.6-00 kubeadm=1.9.6-00
```

## 4.4 清除 KubeSphere

```bash
kubectl delete ns kubesphere-monitoring-system kubesphere-controls-system kubesphere-system
```
