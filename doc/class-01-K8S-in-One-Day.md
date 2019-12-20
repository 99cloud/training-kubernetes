# Class-01: K8S in One Day

## Quick Start

- 什么是容器？容器和虚拟机有什么区别？
- 什么是 [Docker](https://docs.docker.com/get-started/)？Docker 和容器有什么关系？
- 什么是 Kubernetes ？它和 Docker 有什么关系？
- K8S 有什么优势？适用于哪些场景？自动化编排：容错纠错，一键部署应用，自动缩放，一键升降级，备份恢复
- 什么是 OpenShift？和 K8S 相比，OpenShift 有哪些优势？
- 怎样连接到实验环境，命令行和 WebUI
- 如何查文档？[K8S](https://kubernetes.io/)，[OpenShift Origin](https://www.okd.io/)
- 怎么部署一个 All-In-One 的 K8S 环境？

## K8S Basic

- K8S 有哪些组件？kube proxy、api server、kube scheduler、kube dns、kubelete、kubeproxy、etcd
- 怎么理解 YAML？
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
- 怎么部署一个 HA 的 K8S 环境？
- 怎么理解 HPA / CA / VPA？
- Kubenetes Federation