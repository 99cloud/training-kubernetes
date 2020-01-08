# Kubernetes-Administration

## Prefix

- 授课时长：
    - 上午：9:30 至 11:30
    - 下午：13:30 至 16:30
- Prerequisite
    - vim 基础操作 -- 编辑、修改、保存文件
    - 网络基础知识 -- 网段 cidr、vlan、vxlan、配置 linux 网卡等等
    - 基础的 linux 知识 -- 权限、文件系统、服务
    - systemd 的基础操作 -- 重启、关闭、启动、重载、查看 systemd 的服务

## Catalog

| Date | Time | Title | Content |
| ---- | ---- | ----- | ------- |
| 第 1 天 | 上午 | [Lesson 01：Linux 容器和 Docker](#lesson-01lxc--docker) | [什么是 Linux 容器]() |
| | | | [什么是 Docker]() |
| | | | [Docker 的网络模型]() |
| | | | [Docker 的存储模型]() |
| | | | [实验：Docker Quick Start]()  |
| | 下午 | [Lesson 02：Kubernetes 的基本概念](#lesson-02kubernetes-concepts) | [Kubernetes（ K8S ）的起源和适用场景]() |
| | | | [YAML]() |
| | | | [Namespace & Quota]() |
| | | | [Pod / Deployment / ReplicaSet]() |
| | | | [实验：K8S Dashboard]() |
| | | | [实验：K8S 对象管理操作]() |
| | | | [DeamonSet & SetfulSet]() |
| | | [Lesson 03：K8S 的模块架构和部署](#lesson-03k8s-arch--deployment) | [Kubernetes 的模块架构]() |
| | | | [ETCD]() |
| | | | [静态 Pod]() |
| | | | [实验：K8S 的部署]() |
| 第 2 天 | 上午 | | [HA 部署方案]() |
| | | [Lesson 04：K8S 的认证和安全](#lesson-04k8s-auth--security) | [认证、鉴权和准入]() |
| | | | [网络安全]() |
| | | | [用户和角色]() |
| | | | [实验：添加用户 & 绑定角色]() |
| | | [Lesson 05：K8S 的调度](#lesson-05-k8s-schedule) | [Labels：标签](#) |
| | | | [Taints：污染标签 & Toleration：容忍标签](#) |
| | | | [Node Affinity：节点亲和 ](#) |
| | | | [Inter-Pod Affinity / Anti：Pod 的亲和 / 反亲和](#) |
| | | | [实验：Pod 调度](#) |
| | 下午 | [Lesson 06：K8S 的数据持久化](#lesson-06-k8s-storage) | [ConfigMap & Secret](#) |
| | | | [PV / PVC](#) |
| | | | [Storage Class](#) |
| | | | [实验：ConfigMap / Secret / PV & PVC / StorageClass](#) |
| | | [Lesson 07：服务发布](#lesson-07-service) | [Service](#) |
| | | | [实验：发布服务](#) |
| | | | [Ingress](#) |
| | | | [实验：对集群外发布服务](#) |
| | | [Lesson 08：其它](#lesson-08advance) | [监控、日志、排错](#) |
| | | | [HPA / CA / VA](#) |
| | | | [Federation](#) |
| | | | [CRD & Operator](#) |
| 第 3 天 | 上午 | [Lesson 09：CKA 考试讲解](#lesson-09cka) | [考试注意事项](#) |
| | | | [模拟题讲解](#) |
| | 下午 | | [实验：做模拟题](#) |

## Lesson 01：LXC & Docker

### What is LXC

- 什么是 Linux 容器？namespace & cgroup
- 什么是 lxc namespace？

    ![](../images/kernel-user-mode.png)

- 什么是 CGroup？

### What is Docker

- 什么是 [Docker](https://docs.docker.com/engine/docker-overview/#namespaces)（ [QuickStart](https://docs.docker.com/get-started/) ）？

    ![](../images/docker-undertech.png)

- Docker 和容器有什么关系（ why Linus don't care docker ）？

### Docker Network

### Docker Storage

### Docker Quick Start

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

- [容器和虚拟机有什么区别？](https://docs.docker.com/get-started/)
- [什么是 CRI-O ？](https://zhuanlan.zhihu.com/p/30667806)
- [什么是 kata-container ？](https://katacontainers.io/collateral/kata-containers-1pager.pdf)

## Lesson 02：Kubernetes Concepts

### Kubernetes Introduction

- 什么是 Kubernetes ？它和 Docker 有什么关系？参考：[Container runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)
- K8S 有什么优势？适用于哪些场景？自动化编排：容错纠错，一键部署应用，自动缩放，一键升降级，备份恢复
- 什么是 [OpenShift](https://www.openshift.com/learn/what-is-openshift-x)？和 K8S 相比，OpenShift 有哪些优势？

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

## Lesson 03：K8S Arch & Deployment

### Kubernetes Arch

- [K8S 有哪些组件](https://kubernetes.io/zh/docs/concepts/architecture/#)？kube proxy、api server、kube scheduler、kube dns、kubelete、kubeproxy、etcd

    ![](../images/k8s-architecture.png)

### ETCD

### Static Pod

### Lab: K8S Deployment

- [怎么部署一个 All-In-One 和 Multi-Node 的 K8S 环境？](https://github.com/99cloud/training-kubernetes/blob/master/doc/deploy-k8s-manual.md)

### HA 部署方案

- [怎么部署一个 HA 的 K8S 环境？](https://github.com/99cloud/training-kubernetes/blob/master/doc/deploy-aws-ha-k8s-cluster.md)，参考：[penshift-container-platform-reference-architecture-implementation-guides](https://blog.openshift.com/openshift-container-platform-reference-architecture-implementation-guides/)

    ![](../images/openshift-network-arch-azure.png)

    ![](../images/openshift-ha-deployment.png)

## Lesson 04：K8S Auth & Security

### Authentication / Authorization / Admission

- K8S 的认证过程？Authentication、Authorization（ RBRA / ABAC / WebHook ）、Admission Controller
- Kubenetes 的调度
    - 实验：Node Label 和 Node Selector
    - 实验：Pod Label 和 Replica Controller
    - 实验：Taints 污染标签 & Toleration 容忍标签
    - 实验：Node Affinity 节点亲和
    - 实验：Inter-Pod Affinity / Anti，Pod 的亲和与反亲和
- Kubernetes 的网络选型？flannel、calico、ovs、ovn
- Kubernetes 的存储
    - 基本概念：PV / PVC / Storage Class
    - 实验：Config Map
    - 实验：Secret
    - 实验：Storage Class
- Kubernetes 服务发布
    - 基本概念：Service
    - 实验：Service
    - 实验：Ingress / Route

### Network Security

### Service Account & Role

### Lab: User & Role

- 实验：创建 Normal 用户使用 kubectl 工具
- 实验：创建 Normal 用户并给予超级管理员组
- 实验：创建 Service Account 并绑定角色

## Lesson 05: K8S Schedule

### Labels

### Taints & Toleration

### Node Affinity

### Inter-Pod Affinity / Anti

### Lab: Pod Schedule

## Lesson 06: K8S Storage

### ConfigMap & Secret

### PV / PVC

### Storage Class

### Lab: ConfigMap / Secret / PV & PVC / StorageClass

## Lesson 07: Service

### Lab: Service

### Ingress

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
