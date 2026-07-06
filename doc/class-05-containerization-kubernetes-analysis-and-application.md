# 容器化技术与 K8S 详解及应用

- **课程定位**：2 天 × 6 小时，以夯实基础为主，面向应用实践。
- **适用对象**：熟悉 Linux 基本操作；了解 IP、端口、HTTP；能阅读 YAML 更佳；**容器 / K8S
  零基础可学**。
- **版本说明**：本讲义以 **Kubernetes 1.30+** 为基线，重点标注 **1.33（Octarine）**
  及之后的新特性；不涉及 dockershim、Pod Security Policy（PSP）等过时内容。

## 注意 ⚠️

- **未经允许，禁止转载**

---

## Prefix

| 项               | 说明                                                     |
| ---------------- | -------------------------------------------------------- |
| **授课时长**     | 2 天，每天 6 小时（建议上午 3h + 下午 3h），合计 12 小时 |
| **交付形态**     | 线下，理论 + Demo 穿插，**实操占比约 50%**               |
| **实验环境**     | KubeClipper 快速搭建集群；节点运行时为 **containerd**    |
| **Prerequisite** | Linux 基本操作；IP / 端口 / HTTP 概念；YAML 基础（可选） |

**相关讲义**：

- [CKA 培训](class-01-Kubernetes-Administration.md)
- [K8S 最佳实践](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/master/doc/kubernetes-best-practices.md)

### 本课不展开

- kubeadm 手工安装全链路、控制面高可用细节
- RBAC 深度、NetworkPolicy、Admission 深度定制
- Ingress / Gateway API 生产级网关深度实践
- Prometheus 联邦/长期存储、全链路 Trace 深度建设
- ELK/Loki 生产级容量规划
- AIOps 平台私有化部署、模型微调与自动修复闭环
- 拓扑调度、HPA、联邦集群、Helm / GitOps 深度
- CKA/CKAD 考试辅导

---

## Catalog

