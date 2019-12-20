# Class-01: K8S in One Day

## Quick Start

- 什么是容器？namespace & cgroup
- 什么是 lxc namespace？

    ![](https://camo.githubusercontent.com/32d7d4def8e4bfef2562f15b073083272ee1d13f/687474703a2f2f6c616f61722e6769746875622e696f2f696d616765732f6e616d6573706163652d73706163652e706e67)

- 什么是 [Docker](https://docs.docker.com/engine/docker-overview/#namespaces)（ [QuickStart 1](https://docs.docker.com/get-started/)，[QuickStart 2](https://github.com/99cloud/lab-openstack/tree/master/src/docker-quickstart) ）？Docker 和容器有什么关系（ why Linus don't care docker ）？

    ![](https://camo.githubusercontent.com/c998b5298e47a56406a882fa983079f50be88230/68747470733a2f2f692e696d6775722e636f6d2f57476a754270532e706e67)

- [容器和虚拟机有什么区别？](https://docs.docker.com/get-started/)
- 什么是 Kubernetes ？它和 Docker 有什么关系？
- K8S 有什么优势？适用于哪些场景？自动化编排：容错纠错，一键部署应用，自动缩放，一键升降级，备份恢复
- 什么是 [OpenShift](https://www.openshift.com/learn/what-is-openshift-x)？和 K8S 相比，OpenShift 有哪些优势？

    ![](https://www.openshift.com/hubfs/images/illustrations/marketure-diagram.svg)

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
- [怎么部署一个 All-In-One 的 K8S 环境？](https://github.com/99cloud/training-kubernetes/blob/master/doc/deploy-k8s-manual.md)

## K8S Basic

- [K8S 有哪些组件](https://kubernetes.io/zh/docs/concepts/architecture/#)？kube proxy、api server、kube scheduler、kube dns、kubelete、kubeproxy、etcd

    ![](https://d33wubrfki0l68.cloudfront.net/e298a92e2454520dddefc3b4df28ad68f9b91c6f/70d52/images/docs/pre-ccm-arch.png)

- 怎么理解 YAML？列表 / 字典 / 数字 / 字符串
- K8S 有哪些基本概念？deployment、replica set、daemon sets、stateful set、Pod、Node
- K8S 的认证过程？Authentication、Authorization（ RBRA / ABAC / WebHook ）、Admission Controller
- K8S 的用户权限管理
    - 实验：创建 Normal 用户使用 kubectl 工具
    - 实验：创建 Normal 用户并给予超级管理员组
    - 实验：创建 Service Account 并绑定角色
- K8S 的 Namespace 和 Quota
    - 实验：创建一个 namespace
    - 实验：为这个 namespace 限定配额
    - 实验：创建一个 pod，并测试配额可以限制它的资源使用
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

## K8S Advance

- 监控和计量
- 日志
- [怎么部署一个 HA 的 K8S 环境？](https://github.com/99cloud/training-kubernetes/blob/master/doc/deploy-aws-ha-k8s-cluster.md)，参考：[penshift-container-platform-reference-architecture-implementation-guides](https://blog.openshift.com/openshift-container-platform-reference-architecture-implementation-guides/)

    ![](https://i1.wp.com/blog.openshift.com/wp-content/uploads/refarch-ocp-on-azure-v6.png?w=1338&ssl=1)

    ![](https://miro.medium.com/max/2712/1*hX5dwGlqq4-myZNSbYwZ7g.png)

- 怎么理解 HPA / CA / VPA？
- Kubenetes Federation vs ManageIQ