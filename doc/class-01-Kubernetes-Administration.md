# Kubernetes-Administration

## 1. Prefix

- 授课时长：
    - 上午：9:30 至 12:00
    - 下午：13:30 至 16:00
- Prerequisite
    - vim 基础操作 -- 编辑、修改、保存文件
    - 网络基础知识 -- 网段 cidr、vlan、vxlan、配置 linux 网卡等等
    - 基础的 linux 知识 -- 权限、文件系统、服务
    - systemd 的基础操作 -- 重启、关闭、启动、重载、查看 systemd 的服务

## 2. Catalog

| Date | Time | Title | Content |
| ---- | ---- | ----- | ------- |
| 第 1 天 | 上午 | [1. Linux 容器和 Docker](#lesson-01lxc--docker) | [1.1 什么是 Linux 容器？]() |
| | | | [1.2 容器和虚拟机有何区别？]() |
| | | | [1.3 Docker 和容器技术有什么关系？]() |
| | | | [1.4 Docker 的架构和概念空间是怎样的？]() |
| | | | [1.5 什么是所谓的安全容器技术？]() |
| | | | [1.6 实验：Docker Quick Start]() |
| | 下午 | | [1.7 Docker 的网络模型]() |
| | | | [1.8 Docker 的存储模型]() |
| | | [2. Kubernetes 的基本概念](#lesson-02kubernetes-concepts) | [2.1 什么是 K8S？]() |
| | | | [2.2 K8S 是为了解决什么问题？]()快速缩放 / 自愈 |
| | | | [2.3 K8S 不解决什么问题？]()用户管理/限流熔断/监控审计 |
| | | | [2.4 K8S 的模块架构是怎样的？]() |
| | | | [2.5 K8S 有哪些竞争产品？]()OpenShift/VMware/KubeSphere|
| | | | [产品会基于 K8S 做哪些改良？]() 界面/中间件/云支持 |
| | | | [怎么部署出一个 K8S 群集？]() kubeadm |
| | | | [实验：K8S 的部署]() |
| | | | [什么是 Pod？]()为什么调度的基本单位是 pod 不是容器？ |
| | | | [实验：启动一个 pod ]() |
| 第 2 天 | 上午 | | [什么是 YAML？]() |
| | | | [什么是 Namespace & Quota？]() |
| | | | [什么是 Deployment & ReplicaSet？]() |
| | | | [什么是 Services？]() |
| | | | [实验：K8S Dashboard]() |
| | | | [实验：K8S 对象管理操作]()：Deployment/Service/Label |
| | | | [实验：K8S 怎么发布服务和扩缩容？]() |
| | | | [DeamonSet & SetfulSet]() |
| | 下午 | [3. K8S 的模块解析](#lesson-03k8s-arch--ha) | [Kubernetes 的模块解析]() |
| | | | [实验：ETCD 操作]() |
| | | | [什么是静态 Pod？]() |
| | | | [怎么部署一个 HA 的 K8S 群集？]() |
| | | [4. K8S 的认证和安全](#lesson-04k8s-auth--security) | [什么是 K8S 的 3A？]()认证、 / 鉴权 / 准入 |
| | | | [怎么配置 kubectl？]() |
| | | | [K8S 怎么保证网络安全？]() |
| | | | [什么是用户和角色？]() |
| | | | [实验：添加用户 & 绑定角色]() |
| 第 3 天 | 上午 | [5. K8S 的调度](#lesson-05-k8s-schedule) | [什么是 Labels？]() |
| | | | [什么是 Taints & Toleration？]()污染标签 & 容忍标签 |
| | | | [什么是 Node Affinity？]()节点亲和 / 反亲和 |
| | | | [什么是 Pod Affinity？]()Pod 的亲和 / 反亲和 |
| | | | [实验：Pod 调度]() |
| | 下午 | [6. K8S 的数据持久化](#lesson-06-k8s-storage) | [什么是 ConfigMap & Secret ？]() |
| | | | [什么是 PV / PVC？]() |
| | | | [什么是 Storage Class？]() |
| | | | [实验：ConfigMap / Secret / PV & PVC / StorageClass]() |
| | | [7. 服务发布](#lesson-07-service) | [Service 在底层是怎么实现的？]() |
| | | | [实验：发布服务]() |
| | | | [什么是 Ingress？]() |
| | | | [实验：对集群外发布服务]() |
| | | [8. 其它](#lesson-08advance) | [监控、日志、排错](#) |
| | | | [什么是 HPA / CA / VA？]() |
| | | | [什么是 Federation？]() |
| | | | [K8S 怎么处理有状态服务?]() CRD & Operator |
| 第 4 天 | 上午 | [9. CKA 考试讲解](#lesson-09cka) | [考试注意事项](#) |
| | | | [模拟题讲解](#) |
| | 下午 | | [实验：做模拟题](#) |

## Lesson 01：LXC & Docker

### 1.1 什么是 Linux 容器？

- 虚拟化技术的演进

    ![](../images/container-evolution.png)

- 虚拟化是为了解决什么问题？资源隔离 & 资源限制
- 什么是 Linux 容器？namespace & cgroup
- 什么是 lxc namespace？

    ![](../images/kernel-user-mode.png)

- 什么是 CGroup？
- Mac 和 Win 上 有容器技术么？

### 1.2 容器和虚拟机有何区别？

- 原理
- 应用场景

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

- 在 Ubuntu 18.04 上配置 Docker

    ```bash
    # 更新依赖仓库
    apt-get update -y

    # 安装 Docker
    apt-get install docker.io -y
    systemctl enable docker
    systemctl start docker
    ```

- [如何创建一个镜像？如何启动和调试容器？](https://github.com/99cloud/lab-openstack/tree/master/src/docker-quickstart)

    ```console
    $ python app.py
     * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)

    $ docker run -p 4000:80 maodouzi/get-started:part2
     * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)

    # 进入容器调试
    $ docker exec -it 4224b69e7ee3 /bin/bash
    root@4224b69e7ee3:/app# env
    HOSTNAME=4224b69e7ee3
    PWD=/app
    HOME=/root
    NAME=World
    ...

    # 结束容器
    $ docker stop 4224b69e7ee3
    ```

- [Docker 官方入门参考资料](https://docs.docker.com/get-started/)

### 1.7 Docker 的网络模型

- Bridge 模式
- Host 模式
- CNM

### 1.8 Docker 的存储模型

- Mount 模式
- Volumn 模式

## Lesson 02：Kubernetes Concepts

### 2.1 什么是 K8S？

- 什么是 Kubernetes？容器编排工具
- K8S 和 Docker 有什么关系？参考：[Container runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)
- 为什么叫 K8S？和 Borg 有何关系？

### 2.2 

- K8S 有什么优势？适用于哪些场景？自动化编排：容错纠错，一键部署应用，自动缩放，一键升降级，备份恢复
- 什么是 [OpenShift](https://www.openshift.com/learn/what-is-openshift-x)？和 K8S 相比，OpenShift（ 红帽最有价值的产品 ）有哪些优势？

    ![](../images/openshift-k8s.svg)

- 怎样连接到实验环境？
    - 命令行：

        ```console
        $ ssh root@k8slab.trystack.cn
        root@k8slab.trystack.cn's password:
        Last failed login: Fri Dec 20 22:05:41 CST 2019 from 218.83.103.52 on ssh:notty
        There were 3 failed login attempts since the last successful login.
        Last login: Fri Dec 20 22:02:39 2019 from 218.83.103.52

        Welcome to Alibaba Cloud Elastic Compute Service !

        [root@k8slab ~]# ssh openshift1-aio
        Last login: Fri Dec 20 14:06:24 2019 from 139.224.215.78

        [cloud-user@openshift-aio ~]$ oc get pods
        NAME                       READY     STATUS    RESTARTS   AGE
        docker-registry-1-pmv7w    1/1       Running   0          5h
        registry-console-1-fjgdv   1/1       Running   0          5h
        router-1-t46zw             1/1       Running   0          5h

        [cloud-user@openshift-aio ~]$ exit
        logout
        Connection to openshift1-aio-master.demotheworld.com closed.
        [root@k8slab ~]#
        ```

    - [Web UI](https://console.openshift1-aio-apps.demotheworld.com/k8s/cluster/projects)
- 如何查文档？[K8S](https://kubernetes.io/)，[OpenShift Origin](https://www.okd.io/)
- 其它资料：slack、cncf、quay.io

### Lab: K8S Deployment

- [怎么部署一个 All-In-One 和 Multi-Node 的 K8S 环境？](https://github.com/99cloud/training-kubernetes/blob/master/doc/deploy-k8s-manual.md)

### YAML

- 怎么理解 YAML？列表 / 字典 / 数字 / 字符串

### Namespace & Quota

- 实验：创建一个 namespace
- 实验：为这个 namespace 限定配额
- 实验：创建一个 pod，并测试配额可以限制它的资源使用

### Pod / Deployment / ReplicaSet

- K8S 有哪些基本概念？pod（ pause container ）、deployment、replica set、daemon sets、stateful set、Node

### Lab: K8S Dashboard

### Lab: K8S Objects Operation

- 实验：创建一个 namespace

    ```console
    [root@cn-shanghai ~]# kubectl create namespace student-wuwenxiang
    namespace/wuwenxiang created
    ```

- 实验：创建一个 pod

    ```console
    [root@cn-shanghai ~]# cat student-wuwenxiang-test1.yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: test1
      labels:
        app: test1
      namespace: student-wuwenxiang
    spec:
      containers:
        - name: test1
          image: maodouzi/get-started:part2
          ports:
            - containerPort: 80
    
    [root@cn-shanghai ~]# kubectl create -f student-wuwenxiang-test1.yaml
    pod/test1 created
    ```

- 实验：创建一个 Deployment

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: test2
      namespace: student-wuwenxiang
    spec:
      selector:
        matchLabels:
          app: test2
      replicas: 3
      template:
        metadata:
          labels:
            app: test2
        spec:
          containers:
            - name: test2
              image: maodouzi/get-started:part2
              ports:
                - containerPort: 80
    ```

- 实验：创建一个 Service

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: test2
      namespace: student-wuwenxiang
    spec:
      selector:
        app: test2
      ports:
        - protocol: TCP
          port: 80
          targetPort: 80
    ```

### DeamonSet & SetfulSet

## Lesson 03：K8S Arch & HA

### Kubernetes Arch

- [K8S 有哪些组件](https://kubernetes.io/zh/docs/concepts/architecture/#)？kube proxy、api server、kube scheduler、kube dns、kubelete、kubeproxy、etcd

    ![](../images/k8s-architecture.png)

### ETCD

### Static Pod

### HA 部署方案

- [怎么部署一个 HA 的 K8S 环境？](https://github.com/99cloud/training-kubernetes/blob/master/doc/deploy-aws-ha-k8s-cluster.md)，参考：[penshift-container-platform-reference-architecture-implementation-guides](https://blog.openshift.com/openshift-container-platform-reference-architecture-implementation-guides/)

    ![](../images/openshift-network-arch-azure.png)

    ![](../images/openshift-ha-deployment.png)

## Lesson 04：K8S Auth & Security

### Authentication / Authorization / Admission

- K8S 的认证过程？Authentication、Authorization（ RBRA / ABAC / WebHook ）、Admission Controller

### Network Security

- Kubernetes 的网络选型？flannel、calico、ovs、ovn

### Service Account & Role

### Lab: User & Role

- 实验：创建 Normal 用户使用 kubectl 工具
- 实验：创建 Normal 用户并给予超级管理员组
- 实验：创建 Service Account 并绑定角色

## Lesson 05: K8S Schedule

### Labels

- 实验：Node Label 和 Node Selector
- 实验：Pod Label 和 Replica Controller

### Taints & Toleration

- 实验：Taints 污染标签 & Toleration 容忍标签

### Node Affinity

- 实验：Node Affinity 节点亲和

### Inter-Pod Affinity / Anti

- 实验：Inter-Pod Affinity / Anti，Pod 的亲和与反亲和

### Lab: Pod Schedule

## Lesson 06: K8S Storage

### ConfigMap & Secret

- 实验：Config Map
- 实验：Secret

### PV / PVC

- 基本概念：PV / PVC

### Storage Class

- 基本概念：Storage Class
- 实验：Storage Class

### Lab: ConfigMap / Secret / PV & PVC / StorageClass

## Lesson 07: Service

### Lab: Service

- 基本概念：Service
- 实验：Service

### Ingress

- 实验：Ingress / Route

### Lab: Ingress Controller

## Lesson 08：Advance

### Monitor / Log / Debug

### HPA / CA / VA

- 怎么理解 HPA / CA / VPA？

### Federation

- Kubenetes Federation vs ManageIQ

### CRD & Operator

##	Lesson 09：CKA

### Tips

### Quiz

### Lab: Quiz