| 天数        | 时段 | 主题                                                     | 核心内容                                        |
| ----------- | ---- | -------------------------------------------------------- | ----------------------------------------------- |
| **第 1 天** | 上午 | [1. 容器与运行时](#lesson-01-容器与运行时)               | 容器原理、Docker、containerd 生态               |
|             | 下午 | [2. K8S 架构与首批部署](#lesson-02-k8s-架构与首批部署)   | 声明式模型、KubeClipper、Pod/Deployment/Service |
| **第 2 天** | 上午 | [3. 工作负载、存储与调度](#lesson-03-工作负载存储与调度) | DaemonSet/StatefulSet、PV/PVC、调度策略         |
|             | 下午 | [4. 配置发布与运维概览](#lesson-04-配置发布与运维概览)   | ConfigMap/Secret、探针、排障、可观测、AIOps     |

### 课程主线（对照大纲）

1. **容器与运行时** → [Lesson 01](#lesson-01-容器与运行时)
2. **镜像与交付** → [1.5.1 镜像与交付](#151-镜像与交付dockerfile-最佳实践)
3. **K8S 核心** → [Lesson 02](#lesson-02-k8s-架构与首批部署)
4. **面向应用深化** → [Lesson 03](#lesson-03-工作负载存储与调度) +
   [4.1–4.3](#lesson-04-配置发布与运维概览)
5. **运维与可观测** → [4.5](#45-运维与可观测性概览)

---

## 课程收获（Checklist）

完成本课后，学员应能够：

- [ ] 说清容器与虚拟机的区别及适用场景
- [ ] 使用 Docker 完成镜像构建与容器运行
- [ ] 理解 Docker、containerd、**nerdctl**、**crictl** 的分工
- [ ] 使用 KubeClipper 快速创建实验集群并完成应用部署
- [ ] 理解 **声明式 API** 与 **Controller 调谐（Reconcile）**
- [ ] 熟练使用 Deployment、Service；了解 DaemonSet、StatefulSet 典型场景
- [ ] 完成 PV/PVC 持久化存储与调度策略 Demo
- [ ] 完成配置注入、滚动更新、回滚与常见故障初判
- [ ] 了解 CRD、Operator、Ingress Controller 等扩展生态（概览）
- [ ] 建立 Metrics/Logs 可观测性认知；了解生产部署要点与 AIOps 方向

---

# 第 1 天：容器运行时与 K8S 应用部署

<a id="lesson-01-容器与运行时"></a>

## Lesson 01：容器与运行时

### 1.1 部署方式演进

应用部署方式大致经历了：

| 阶段            | 特点                         | 典型问题                         |
| --------------- | ---------------------------- | -------------------------------- |
| 物理机直接部署  | 简单直接                     | 环境不一致、扩容慢、资源利用率低 |
| 虚拟机          | 强隔离、可跑不同 OS          | 镜像大、启动慢、密度有限         |
| 容器            | 进程级隔离、镜像小、秒级启动 | 需编排平台管理大规模集群         |
| 容器编排（K8S） | 声明式、自愈、扩缩、服务发现 | 学习曲线、运维复杂度             |

![部署方式演进](images/container-evolution.png)

![IaaS / PaaS / CaaS 分层（容器位于 CaaS）](images/caas-kaas-paas.png)

![算力演进简史](images/computing-history.png)

> 算力架构从集中式（大型机）→ 分布式（PC/云）→ 泛在式（云边协同）持续演进。容器与 K8S
> 是**云计算下半场**「算力统一调度、接口统一（Kubernetes API）」的关键技术栈之一。详见
> [边缘云与算力演进](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/master/doc/mec-edge-and-ai.md#12-边缘云的起源与演进)。

**Reference**

- [What is a Container?](https://www.docker.com/resources/what-container/) — Docker 官方容器概念
- [Kubernetes 是什么？](https://kubernetes.io/zh-cn/docs/concepts/overview/) — 官方概览
- [边缘云与算力演进](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/master/doc/mec-edge-and-ai.md)

### 1.2 容器 vs 虚拟机

| 维度     | 虚拟机（VM）              | 容器（Container）                        |
| -------- | ------------------------- | ---------------------------------------- |
| 隔离级别 | 硬件虚拟化，独立 Guest OS | 内核 Namespace + Cgroups，共享 Host 内核 |
| 启动速度 | 分钟级                    | 秒级                                     |
| 镜像大小 | GB 级                     | MB 级常见                                |
| 密度     | 较低                      | 较高                                     |
| 适用场景 | 不同内核/OS、强隔离合规   | 微服务、CI/CD、云原生应用                |

**原理要点**

- 一个 KVM 虚拟机对应一个 QEMU/KVM 进程；vCPU 对应宿主机线程。
- 一个容器是一组被 **Namespace** 隔离、被 **Cgroups**
  限制资源的进程组；容器内进程就是宿主机上的进程。

**何时仍需要 VM？**

- 需要与宿主机**不同内核**或**不同操作系统**
- 需要硬件级隔离（如部分合规场景）→ 可进一步考虑 Kata Containers、gVisor 等安全容器

![容器 vs 传统虚拟机](images/katacontainers_traditionalvskata_diagram.jpg)

![Kata Containers 架构（安全容器）](images/katacontainers-architecture-diagram.jpg)

**Reference**

- [Kata Containers](https://katacontainers.io/learn/) —
  [一页纸 PDF](https://katacontainers.io/collateral/kata-containers-1pager.pdf)
- [Namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html) — Linux man page
- [Control Groups (cgroups)](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html) —
  Linux 内核文档

### 1.3 Linux 容器底层：Namespace 与 Cgroups

| 机制          | 作用                                            | K8S/Docker 中的体现                             |
| ------------- | ----------------------------------------------- | ----------------------------------------------- |
| **Namespace** | 隔离 PID、Network、Mount、UTS、IPC、User 等视图 | Pod 内容器共享 Network/IPC/UTS Namespace        |
| **Cgroups**   | 限制 CPU、内存、IO 等资源                       | `resources.requests/limits` 最终由 Cgroups 落地 |

Pod 内 pause 容器与业务容器共享 net/ipc/uts namespace（可在节点上用 `/proc/<pid>/ns/` 观察）。

![Kernel / User Mode 与 Namespace](images/kernel-user-mode.png)

**Reference**

- [Docker overview — Namespaces](https://docs.docker.com/engine/docker-overview/#namespaces)
- [About containers — Cgroups](https://docs.docker.com/engine/containers/resource_constraints/)

### 1.4 OCI 与镜像标准

**OCI（Open Container Initiative）** 定义了两份核心规范：

| 规范             | 内容                                                 |
| ---------------- | ---------------------------------------------------- |
| **Image Spec**   | 镜像目录结构、manifest、layer 格式                   |
| **Runtime Spec** | 容器生命周期：`create` / `start` / `stop` / `delete` |

**runC** 是 OCI Runtime 的参考实现（由 Docker 捐献 libcontainer 演化而来）。

**Reference**

- [Open Container Initiative](https://opencontainers.org/)
- [OCI Runtime Spec](https://github.com/opencontainers/runtime-spec)

### 1.5 Docker 架构与核心对象

Docker 概念空间：

| 对象                  | 说明                                    |
| --------------------- | --------------------------------------- |
| **Image（镜像）**     | 只读模板，分层存储                      |
| **Container（容器）** | 镜像的运行实例                          |
| **Registry（仓库）**  | 镜像存储与分发（Docker Hub、Harbor 等） |
| **Dockerfile**        | 声明式构建镜像的脚本                    |

![Docker 底层技术](images/docker-undertech.png)

![Docker 架构](images/docker-arch.png)

**Reference**

- [Docker overview](https://docs.docker.com/engine/docker-overview/)
- [Docker Get Started](https://docs.docker.com/get-started/)

<a id="151-镜像与交付dockerfile-最佳实践"></a>

#### 1.5.1 镜像与交付（Dockerfile 最佳实践）

容器化交付的核心：**把应用及其依赖打包成可移植、可版本化的镜像**，推送到 Registry
后在任意环境一致运行。

| 实践                 | 说明                                                                |
| -------------------- | ------------------------------------------------------------------- |
| **多阶段构建**       | 编译阶段与运行阶段分离，减小最终镜像体积                            |
| **固定基础镜像 tag** | 使用 `python:3.12-slim` 而非 `python:latest`                        |
| **非 root 运行**     | Dockerfile 中 `USER nonroot`（配合 PSS restricted）                 |
| **显式声明依赖**     | requirements.txt / go.mod 与代码一起版本管理                        |
| **配置外置**         | 不把环境相关配置 bake 进镜像；运行时注入 ConfigMap/Secret           |
| **日志写 stdout**    | 符合 [12-Factor App](https://12factor.net/logs) 与 K8S 日志采集约定 |

```dockerfile
# 多阶段构建示例
FROM golang:1.22 AS builder
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /app

FROM gcr.io/distroless/static-debian12
COPY --from=builder /app /app
USER nonroot:nonroot
ENTRYPOINT ["/app"]
```

推送私有仓库后，K8S 侧通过 `imagePullSecrets` 拉取（见
[4.1.1](#411-私有镜像拉取imagepullsecrets重点)）。

![Harbor 私有镜像仓库架构（概念）](images/harbor-arch.png)

**Reference**

- [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/)
- [The Twelve-Factor App](https://12factor.net/)
- [Harbor](https://goharbor.io/docs/latest/)

#### 实验：Docker Quick Start

```bash
# 安装 Docker Engine（以 Ubuntu 为例，详见官方文档）
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl enable --now docker

# 验证
docker run hello-world

# 常用操作
docker images
docker ps -a
docker logs <container>
docker exec -it <container> /bin/bash
docker stop <container> && docker rm <container>
```

#### 实验：构建并运行示例 Web 应用

```bash
mkdir ~/demo-web && cd ~/demo-web

# 示例 app.py（Flask）
cat > app.py <<'EOF'
from flask import Flask
import os, socket
app = Flask(__name__)
@app.route("/")
def hello():
    return f"<h3>Hello {os.getenv('NAME','world')}!</h3><b>Hostname:</b> {socket.gethostname()}"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
EOF

cat > requirements.txt <<EOF
flask
EOF

cat > Dockerfile <<'EOF'
FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
EOF

docker build -t demo-web:latest .
docker run -d -p 5001:5000 --name demo-web demo-web:latest
curl http://127.0.0.1:5001/
```

**Reference**

- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [lab-openstack docker-quickstart](https://github.com/99cloud/lab-openstack/tree/master/src/docker-quickstart)
  / [Gitee 镜像](https://gitee.com/dev-99cloud/lab-openstack/tree/master/src/docker-quickstart)
- [Docker 官方入门](https://docs.docker.com/get-started/)

#### Docker 网络与存储（要点）

- **Bridge 模式**：默认；容器通过 veth pair 接入 docker0 网桥。
- **Host 模式**：容器直接使用宿主机网络栈。
- **Volume / Bind Mount**：数据持久化；K8S 中对应 PV/PVC、emptyDir 等。

![Docker Bridge 网络模型](images/bridge_network.jpeg)

**Reference**

- [Docker network](https://docs.docker.com/engine/network/)
- [Docker storage](https://docs.docker.com/storage/)

### 1.6 从 Docker 到 containerd 生态

#### 1.6.1 K8S 为何以 containerd 为默认运行时

K8S 通过 **CRI（Container Runtime Interface）** 与底层运行时通信：

```
Orchestration API (kubelet)
        ↓ gRPC
CRI Runtime (containerd / CRI-O)
        ↓ OCI
OCI Runtime (runc / kata / gVisor)
        ↓
Linux Kernel (Namespace + Cgroups)
```

![K8S 经 CRI 调用 Docker（历史架构，dockershim 已移除）](images/k8s-CRI-OCI-docker.png)

![containerd 1.0 — 独立 cri-containerd 进程](images/k8s-containerd-1-0.png)

![containerd 1.1+ — CRI 插件内嵌](images/k8s-containerd-1-1.png)

![CRI-O 调用链](images/k8s-cri-o-flow.png)

![CRI-O 架构（一）](images/k8s-cri-o-arch-1.png)

![CRI-O 架构（二）](images/k8s-cri-o-arch-2.jpg)

**重要变更（已过时内容剔除）**

| 内容                   | 状态               | 说明                                                   |
| ---------------------- | ------------------ | ------------------------------------------------------ |
| **dockershim**         | ❌ 已移除（1.24+） | K8S 不再内置 Docker 适配层                             |
| Docker 作为 K8S 运行时 | ❌ 不推荐          | 需额外 cri-dockerd 适配，生产应直接用 containerd/CRI-O |
| **containerd**         | ✅ 默认            | kubeadm、KubeClipper 等均默认 containerd               |

**Reference**

- [Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)
  — 官方运行时指南
- [CRI API](https://github.com/kubernetes/cri-api) —
  [cri-api/pkg/apis/services.go](https://github.com/kubernetes/cri-api/blob/master/pkg/apis/services.go)
- [CRI-O 官网](https://cri-o.io/)
- [kubernetes-best-practices — 容器运行时](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/master/doc/kubernetes-best-practices.md#2-容器运行时)

#### 1.6.2 containerd 生态工具对比

| 工具        | 定位                                      | 典型场景                                              |
| ----------- | ----------------------------------------- | ----------------------------------------------------- |
| **ctr**     | containerd 原生 CLI                       | 底层调试、直接操作 containerd                         |
| **nerdctl** | Docker 兼容 CLI（`nerdctl run/build/ps`） | 习惯 Docker 命令的运维/开发                           |
| **crictl**  | CRI 调试 CLI                              | **节点排障**：查 Pod/容器/镜像（与 kubelet 视角一致） |

![containerd 与 K8S 对接（现行）](images/k8s-cri-containerd.png)

![Docker → containerd 演进](images/docker-and-kubernetes-use-containerd-2000-opt.png)

![命令行工具对比：crictl / ctr / nerdctl / podman](images/k8s-containerd-tools.png)

![CRI 技术栈总览](images/k8s-cri-tools.png)

![containerd 生态（CRI / CNI / CSI 等）](images/containerd-eco-system.jpeg)

#### crictl 配置要点

节点上使用 crictl 前需指定 CRI endpoint（**不要再配置 dockershim.sock**）：

```bash
cat <<EOF | sudo tee /etc/crictl.yaml
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
timeout: 10
EOF
```

| docker 命令      | crictl 等价      |
| ---------------- | ---------------- |
| `docker ps`      | `crictl ps`      |
| `docker images`  | `crictl images`  |
| `docker logs`    | `crictl logs`    |
| `docker inspect` | `crictl inspect` |
| `docker exec`    | `crictl exec`    |

crictl 独有：`crictl pods` / `crictl inspectp` / `crictl port-forward` — 以 **Pod** 为视角排障。

```bash
# 节点上查看 K8S Pod（推荐 crictl，而非 docker ps）
crictl pods
crictl ps
crictl images
crictl inspect <container-id>

# nerdctl（需 containerd + nerdctl 安装）
nerdctl ps
nerdctl images

# ctr（containerd 原生）
ctr -n k8s.io containers list
ctr -n k8s.io images list
```

> **Note**：containerd 的 K8S 命名空间通常为 `k8s.io`。

**Reference**

- [crictl — Debugging Kubernetes nodes with crictl](https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl/)
- [cri-tools 文档（含 docker/crictl 命令对照，旧版参考）](https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md)
- [nerdctl](https://github.com/containerd/nerdctl)
- [containerd](https://containerd.io/)
- [kubernetes-best-practices — Containerd 和命令行工具](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/master/doc/kubernetes-best-practices.md#22-containerd)
  /
  [命令行对比表](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/master/doc/kubernetes-best-practices.md#222-命令行对比)
- [Map crictl to Docker CLI](https://kubernetes.io/zh-cn/docs/tasks/debug/debug-cluster/crictl/#映射-crictl-到-docker-命令)

#### 实验：节点侧对照理解容器视图

```bash
# 1. 在集群中创建一个 Pod
kubectl run nginx --image=nginx:1.27 --port=80

# 2. 到 Pod 所在节点
kubectl get pod nginx -o wide
NODE=<pod-scheduled-node>

# 3. 节点上用 crictl 查看（与 kubelet 一致）
ssh $NODE
sudo crictl pods --name nginx
sudo crictl ps | grep nginx
sudo crictl inspect $(sudo crictl ps -q --name nginx | head -1) | jq .info.runtimeSpec
```

---

<a id="lesson-02-k8s-架构与首批部署"></a>

## Lesson 02：K8S 架构与首批部署

### 2.1 K8S 解决什么问题

K8S 是**容器编排平台**，核心价值：

| 能力                   | 说明                             |
| ---------------------- | -------------------------------- |
| **编排**               | 声明期望状态，自动调度到合适节点 |
| **自愈**               | 容器/Pod 异常时重建              |
| **扩缩**               | 副本数弹性调整（本课不展开 HPA） |
| **服务发现与负载均衡** | Service、DNS                     |
| **滚动发布与回滚**     | Deployment 内置策略              |
| **配置与密钥外置**     | ConfigMap、Secret                |

**云原生视角**：K8S
解决的是「业务无关的基础运维」——自动调度、自愈、扩缩、服务注册发现、配置管理。业务团队**把业务上云后只关注业务本身**。详见
[云原生基本原则](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/master/doc/cloudnative-and-mircoservice.md#112-云原生的基本原则)（API +
微服务 + 容器化）。

**与单机 Docker 的差异**：Docker 管单机容器；K8S 管**跨节点**的容器集群，并提供控制平面 API。

**Reference**

- [Why Kubernetes?](https://kubernetes.io/docs/concepts/overview/#why-you-need-kubernetes-and-what-can-it-do)
- [Production-Ready Features](https://kubernetes.io/docs/concepts/overview/#why-you-need-kubernetes-and-what-can-it-do)

### 2.2 K8S 不解决什么问题

- 用户身份体系（需对接 LDAP/OIDC 等）
- 服务网格限流熔断（Istio 等，本课不展开）
- 完整监控/日志平台（需 Prometheus、Loki 等叠加）
- 应用业务逻辑本身
- 底层 IaaS 资源供给

### 2.3 K8S 架构概览

| 组件                         | 类型             | 职责                               |
| ---------------------------- | ---------------- | ---------------------------------- |
| **kube-apiserver**           | 控制平面         | REST API 入口，唯一 etcd 写入口    |
| **etcd**                     | 控制平面         | 集群状态持久化（键值存储）         |
| **kube-scheduler**           | 控制平面         | 为 Pod 选择节点                    |
| **kube-controller-manager**  | 控制平面         | 运行各类 Controller，驱动调谐      |
| **cloud-controller-manager** | 控制平面（可选） | 对接云厂商 LB/Route 等             |
| **kubelet**                  | 工作节点         | 接收 PodSpec，通过 CRI 管理容器    |
| **kube-proxy**               | 工作节点         | 维护 Service 的 iptables/IPVS 规则 |
| **Container Runtime**        | 工作节点         | containerd / CRI-O                 |

![Kubernetes 架构](images/k8s-architecture.png)

K8S 源自 Google Borg 的编排思想，但架构与 API 完全独立设计：

![Borg 架构（K8S 思想渊源）](images/borg-arch.png)

**Reference**

- [Kubernetes 组件](https://kubernetes.io/zh-cn/docs/concepts/architecture/#%E6%A6%82%E8%BF%B0)
- [Node Components](https://kubernetes.io/zh-cn/docs/concepts/architecture/#node-components)
- [OpenShift 与 K8S 关系概览](https://developers.redhat.com/learn/openshift)

### 2.4 声明式模型与 Controller 原理（重点）

#### 声明式 vs 命令式

| 方式       | 示例                               | 特点                   |
| ---------- | ---------------------------------- | ---------------------- |
| **命令式** | `kubectl run nginx --image=nginx`  | 告诉系统「做什么」     |
| **声明式** | `kubectl apply -f deployment.yaml` | 描述「期望状态是什么」 |

#### Controller 与 Reconcile（调谐）

```
用户提交 YAML（期望状态）
        ↓
  API Server 写入 etcd
        ↓
  Controller 监听变化
        ↓
  对比 期望状态 vs 实际状态
        ↓
  Reconcile：创建/更新/删除资源直到一致
```

![控制回路（Control Loop）](images/kubernetes-co-loop.webp)

![Controller 调谐循环](images/kubernetes-controller-loop.webp)

![Informer 边缘触发](images/kubernetes-controller-trigger.png)

Kubernetes 的核心是**控制理论**：控制器定期（或通过 Informer **边缘触发**）比较 **Spec（期望状态）**
与 **Status（实际状态）**，驱动调谐直到误差为零。kube-controller-manager 整合了
ReplicaSet、Deployment、Node 等数十种内置控制器。

典型 Controller：

| Controller                | 调谐目标                     |
| ------------------------- | ---------------------------- |
| **Deployment Controller** | 维护指定副本数的 Pod         |
| **ReplicaSet Controller** | 确保 Pod 副本数              |
| **Service Controller**    | 维护 Endpoints/EndpointSlice |
| **Node Controller**       | 节点健康、Pod 驱逐           |

> **生产环境不要裸跑 Pod**：裸 Pod 无副本保障、无滚动更新、节点故障即丢失。

**Reference**

- [Kubernetes Controllers](https://kubernetes.io/docs/concepts/architecture/controller/)
- [Extend Kubernetes — Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
- [云原生 — 基于 K8S API 的控制器原理](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/master/doc/cloudnative-and-mircoservice.md#171-基于-k8s-api-的云原生)

### 2.5 KubeClipper 快速搭建实验集群

本课使用 **KubeClipper**（基于 kubeadm 封装）快速获得实验集群，**约 10 分钟**完成，不展开 kubeadm
手工步骤。

**KubeClipper 是什么？**

- 轻量级 K8S 集群生命周期管理平台（Web 控制台 + API + **kcctl** CLI）
- 完全兼容原生 Kubernetes；封装 kubeadm 完成安装、升级、扩缩、备份等
- 对比 Sealos / KubeKey 等：具备**图形化页面**、**轻依赖**（不依赖
  Ansible）、**多集群管理**、**离线安装**

| 能力         | KubeClipper | Sealos | KubeKey |
| ------------ | ----------- | ------ | ------- |
| 图形化页面   | ✅          | ❌     | ❌      |
| 轻依赖       | ✅          | ✅     | ✅      |
| 多集群管理   | ✅          | ❌     | ❌      |
| 离线安装     | ✅          | ✅     | ✅      |
| 基于 kubeadm | ✅          | ✅     | ✅      |

![K8S 集群拓扑（概念）](images/kubeadm-cluster.png)

**Reference**

- [KubeClipper 官网](https://kubeclipper.io/)
- [KubeClipper Overview](https://kubeclipper.io/en/docs/overview/)
- [KubeClipper GitHub / QuickStart](https://github.com/kubeclipper/kubeclipper/blob/master/README_zh.md#quick-start)
- [kubernetes-best-practices — KubeClipper](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/master/doc/kubernetes-best-practices.md#314-kubeclipper)

#### 实验：安装 KubeClipper 并创建集群

```bash
# 1. 安装 kcctl
curl -sfLk https://oss.kubeclipper.io/get-kubeclipper.sh | bash -

# 2. 单机 All-in-One 部署 KubeClipper（实验环境）
kcctl deploy

# 3. 浏览器访问控制台（默认 kc-server 所在节点 IP）
# http://<server-ip>

# 4. 获取节点 IP 并创建单节点集群
NODE=$(kcctl get node -o yaml | grep ipv4DefaultIP | head -1 | awk '{print $2}')
kcctl create cluster --master $NODE --name demo --untaint-master

# 5. 查看集群状态（Running 即就绪）
kcctl get cluster

# 6. 下载 kubeconfig 并使用 kubectl
# （控制台或 kcctl 获取 kubeconfig 后）
export KUBECONFIG=~/.kube/demo-config
kubectl get nodes
kubectl get pods -A
```

> **生产环境**：参考 [HA 部署文档](https://kubeclipper.io/en/docs/deployment-docs/ha-deploy/) 部署多
> Server/Agent 节点。

### 2.6 kubectl 与 YAML 基础

#### kubectl 常用命令

```bash
kubectl get nodes,pods,svc,deploy -A
kubectl describe pod <name>
kubectl logs <pod> [-c <container>] [-f]
kubectl exec -it <pod> -- /bin/sh
kubectl apply -f <file.yaml>
kubectl delete -f <file.yaml>
kubectl explain pod.spec.containers   # 内置 API 文档
```

#### K8S 资源对象通用结构

```yaml
apiVersion: <api-group>/<version>   # 如 apps/v1
kind: <ResourceKind>                # 如 Deployment
metadata:
  name: <name>
  namespace: <namespace>            # 默认 default
  labels:
    app: my-app
spec:                               # 期望状态
  ...
status:                             # 实际状态（由系统写入，用户一般不填）
  ...
```

#### YAML 语法要点

- 缩进用空格（不用 Tab）
- 列表项用 `-` 开头
- 键值对用 `key: value`；字符串含特殊字符时加引号

**Reference**

- [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
- [Configuration Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)

### 2.7 核心对象：Namespace、Pod、Deployment、Service

#### Namespace

逻辑隔离单元；不同 Namespace 中同名资源可共存。

```bash
kubectl create namespace dev
kubectl get ns
```

**Reference**

- [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)

#### Pod

K8S **最小调度单位**；一个 Pod 可含一个或多个容器（共享 Network Namespace）。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    image: registry.k8s.io/nginx-slim:0.21
    ports:
    - containerPort: 80
```

```bash
kubectl apply -f pod.yaml
kubectl get pod nginx -o wide
kubectl describe pod nginx
```

**Reference**

- [Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Get started with Kubernetes using Python](https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/)
  — 示例源码 [hello-python](https://github.com/JasonHaley/hello-python) /
  [本仓库 src](https://gitee.com/dev-99cloud/training-kubernetes/tree/master/src/hello-python)

#### Deployment

管理 Pod 副本、滚动更新、回滚的 Controller。

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-python
spec:
  replicas: 3
  selector:
    matchLabels:
      app: hello-python
  template:
    metadata:
      labels:
        app: hello-python
    spec:
      containers:
      - name: app
        image: demo-web:latest
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 5000
        env:
        - name: NAME
          value: "Kubernetes"
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 256Mi
```

```bash
kubectl apply -f deployment.yaml
kubectl get deploy,pods -l app=hello-python
kubectl scale deployment hello-python --replicas=5
```

**Reference**

- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)

#### Service

为一组 Pod 提供稳定访问入口（ClusterIP / NodePort / LoadBalancer）。

![Ingress 与 Service 关系（概念）](images/ingress-service.drawio.svg)

| 类型             | 说明                         | 典型场景          |
| ---------------- | ---------------------------- | ----------------- |
| **ClusterIP**    | 集群内虚拟 IP（默认）        | 集群内服务互访    |
| **NodePort**     | 在每个节点开放固定端口       | 实验/开发外部访问 |
| **LoadBalancer** | 云 LB 或 MetalLB 分配外部 IP | 生产外部访问      |

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-python-svc
spec:
  type: NodePort
  selector:
    app: hello-python
  ports:
  - port: 80
    targetPort: 5000
    nodePort: 31000
```

**Service DNS（集群内）**

```
<service>.<namespace>.svc.cluster.local
```

```bash
kubectl run curl --image=curlimages/curl -it --rm -- \
  curl http://hello-python-svc.default.svc.cluster.local
```

> **Note**：自 K8S 1.21 起，EndpointSlice 为默认 Endpoint 机制；`Endpoints`
> 对象逐步被替代，对使用者透明。

**Reference**

- [Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Connect Applications with Services](https://kubernetes.io/docs/tutorials/services/connect-applications-service/)
- [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
- [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/)
- [MetalLB](https://metallb.universe.tf/) — 裸金属 LoadBalancer 实现
- [kubernetes-best-practices — 网络管理](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/master/doc/kubernetes-best-practices.md#5-网络管理)

#### 实验：完整部署 Web 应用

> 也可直接使用本仓库示例：
> [src/hello-python](https://gitee.com/dev-99cloud/training-kubernetes/tree/master/src/hello-python)
> （含 `main.py`、`Dockerfile`、`deployment.yaml`）。

```bash
# 可选：下载 hello-python 示例
wget https://gitee.com/dev-99cloud/training-kubernetes/raw/master/src/hello-python/main.py
wget https://gitee.com/dev-99cloud/training-kubernetes/raw/master/src/hello-python/requirements.txt
wget https://gitee.com/dev-99cloud/training-kubernetes/raw/master/src/hello-python/Dockerfile
wget https://gitee.com/dev-99cloud/training-kubernetes/raw/master/src/hello-python/deployment.yaml

# 1. 构建镜像并推送到可访问的 Registry（或使用 imagePullPolicy: Never + 预加载镜像）
# 2. 部署 Deployment + Service
kubectl apply -f deployment.yaml -f service.yaml

# 3. 验证
kubectl get pods -l app=hello-python -o wide
curl http://<node-ip>:31000/

# 4. 观察 EndpointSlice
kubectl get endpointslice -l kubernetes.io/service-name=hello-python-svc
```

**第 1 天收束**：运行时体系清晰；集群可用；理解「YAML + Controller」；完成首次应用上线。

---

# 第 2 天：工作负载、存储、调度与综合实践

<a id="lesson-03-工作负载存储与调度"></a>

## Lesson 03：工作负载、存储与调度

### 3.1 DaemonSet 与 StatefulSet

#### 工作负载选型

![K8S 架构（工作负载在其中的位置）](images/kubernetes-arch.png)

| 控制器          | 副本策略                         | 典型场景                       |
| --------------- | -------------------------------- | ------------------------------ |
| **Deployment**  | 任意副本，Pod 可替换             | 无状态 Web/API 服务            |
| **DaemonSet**   | 每个（匹配）节点一个 Pod         | 日志采集、监控 Agent、CNI 插件 |
| **StatefulSet** | 固定序号、稳定网络标识、有序启停 | 数据库、消息队列、分布式存储   |

#### DaemonSet 示例

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: node-exporter
  template:
    metadata:
      labels:
        app: node-exporter
    spec:
      tolerations:
      - operator: Exists   # 容忍所有污点，确保每节点都跑
      containers:
      - name: node-exporter
        image: prom/node-exporter:v1.8.0
        ports:
        - containerPort: 9100
```

**Reference**

- [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)

#### StatefulSet 示例（要点）

- 稳定 Pod 名：`<statefulset>-0`, `<statefulset>-1`, ...
- 稳定 DNS：`<pod>.<headless-svc>.<ns>.svc.cluster.local`
- 需配合 **Headless Service** 与 **volumeClaimTemplates**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-headless
spec:
  clusterIP: None
  selector:
    app: nginx-sts
  ports:
  - port: 80
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: nginx-sts
spec:
  serviceName: nginx-headless
  replicas: 3
  selector:
    matchLabels:
      app: nginx-sts
  template:
    metadata:
      labels:
        app: nginx-sts
    spec:
      containers:
      - name: nginx
        image: registry.k8s.io/nginx-slim:0.21
        ports:
        - containerPort: 80
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 1Gi
```

**Reference**

- [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [StatefulSet Basics Tutorial](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/)

#### 实验：观察 Deployment vs DaemonSet vs StatefulSet 行为差异

```bash
kubectl apply -f daemonset.yaml
kubectl apply -f statefulset.yaml
kubectl get ds,sts,pods -o wide
kubectl delete pod nginx-sts-0    # StatefulSet 会按同名重建
kubectl scale sts nginx-sts --replicas=5  # 有序扩缩
```

### 3.2 持久化存储：PV、PVC、StorageClass

#### 核心概念

| 对象                             | 角色                                                 |
| -------------------------------- | ---------------------------------------------------- |
| **PV（PersistentVolume）**       | 集群级存储资源（NFS、云盘、Local 等）                |
| **PVC（PersistentVolumeClaim）** | 用户对存储的申请                                     |
| **StorageClass**                 | 存储「类」；支持**动态供给（Dynamic Provisioning）** |

```
PVC 申请 storage → StorageClass 触发 Provisioner → 自动创建 PV → 绑定 Pod
```

#### StorageClass 动态供给示例

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: standard
provisioner: kubernetes.io/no-provisioner   # 实验环境按实际 CSI 驱动替换
volumeBindingMode: WaitForFirstConsumer
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 2Gi
  storageClassName: standard
---
apiVersion: v1
kind: Pod
metadata:
  name: app-with-pvc
spec:
  containers:
  - name: app
    image: registry.k8s.io/nginx-slim:0.21
    volumeMounts:
    - name: data
      mountPath: /data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: data-pvc
```

#### 实验：数据写入后 Pod 重建仍保留

```bash
kubectl apply -f pvc-demo.yaml
kubectl exec -it app-with-pvc -- sh -c 'echo hello-pv > /data/test.txt'
kubectl delete pod app-with-pvc
# 重新创建 Pod 并挂载同一 PVC
kubectl apply -f pvc-demo.yaml
kubectl exec -it app-with-pvc -- cat /data/test.txt   # 应输出 hello-pv
```

**Reference**

- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
- [Dynamic Volume Provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/)
- [CSI（Container Storage Interface）](https://kubernetes-csi.github.io/docs/)
- [kubernetes-best-practices — 存储管理](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/master/doc/kubernetes-best-practices.md#4-存储管理)

### 3.3 调度策略入门

#### Scheduler 职责

过滤（Filter）→ 打分（Score）→ 绑定（Bind）

#### requests / limits

| 字段         | 含义                                        |
| ------------ | ------------------------------------------- |
| **requests** | 调度依据；保证的最小资源                    |
| **limits**   | 容器可用上限；超出可能被 OOMKill / Throttle |

#### nodeSelector / Node Affinity

```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd
```

#### Taints & Tolerations

- **Taint**：节点「排斥」某些 Pod
- **Toleration**：Pod「容忍」节点 Taint

```bash
# 给节点打污点（实验：专用节点）
kubectl taint nodes node1 dedicated=training:NoSchedule

# Pod 侧 toleration
```

```yaml
spec:
  tolerations:
  - key: dedicated
    operator: Equal
    value: training
    effect: NoSchedule
```

#### Pod Affinity / Anti-Affinity

- **Affinity**：Pod 与 Pod 部署在一起（如应用与缓存同节点）
- **Anti-Affinity**：Pod 分散到不同节点（高可用）

```yaml
spec:
  affinity:
    podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          labelSelector:
            matchLabels:
              app: hello-python
          topologyKey: kubernetes.io/hostname
```

**Reference**

- [Assign Pods to Nodes](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/)
- [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
- [Assign Pods to Nodes using Node Affinity](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)
- [Inter-pod affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity)
- [class-01 — K8S 调度](class-01-Kubernetes-Administration.md#lesson-05-k8s-schedule)

---

<a id="lesson-04-配置发布与运维概览"></a>

## Lesson 04：配置发布与运维概览

### 4.1 ConfigMap 与 Secret

#### ConfigMap — 非敏感配置

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_MODE: production
  config.yaml: |
    log_level: info
    max_conn: 100
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: demo-web:latest
        env:
        - name: APP_MODE
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: APP_MODE
        volumeMounts:
        - name: config-vol
          mountPath: /etc/config
          readOnly: true
      volumes:
      - name: config-vol
        configMap:
          name: app-config
          items:
          - key: config.yaml
            path: config.yaml
```

#### Secret — 敏感信息

Secret 类型 `kubernetes.io/dockerconfigjson` 专用于**私有镜像仓库认证**（见 4.1.1）。

```bash
kubectl create secret generic db-secret \
  --from-literal=username=appuser \
  --from-literal=password='S3cr3t!'
```

**Reference**

- [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [Secret](https://kubernetes.io/docs/concepts/configuration/secret/)
- [Configure a Pod to Use a ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)

<a id="411-私有镜像拉取imagepullsecrets重点"></a>

#### 4.1.1 私有镜像拉取：imagePullSecrets（重点）

从私有 Registry 拉镜像时，kubelet 需要认证凭据。完整流程：**构建 → push 到 Registry → 创建 Secret →
Pod/SA 引用**。

![镜像供应链与签名（Grafeas 概念，生产可配合准入控制）](images/chapter-3-1.png)

**步骤 1：创建 docker-registry Secret**

```bash
kubectl create secret docker-registry regcred \
  --docker-server=https://index.docker.io/v1/ \
  --docker-username=<USER> \
  --docker-password=<TOKEN> \
  --docker-email=<EMAIL>
```

**步骤 2：在 Pod/Deployment 中引用**

```yaml
spec:
  imagePullSecrets:
  - name: regcred
  containers:
  - name: app
    image: myregistry.example.com/myorg/myapp:v1.0.0
```

**步骤 3（推荐）：绑定到 ServiceAccount，避免每个 Pod 重复配置**

```bash
kubectl patch serviceaccount default -p \
  '{"imagePullSecrets": [{"name": "regcred"}]}'
```

此后使用该 ServiceAccount 的 Pod 会自动继承 `imagePullSecrets`。

**多 Registry 场景**

- 一个 Pod 可配置多个 `imagePullSecrets`
- 每个 Secret 可含多个 Registry 凭据；拉取时按 Registry 匹配

**K8S 1.33 新特性（了解）**

| 特性                         | 状态  | 说明                                                                              |
| ---------------------------- | ----- | --------------------------------------------------------------------------------- |
| **EnsureSecretPulledImages** | Alpha | 即使本地已有镜像，`IfNotPresent`/`Never` 策略下也强制校验凭据                     |
| **Secret-less image pulls**  | Alpha | kubelet 凭据插件可对接 SA Token/OIDC 获取短期 Registry 凭据                       |
| **containerd 2.x**           | —     | 节点侧镜像认证应优先走 K8S `imagePullSecrets`，而非 containerd config.toml 硬编码 |

**常见故障**

| 现象                              | 原因                             |
| --------------------------------- | -------------------------------- |
| `ImagePullBackOff`                | 凭据错误、镜像不存在、网络不通   |
| `FailedToRetrieveImagePullSecret` | Secret 不存在或 Namespace 不匹配 |

**Reference**

- [Pull an Image from a Private Registry](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/)
- [Images — Using a private registry](https://kubernetes.io/docs/concepts/containers/images/#using-a-private-registry)
- [Configure Service Accounts — Add ImagePullSecrets](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account)
- [KEP-2535: Ensure secret pulled images](https://github.com/kubernetes/enhancements/issues/2535)
- [CNCF: Smart Uses of imagePullSecrets](https://www.cncf.io/blog/2025/06/20/smart-uses-of-imagepullsecrets-in-kubernetes-cluster-with-serviceaccounts/)

### 4.2 发布策略与健康探针

#### 滚动更新与回滚

```bash
# 更新镜像
kubectl set image deployment/hello-python app=demo-web:v2

# 查看 rollout 状态
kubectl rollout status deployment/hello-python
kubectl rollout history deployment/hello-python

# 回滚
kubectl rollout undo deployment/hello-python
kubectl rollout undo deployment/hello-python --to-revision=2
```

Deployment 关键字段：

```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  minReadySeconds: 5
```

**Reference**

- [Rolling Update Deployment](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)
- [Deployment — Rolling Update](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-update-deployment)

#### 健康探针

| 探针               | 作用                             | 失败后果                             |
| ------------------ | -------------------------------- | ------------------------------------ |
| **startupProbe**   | 慢启动应用；通过前不执行其他探针 | 重启容器                             |
| **readinessProbe** | 是否接收流量                     | 从 Service 后端（EndpointSlice）移除 |
| **livenessProbe**  | 是否存活                         | 重启容器                             |

```yaml
containers:
- name: app
  image: demo-web:latest
  ports:
  - containerPort: 5000
  startupProbe:
    httpGet:
      path: /
      port: 5000
    failureThreshold: 30
    periodSeconds: 5
  readinessProbe:
    httpGet:
      path: /
      port: 5000
    initialDelaySeconds: 5
    periodSeconds: 10
  livenessProbe:
    httpGet:
      path: /
      port: 5000
    initialDelaySeconds: 15
    periodSeconds: 20
```

#### 原生 Sidecar 容器（K8S 1.33 Stable）

Sidecar（日志/代理/监控 Agent）在 1.33 成为稳定特性：在 `initContainers` 中设置
`restartPolicy: Always`。

```yaml
spec:
  initContainers:
  - name: log-shipper
    image: fluent/fluent-bit:3.0
    restartPolicy: Always    # Sidecar：与应用容器并行运行
  containers:
  - name: app
    image: demo-web:latest
```

**Reference**

- [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
- [Sidecar Containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) —
  **v1.33 stable**

### 4.3 常见排障思路

#### 通用排查流程

```
kubectl get <resource>
        ↓ 异常
kubectl describe <resource>     # 看 Events
        ↓
kubectl logs <pod> [-c <container>] [--previous]
        ↓ 仍不清楚
kubectl exec -it <pod> -- sh    # 进容器
        ↓ 节点/运行时问题
节点：crictl / journalctl -u kubelet
```

#### 典型现象与排查路径

| 现象                 | 可能原因                          | 排查命令                                                      |
| -------------------- | --------------------------------- | ------------------------------------------------------------- |
| **Pod Pending**      | 资源不足、污点、亲和性不满足      | `kubectl describe pod` → Events                               |
| **CrashLoopBackOff** | 应用启动失败、探针误杀            | `kubectl logs --previous`                                     |
| **ImagePullBackOff** | 镜像名错误、无凭据                | `describe pod` → Failed pull；检查 imagePullSecrets           |
| **Service 不可达**   | selector 不匹配、readiness 未通过 | `kubectl get endpointslices`；`kubectl get pod --show-labels` |
| **节点 NotReady**    | kubelet/CNI/磁盘压力              | `kubectl describe node`；节点 `systemctl status kubelet`      |

#### 节点侧调试

```bash
# 查看 kubelet 日志
journalctl -u kubelet -f

# CRI 视角
sudo crictl pods
sudo crictl ps -a
sudo crictl logs <container-id>

# 进入 Pod 网络命名空间抓包（高级）
PID=$(sudo crictl inspect -o go-template --template '{{.info.pid}}' <cid>)
sudo nsenter -t $PID -n tcpdump -i eth0 -nn port 80
```

**Reference**

- [Troubleshooting Applications](https://kubernetes.io/docs/tasks/debug/debug-application/)
- [Troubleshooting Clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/)
- [Debug Running Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/)

### 4.4 K8S 扩展生态概览（不展开实现）

#### 扩展机制全景

![OpenShift 与 K8S 扩展生态对比](images/openshift-k8s.svg)

```
Kubernetes 核心 API
        ↓
  ┌─────┴─────┬─────────────┬──────────────┐
  CRD      Operator    Ingress Ctrl    CSI Driver
  自定义资源   领域控制器    七层路由         存储插件
```

| 扩展                   | 说明                          | 举例                           |
| ---------------------- | ----------------------------- | ------------------------------ |
| **CRD**                | 扩展 API 类型                 | PrometheusRule、Certificate    |
| **Operator**           | CRD + Controller 封装运维逻辑 | mysql-operator、redis-operator |
| **Ingress Controller** | 实现 Ingress/Gateway 资源     | ingress-nginx、Traefik         |
| **CSI**                | 存储插件标准                  | 云盘 CSI、NFS CSI              |
| **CNI**                | 网络插件                      | Calico、Cilium、Flannel        |
| **Device Plugin**      | 硬件资源（GPU 等）            | nvidia-device-plugin           |

#### Gateway API（了解，替代 Ingress 的方向）

- **Ingress**：单一资源，注解驱动，功能有限
- **Gateway API**：角色分离（GatewayClass/Gateway/HTTPRoute），表达能力更强；生产级网关本课不展开

![Gateway / Ingress 概念对比](images/apigateway-servicediscover.png)

**Reference**

- [Extend Kubernetes — Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
- [Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
- [Ingress Controllers](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)
- [Gateway API](https://gateway-api.sigs.k8s.io/)

<a id="45-运维与可观测性概览"></a>

### 4.5 运维与可观测性概览

#### 4.5.1 可观测性三板斧

| 维度                | 说明           | K8S 常见方案                 |
| ------------------- | -------------- | ---------------------------- |
| **Metrics（指标）** | 数值型时序数据 | Prometheus + Grafana         |
| **Logs（日志）**    | 文本事件流     | Loki / ELK / EFK             |
| **Traces（链路）**  | 请求跨服务路径 | Jaeger / Tempo（本课不展开） |

与研发侧衔接：

- 应用暴露 `/metrics` 或依赖 Exporter
- 日志写 **stdout/stderr**（容器最佳实践），由平台采集

#### 4.5.2 Prometheus 监控（概览 + 轻量 Demo）

**Prometheus 定位**：Pull 模型时序数据库 + 告警规则引擎。Exporter 暴露 `/metrics`，Prometheus 定期
scrape。

```
Pod/Node ──metrics──▶ Exporter / cAdvisor / kube-state-metrics
                              ▲
                              │ pull
                         Prometheus ──▶ Grafana / Alertmanager
```

![Grafana 监控大盘示例](images/dashbord.png)

K8S 生态关键组件：

| 组件                    | 作用                                    |
| ----------------------- | --------------------------------------- |
| **cAdvisor**            | 节点/容器资源指标（kubelet 内置）       |
| **kube-state-metrics**  | K8S 对象状态指标（Deployment/Pod 数等） |
| **metrics-server**      | 资源用量 API（`kubectl top`）           |
| **Prometheus Operator** | 以 CRD 管理 Prometheus 实例（概念）     |

```bash
# 安装 metrics-server（以官方 manifest 为例，按集群版本选择 release）
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# 验证
kubectl top nodes
kubectl top pods -A
```

**告警思路（示例规则概念）**

```yaml
# PrometheusRule 示例（需 Prometheus Operator 或等价配置）
groups:
- name: pod-alerts
  rules:
  - alert: PodCrashLooping
    expr: rate(kube_pod_container_status_restarts_total[15m]) > 0
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "Pod {{ $labels.pod }} 频繁重启"
```

**Reference**

- [Prometheus](https://prometheus.io/docs/introduction/overview/)
- [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics)
- [metrics-server](https://github.com/kubernetes-sigs/metrics-server)
- [Prometheus Operator](https://prometheus-operator.dev/)

#### 4.5.3 日志收集方案（概念对比）

| 方案           | 组件                                        | 特点                                 |
| -------------- | ------------------------------------------- | ------------------------------------ |
| **EFK/ELK**    | Fluent Bit/Fluentd → Elasticsearch → Kibana | 检索能力强；存储成本较高             |
| **Loki 栈**    | Promtail/Fluent Bit → Loki → Grafana        | 与 Prometheus 标签模型一致；成本较低 |
| **云厂商日志** | 托管采集 + 存储                             | 运维简单；厂商绑定                   |

容器日志路径约定：

- 默认：`/var/log/pods/<namespace>_<pod>_<uid>/<container>/`
- 应用应写 stdout/stderr，避免写容器内本地文件

**Reference**

- [Logging Architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/)
- [Fluent Bit](https://fluentbit.io/)
- [Grafana Loki](https://grafana.com/docs/loki/latest/)

#### 4.5.4 生产级部署要点清单

| 维度           | 要点                                                        |
| -------------- | ----------------------------------------------------------- |
| **控制面**     | 多副本、etcd 定期备份、API Server 高可用                    |
| **工作节点**   | 合理 requests/limits；节点/Pod 反亲和                       |
| **应用发布**   | 滚动更新 + 探针 + 回滚预案；镜像版本 pin（不用 `:latest`）  |
| **配置与密钥** | ConfigMap/Secret 外置；私有镜像配置 imagePullSecrets        |
| **安全基线**   | **Pod Security Standards**（替代已移除的 PSP）；最小权限 SA |
| **存储**       | 有状态服务用 StatefulSet + 备份策略；PV 数据保护            |
| **入口**       | Ingress / LoadBalancer 选型；多环境 Namespace 隔离          |
| **交付形态**   | 裸集群 / 托管 K8S（EKS/ACK/CCE）/ KubeClipper 运维平台      |

![多区域 / 多集群交付形态（概念）](images/multi-region-caas.png)

![OpenShift 生产级 HA 部署参考](images/openshift-ha-deployment.png)

| 交付方式              | 适用           | 本课定位                       |
| --------------------- | -------------- | ------------------------------ |
| **实验集群**          | 学习、PoC      | KubeClipper 快速搭建           |
| **裸集群 + 运维平台** | 私有化、信创   | KubeClipper / 自建             |
| **托管 K8S**          | 公有云、省运维 | ACK / EKS / CCE 等             |
| **轻量发行版**        | 边缘 / CI      | K3s（见 class-03，本课不展开） |

**4C 安全模型（Code / Container / Cluster / Cloud）**

![CNCF 4C 安全层级](images/what-is-security.png)

![4C 安全模型详图](images/4c-1.png)

生产环境安全是持续过程：从镜像供应链（Harbor 扫描、固定 tag）、运行时（PSS
baseline/restricted）、集群（RBAC 概览、etcd 备份）到云平台（网络隔离）逐层加固。详见
[class-04 安全纲要](class-04-Kubernetes-Security-Specialist.md)。

**Pod Security Standards（PSS）— 替代 PSP**

自 1.25 起 PSP 已移除；使用内置 **Pod Security Admission**：

```bash
# 为 Namespace 设置 baseline 策略（示例）
kubectl label namespace dev \
  pod-security.kubernetes.io/enforce=baseline \
  pod-security.kubernetes.io/warn=restricted \
  pod-security.kubernetes.io/audit=restricted
```

| 级别           | 说明                          |
| -------------- | ----------------------------- |
| **privileged** | 无限制                        |
| **baseline**   | 阻止已知特权升级              |
| **restricted** | 最严格；符合 Pod 安全最佳实践 |

**Reference**

- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
- [Backup etcd](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/#backing-up-an-etcd-cluster)
- [kubernetes-best-practices — 安全相关](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/master/doc/kubernetes-best-practices.md#6-安全相关)
- [class-04 — Kubernetes 安全](class-04-Kubernetes-Security-Specialist.md)

#### 4.5.5 AIOps 与智能运维（概览）

> 边缘与云协同场景下，AIOps 可结合 Prometheus 指标 + 日志平台 + K8S Events 作为 LLM
> 上下文，辅助告警根因分析与 Runbook 检索。参见
> [边缘智算与运维](https://gitee.com/wu-wen-xiang/lab-kubernetes/blob/master/doc/mec-edge-and-ai.md)。

**典型适用场景**

| 场景                 | 说明                           |
| -------------------- | ------------------------------ |
| 告警聚合与根因解释   | 将多条 Prometheus 告警关联分析 |
| 日志/事件摘要        | 从大量 Pod 日志中提取关键异常  |
| Runbook / 知识库问答 | 运维文档、故障手册智能检索     |
| 变更影响分析         | 结合发布记录与指标波动         |

**边界与原则**

- ✅ 适宜：信息整理、模式识别、排查建议、文档生成
- ❌ 不宜：未经人工复核的**自动修复**（尤其生产环境 exec/删除/扩缩）
- 数据衔接：Prometheus 指标 + 日志平台 + K8S Events 作为 LLM 上下文

**可选 Demo 思路**

```text
输入：kubectl describe pod 的 Events + 容器 logs 片段
输出：大模型解读「镜像拉取失败 → 检查 imagePullSecrets / 镜像 tag」
```

### 4.6 综合 Demo：完整发布闭环

```bash
# === 1. 构建镜像 ===
docker build -t demo-web:v2 .
docker tag demo-web:v2 registry.example.com/training/demo-web:v2
docker push registry.example.com/training/demo-web:v2

# === 2. 创建拉取凭据 ===
kubectl create secret docker-registry regcred \
  --docker-server=registry.example.com \
  --docker-username=<user> --docker-password=<pass>

kubectl patch sa default -p '{"imagePullSecrets":[{"name":"regcred"}]}'

# === 3. 声明式部署（含 ConfigMap + 探针）===
kubectl apply -f configmap.yaml -f deployment-v2.yaml -f service.yaml

# === 4. 访问验证 ===
curl http://<node-ip>:31000/

# === 5. 滚动更新 ===
kubectl set image deployment/hello-python app=registry.example.com/training/demo-web:v2
kubectl rollout status deployment/hello-python

# === 6. 回滚 ===
kubectl rollout undo deployment/hello-python

# === 7. 节点侧对照 ===
ssh <node>
sudo crictl ps | grep hello-python
sudo crictl logs <container-id>
```

### 4.7 研发场景收束：何时引入 K8S

| 适合引入 K8S                    | 暂不必引入                       |
| ------------------------------- | -------------------------------- |
| 多服务、需弹性扩缩              | 单体小工具、访问量极低           |
| 多环境（dev/test/prod）一致交付 | 团队无运维能力、无学习预算       |
| 需滚动发布、自愈                | 强依赖本地 GUI/桌面应用          |
| 已有容器化应用                  | 应用无法容器化（极少数遗留系统） |

实验环境容器化、工具服务上云是常见第一步；**不必为了「云原生」而云原生**。

---

## 附录 A：kubectl 速查

```bash
# 资源查看
kubectl get all -n <ns>
kubectl api-resources
kubectl explain deployment.spec

# 调试
kubectl describe <type> <name>
kubectl logs -f <pod> -c <container>
kubectl exec -it <pod> -- sh
kubectl port-forward svc/<name> 8080:80

# 发布
kubectl apply -f .
kubectl diff -f .
kubectl rollout status deploy/<name>
kubectl rollout undo deploy/<name>

# 节点
kubectl cordon <node>
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data
kubectl uncordon <node>
```

---

## 附录 B：版本变更速查（过时 → 现行）

### Kubernetes 1.33+ 值得了解的新特性

| 特性                         | 状态                            | 与本课关系                                                           |
| ---------------------------- | ------------------------------- | -------------------------------------------------------------------- |
| **Sidecar Containers**       | Stable (1.33)                   | 日志/代理 Sidecar 用 `initContainers` + `restartPolicy: Always`      |
| **EnsureSecretPulledImages** | Alpha                           | 私有镜像在 `IfNotPresent` 时也强制校验凭据                           |
| **Secret-less image pulls**  | Alpha                           | SA Token/OIDC 短期 Registry 凭据                                     |
| **EndpointSlice 默认**       | GA                              | Service 后端发现机制；`Endpoints` 逐步弃用                           |
| **Pod Security Admission**   | GA                              | 替代 PSP；Namespace 标签 enforce/warn/audit                          |
| **User Namespaces**          | Beta（1.33 起默认开启特性门控） | Pod 设置 `hostUsers: false` 可 opt-in；需 containerd 2.0+ 等节点条件 |
| **containerd 2.x**           | 运行时                          | 镜像认证优先走 K8S `imagePullSecrets`                                |

**Reference**

- [Kubernetes v1.33: Octarine](https://kubernetes.io/blog/2025/04/23/kubernetes-v1-33-release/)
- [Kubernetes Enhancements (KEPs)](https://github.com/kubernetes/enhancements)

### 过时 → 现行对照

| 过时内容                                    | 现行替代                                 | 说明                    |
| ------------------------------------------- | ---------------------------------------- | ----------------------- |
| dockershim                                  | containerd / CRI-O                       | 1.24+ 已移除            |
| Pod Security Policy (PSP)                   | Pod Security Standards + Admission       | 1.25+ 已移除            |
| `kubectl run` 自动创建 Deployment           | 显式 YAML 或 `kubectl create deployment` | 行为已变更              |
| Endpoints（默认）                           | EndpointSlice                            | 对用户基本透明          |
| 节点 `docker ps` 查 Pod                     | `crictl ps`                              | 与 kubelet 视角一致     |
| containerd config.toml 硬编码 registry auth | K8S imagePullSecrets                     | containerd 2.x 推荐做法 |
| Ingress 注解堆砌                            | Gateway API（演进方向）                  | 本课仅概览              |

---

## 附录 C：Reference 汇总

### 官方文档

| 主题                    | 链接                                                                                                                               |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Kubernetes 文档（中文） | [https://kubernetes.io/zh-cn/docs/home/](https://kubernetes.io/zh-cn/docs/home/)                                                   |
| 概念 — 工作负载         | [https://kubernetes.io/docs/concepts/workloads/](https://kubernetes.io/docs/concepts/workloads/)                                   |
| 概念 — 存储             | [https://kubernetes.io/docs/concepts/storage/](https://kubernetes.io/docs/concepts/storage/)                                       |
| 概念 — 调度             | [https://kubernetes.io/docs/concepts/scheduling-eviction/](https://kubernetes.io/docs/concepts/scheduling-eviction/)               |
| 概念 — 安全             | [https://kubernetes.io/docs/concepts/security/](https://kubernetes.io/docs/concepts/security/)                                     |
| Tasks — 配置 Pod        | [https://kubernetes.io/docs/tasks/configure-pod-container/](https://kubernetes.io/docs/tasks/configure-pod-container/)             |
| Release Notes           | [https://kubernetes.io/releases/](https://kubernetes.io/releases/)                                                                 |
| v1.33 发布说明          | [https://kubernetes.io/blog/2025/04/23/kubernetes-v1-33-release/](https://kubernetes.io/blog/2025/04/23/kubernetes-v1-33-release/) |

### 容器与运行时

| 主题        | 链接                                                                                         |
| ----------- | -------------------------------------------------------------------------------------------- |
| Docker 文档 | [https://docs.docker.com/](https://docs.docker.com/)                                         |
| containerd  | [https://containerd.io/](https://containerd.io/)                                             |
| nerdctl     | [https://github.com/containerd/nerdctl](https://github.com/containerd/nerdctl)               |
| crictl      | [https://github.com/kubernetes-sigs/cri-tools](https://github.com/kubernetes-sigs/cri-tools) |
| OCI         | [https://opencontainers.org/](https://opencontainers.org/)                                   |

### 集群管理

| 主题        | 链接                                                                                                                                             |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| KubeClipper | [https://kubeclipper.io/](https://kubeclipper.io/)                                                                                               |
| kubeadm     | [https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/) |

### 可观测与安全

| 主题                     | 链接                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| Prometheus               | [https://prometheus.io/docs/](https://prometheus.io/docs/)                                                                     |
| Grafana Loki             | [https://grafana.com/docs/loki/latest/](https://grafana.com/docs/loki/latest/)                                                 |
| CNCF Security Whitepaper | [https://www.cncf.io/reports/cloud-native-security-whitepaper/](https://www.cncf.io/reports/cloud-native-security-whitepaper/) |
| CIS Kubernetes Benchmark | [https://www.cisecurity.org/benchmark/kubernetes](https://www.cisecurity.org/benchmark/kubernetes)                             |

### 本仓库相关课程

| 课程                      | 链接                                                                                     |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| Kubernetes-Administration | [class-01-Kubernetes-Administration.md](class-01-Kubernetes-Administration.md)           |
| Kubernetes-Development    | [class-02-Kubernetes-Development.md](class-02-Kubernetes-Development.md)                 |
| 边缘容器云解决方案        | [class-03-Kubernetes-Edge-Solutions.md](class-03-Kubernetes-Edge-Solutions.md)           |
| Kubernetes 安全           | [class-04-Kubernetes-Security-Specialist.md](class-04-Kubernetes-Security-Specialist.md) |
