# 容器化技术与 K8S 详解及应用 — PPT 大纲

> **对应讲义**：[class-05-容器化技术与K8S详解及应用.md](class-05-容器化技术与K8S详解及应用.md)\
> **课程形态**：2 天 × 6 小时，理论 + Demo 穿插，实操约 50%\
> **PPT 定位**：课堂投影主视觉；细节与命令以讲义 / 终端 Demo 为准，**PPT 不堆代码**

---

## 一、总体结构

### 1.1 大章节（4 章 + 开场/收束）

| 序号  | 大章节               | 对应讲义                     | 建议页数 | 授课时段            |
| ----- | -------------------- | ---------------------------- | -------: | ------------------- |
| **0** | 开场与课程总览       | Prefix / Catalog / Checklist |    **6** | 第 1 天开场 ~15 min |
| **1** | 容器与运行时         | Lesson 01（1.1–1.6）         |   **24** | 第 1 天上午         |
| **2** | K8S 架构与首批部署   | Lesson 02（2.1–2.7）         |   **28** | 第 1 天下午         |
| **3** | 工作负载、存储与调度 | Lesson 03（3.1–3.3）         |   **18** | 第 2 天上午         |
| **4** | 配置发布与运维概览   | Lesson 04（4.1–4.7）         |   **22** | 第 2 天下午         |
| **5** | 收束与附录速查       | Checklist / 附录 A–B         |    **4** | 课程结束前 ~10 min  |
|       | **合计**             |                              |  **102** |                     |

> **页数说明**：102 页对应 12 小时课堂；按「每页 3–5 分钟（含 Demo 切换）」估算，与 50%
> 实操节奏匹配。若时间紧张，可压缩第 4 章运维概览（见文末「精简方案」→ **82 页**）。

### 1.2 小章节（与讲义一一对应）

```
0  开场与课程总览
   0.1  封面
   0.2  目录
   0.3  课程定位与目标
   0.4  本课特点 / 不展开范围
   0.5  五条主线
   0.6  两天培训总览

1  容器与运行时（Lesson 01）
   1.1  部署方式演进
   1.2  容器 vs 虚拟机
   1.3  Linux 底层：Namespace 与 Cgroups
   1.4  OCI 与镜像标准
   1.5  Docker 架构与核心对象
       1.5.1  镜像与交付（Dockerfile 最佳实践）
       1.5.2  Docker 网络与存储要点
   1.6  从 Docker 到 containerd 生态
       1.6.1  K8S 为何以 containerd 为默认运行时
       1.6.2  nerdctl / crictl / ctr 工具对比
   【Lab】Docker Quick Start + 构建 Web 镜像
   【Lab】节点侧 crictl 对照

2  K8S 架构与首批部署（Lesson 02）
   2.1  K8S 解决什么问题
   2.2  K8S 不解决什么问题
   2.3  K8S 架构概览
   2.4  声明式模型与 Controller 原理 ★
   2.5  KubeClipper 快速搭建实验集群
   2.6  kubectl 与 YAML 基础
   2.7  核心对象：Namespace / Pod / Deployment / Service
   【Lab】KubeClipper 建集群
   【Lab】完整部署 Web 应用

3  工作负载、存储与调度（Lesson 03）
   3.1  DaemonSet 与 StatefulSet
   3.2  持久化存储：PV / PVC / StorageClass
   3.3  调度策略入门
   【Lab】三种工作负载行为对比
   【Lab】PVC 数据持久化 Demo

4  配置发布与运维概览（Lesson 04）
   4.1  ConfigMap 与 Secret（含 imagePullSecrets）
   4.2  发布策略与健康探针
   4.3  常见排障思路
   4.4  K8S 扩展生态概览
   4.5  运维与可观测性概览
       4.5.1  可观测性三板斧
       4.5.2  Prometheus 监控
       4.5.3  日志收集方案
       4.5.4  生产级部署要点
       4.5.5  AIOps 与智能运维
   4.6  综合 Demo：完整发布闭环
   4.7  研发场景收束

5  收束
   5.1  课程收获 Checklist
   5.2  版本变更速查（过时 → 现行）
   5.3  延伸阅读 / Q&A
   5.4  致谢
```

---

## 二、PPT 设计规范（本课专用）

### 2.1 版式与字数

| 规则     | 建议值              | 说明                                |
| -------- | ------------------- | ----------------------------------- |
| 每页要点 | **≤ 4 条**          | 超过则拆页                          |
| 每条字数 | **≤ 28 字**         | 投影 3m 距离可读                    |
| 标题字数 | **≤ 20 字**         | 一行内显示                          |
| 正文字号 | 16–18 pt            | 标题 24–28 pt                       |
| 字体     | 微软雅黑 / 思源黑体 | 中英文混排统一                      |
| 代码     | **不放完整 YAML**   | 最多 3–5 行关键字段；完整清单见讲义 |

### 2.2 版式类型（建议模板 5 种）

| 类型                | 用途                                | 文字 : 图 比例                   |
| ------------------- | ----------------------------------- | -------------------------------- |
| **封面 / 章节分隔** | 大章节切换                          | 纯标题                           |
| **图文页**          | 架构、原理、对比                    | 图 60% + 要点 2 条               |
| **双栏对比页**      | VM vs 容器、声明式 vs 命令式        | 左 3 点 + 右 3 点                |
| **流程页**          | Controller 调谐、排障路径、发布闭环 | 流程图 70% + 注释 1 条           |
| **Lab 引导页**      | 实验开始/结束                       | 目标 2 条 + 步骤编号（无长命令） |

### 2.3 配图原则

- **一图一义**：每页最多 1 张主图；对比类可用左右双图
- **优先复用讲义插图**：见 [附录：插图索引](#附录插图索引)
- **架构图 > 截图**：K8S 组件、CRI 调用链用矢量/高清架构图
- **Demo 页用终端截图**：仅展示关键输出（如 `kubectl get pods` 结果），命令口述或切终端
- **标注高亮**：用色块/箭头标出当页讲解焦点（如 API Server、CRI endpoint）

### 2.4 授课节奏

| 时段     | PPT 角色            | 建议                  |
| -------- | ------------------- | --------------------- |
| 概念讲解 | 投影主视觉          | 2–4 min/页            |
| Demo 前  | Lab 引导页（1 页）  | 说明目标与验收标准    |
| Demo 中  | **切终端 / 控制台** | PPT 停在 Lab 页或黑屏 |
| Demo 后  | 小结页（可选 1 页） | 3 条「你应观察到…」   |
| 章节末   | 分隔页 + 3 条收束   | 承上启下              |

### 2.5 通用最佳实践

1. **6×6 法则**：每页不超过 6 行、每行不超过 6 词（中文按「条」计，本课收紧为 4 条）
2. **结论先行**：标题即观点（如「生产环境不要裸跑 Pod」），正文为支撑
3. **动画克制**：仅用于流程分步（Reconcile 循环）；避免逐字飞入
4. **色彩一致**：强调色 1 种（如 K8S 蓝）；告警/错误用红，成功用绿
5. **版本标注**：涉及 1.33 新特性页脚注「K8S 1.33+」
6. **讲义互补**：PPT 讲「为什么」，讲义/Demo 讲「怎么做」
7. **备份纯 PDF**：防字体/动画兼容问题

---

## 三、逐页大纲（102 页）

> 格式：**Pxx** | 版式 | 标题 | 要点（≤4）| 配图\
> ★ = 重点页；🔬 = Demo 引导页（讲解后切终端）

---

### 第 0 章 · 开场与课程总览（6 页）

| 页码 | 版式 | 标题                        | 页面要点                                                                                 | 配图                     |
| ---: | ---- | --------------------------- | ---------------------------------------------------------------------------------------- | ------------------------ |
|  P01 | 封面 | 容器化技术与 K8S 详解及应用 | 副标题：2 天实战培训 · K8S 1.30+                                                         | 品牌 Logo / K8S 官方图   |
|  P02 | 目录 | 课程目录                    | ① 容器与运行时 ② K8S 架构与部署 ③ 工作负载与存储 ④ 运维与可观测                          | —                        |
|  P03 | 内容 | 课程定位与目标              | 建立容器/K8S 正确认知；以「会用」为主；完成从镜像到上线的闭环                            | —                        |
|  P04 | 双栏 | 本课特点 / 不展开           | 左：夯实基础、面向应用、KubeClipper 10 分钟建集群 / 右：不展开 Mesh、RBAC 深度、CKA 辅导 | —                        |
|  P05 | 内容 | 五条主线                    | ① 容器运行时 ② 镜像交付 ③ K8S 核心 ④ 应用深化 ⑤ 运维可观测                               | 五条主线流程图（可手绘） |
|  P06 | 内容 | 两天培训总览                | 第 1 天：容器 + K8S 部署；第 2 天：工作负载 + 运维；实操约 50%                           | 2×2 时间表               |

---

### 第 1 章 · 容器与运行时（24 页）

| 页码 | 版式 | 标题                       | 页面要点                                                                       | 配图                                                                |
| ---: | ---- | -------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
|  P07 | 章节 | **01 · 容器与运行时**      | 第 1 天 · 上午                                                                 | —                                                                   |
|  P08 | 图文 | 1.1 部署方式演进           | 物理机 → VM → 容器 → K8S 编排；密度↑ 启动↓ 一致性↑                             | `container-evolution.png`                                           |
|  P09 | 内容 | 各阶段典型问题             | 物理机：环境不一致；VM：镜像大启动慢；容器：需编排平台                         | 同上（可选时间轴）                                                  |
|  P10 | 双栏 | 1.2 容器 vs 虚拟机 ★       | 左：隔离/启动/镜像/密度对比表（4 行）/ 右：VM=Guest OS；容器=Namespace+Cgroups | `katacontainers_traditionalvskata_diagram.jpg`                      |
|  P11 | 内容 | 何时仍需要 VM？            | 不同内核/OS；硬件级隔离合规；安全容器 Kata/gVisor                              | Kata 对比图（续）                                                   |
|  P12 | 图文 | 1.3 Namespace 与 Cgroups ★ | Namespace：视图隔离（PID/Net/Mount…）；Cgroups：CPU/内存限制                   | `kernel-user-mode.png`                                              |
|  P13 | 内容 | Pod 与 Namespace 关系      | Pod 内容器共享 Network/IPC/UTS；pause 容器；requests/limits → Cgroups          | Pod 示意图（可引用官方）                                            |
|  P14 | 内容 | 1.4 OCI 与镜像标准         | Image Spec + Runtime Spec；runC 为参考实现                                     | OCI Logo / 分层示意                                                 |
|  P15 | 图文 | 1.5 Docker 架构            | Client → dockerd → containerd → runc；四大对象：镜像/容器/仓库/Dockerfile      | `docker-arch.png`                                                   |
|  P16 | 图文 | Docker 底层技术            | Namespace + Cgroups + Union FS + libcontainer                                  | `docker-undertech.png`                                              |
|  P17 | 内容 | 1.5.1 Dockerfile 最佳实践  | 多阶段构建；固定 tag；非 root；配置外置；日志写 stdout                         | 多阶段构建示意（简图）                                              |
|  P18 | 图文 | 镜像供应链                 | 构建 → push Registry → K8S 拉取；Harbor 私有仓库                               | `harbor-arch.png`（lab-kubernetes）                                 |
|  P19 | 🔬   | Lab：Docker Quick Start    | 目标：跑通 hello-world；验收：images/ps/logs/exec                              | —                                                                   |
|  P20 | 🔬   | Lab：构建 demo-web 镜像    | 目标：Flask 应用容器化；验收：curl 本地 5001 端口                              | 终端截图（可选）                                                    |
|  P21 | 图文 | Docker 网络与存储          | Bridge 默认；Host 模式；Volume 持久化 → K8S PV/PVC                             | `bridge_network.jpeg`                                               |
|  P22 | 章节 | **02 · containerd 生态**   | K8S 运行时切换                                                                 | —                                                                   |
|  P23 | 流程 | 1.6.1 CRI 调用链 ★         | Orchestration → CRI → OCI Runtime → Kernel                                     | `k8s-CRI-OCI-docker.png`                                            |
|  P24 | 图文 | containerd 架构演进        | 1.0 独立 cri 进程 → 1.1+ CRI 内嵌                                              | `k8s-containerd-1-0.png` + `k8s-containerd-1-1.png`（分两页或并列） |
|  P25 | 内容 | dockershim 已移除          | 1.24+ 不再内置；生产用 containerd/CRI-O                                        | 变更对照表（3 行）                                                  |
|  P26 | 图文 | 1.6.2 工具对比             | ctr：底层调试；nerdctl：Docker 兼容；crictl：节点排障 ★                        | `k8s-cri-tools.png` / `k8s-containerd-tools.png`                    |
|  P27 | 双栏 | docker vs crictl           | 左：docker ps/logs / 右：crictl ps/pods/inspectp                               | 命令对照表（各 4 行）                                               |
|  P28 | 内容 | crictl 配置要点            | endpoint: containerd.sock；命名空间 k8s.io                                     | —                                                                   |
|  P29 | 🔬   | Lab：节点 crictl 对照      | 目标：kubectl 创建 Pod → 节点 crictl 查看；验收：Pod/容器 ID 一致              | —                                                                   |
|  P30 | 内容 | 第 1 天上午收束            | 容器原理清晰；Docker 会构建；理解 CRI/containerd 分工                          | —                                                                   |

---

### 第 2 章 · K8S 架构与首批部署（28 页）

| 页码 | 版式 | 标题                    | 页面要点                                                                   | 配图                                |
| ---: | ---- | ----------------------- | -------------------------------------------------------------------------- | ----------------------------------- |
|  P31 | 章节 | **03 · K8S 架构与部署** | 第 1 天 · 下午                                                             | —                                   |
|  P32 | 内容 | 2.1 K8S 解决什么问题 ★  | 编排、自愈、扩缩、服务发现、滚动发布、配置外置                             | —                                   |
|  P33 | 内容 | 云原生视角              | 业务无关的基础运维；API + 微服务 + 容器化                                  | —                                   |
|  P34 | 内容 | 2.2 K8S 不解决什么      | 身份体系、Mesh 限流、完整监控平台、业务逻辑本身                            | —                                   |
|  P35 | 图文 | 2.3 K8S 架构概览 ★      | 控制面：API Server / etcd / Scheduler / CM；节点：kubelet / proxy / 运行时 | `k8s-architecture.png`              |
|  P36 | 图文 | Borg → Kubernetes       | 编排思想渊源；架构与 API 独立设计                                          | `borg-arch.png`                     |
|  P37 | 双栏 | 2.4 声明式 vs 命令式 ★  | 左：kubectl run（做什么）/ 右：kubectl apply（期望状态）                   | —                                   |
|  P38 | 流程 | Controller 调谐循环 ★   | YAML → API Server → etcd → Controller → Reconcile                          | `kubernetes-co-loop.webp`           |
|  P39 | 图文 | Informer 边缘触发       | 对比轮询；Deployment/RS/Service Controller 举例                            | `kubernetes-controller-trigger.png` |
|  P40 | 内容 | 不要裸跑 Pod            | 无副本保障、无滚动更新、节点故障即丢失                                     | —                                   |
|  P41 | 内容 | 2.5 KubeClipper 简介    | 基于 kubeadm；Web + kcctl；约 10 分钟建集群                                | KubeClipper Logo                    |
|  P42 | 双栏 | KubeClipper vs 同类     | 图形化、多集群、离线安装 vs Sealos/KubeKey                                 | 对比表（5 行）                      |
|  P43 | 🔬   | Lab：KubeClipper 建集群 | 目标：单节点集群 Running；验收：kubectl get nodes                          | 控制台截图                          |
|  P44 | 内容 | 2.6 kubectl 常用命令    | get/describe/logs/exec/apply/explain                                       | —                                   |
|  P45 | 内容 | K8S 资源通用结构        | apiVersion / kind / metadata / spec / status                               | YAML 骨架（5 行）                   |
|  P46 | 内容 | YAML 语法要点           | 空格缩进；列表用 `-`；特殊字符加引号                                       | —                                   |
|  P47 | 内容 | 2.7 Namespace           | 逻辑隔离；不同 ns 可同名资源                                               | —                                   |
|  P48 | 内容 | Pod — 最小调度单元      | 一 Pod 可多容器；共享 Network NS                                           | Pod 图标                            |
|  P49 | 内容 | Deployment ★            | 副本管理、滚动更新、回滚；生产首选                                         | —                                   |
|  P50 | 图文 | Service 类型            | ClusterIP / NodePort / LoadBalancer 场景对比                               | `ingress-service.drawio.svg`        |
|  P51 | 内容 | Service DNS             | `<svc>.<ns>.svc.cluster.local`；EndpointSlice 默认                         | —                                   |
|  P52 | 🔬   | Lab：部署 Web 应用      | 目标：Deployment + NodePort Service；验收：curl 节点 IP                    | —                                   |
|  P53 | 流程 | 首次上线数据流          | 镜像 → YAML → Controller → Pod → Service → 访问                            | —                                   |
|  P54 | 内容 | 第 1 天收束 ★           | 运行时清晰；集群可用；YAML+Controller；完成首次上线                        | Checklist 4 条                      |
|  P55 | 内容 | 第 1 天 Q&A 预留        | （空白互动页或常见问题）                                                   | —                                   |
|  P56 | 内容 | 过渡：明天预告          | 工作负载选型、持久化、配置发布、运维概览                                   | —                                   |
|  P57 | 内容 | 课后练习（可选）        | 调整副本数；describe Pod 看 Events；节点 crictl 对照                       | —                                   |
|  P58 | 内容 | 讲义与实验环境          | KubeClipper 控制台地址；kubeconfig 获取方式                                | —                                   |

> **说明**：P55–P58 为缓冲页，时间充裕可展开 Q&A；紧张则合并为 1 页，总页数 **98**。

---

### 第 3 章 · 工作负载、存储与调度（18 页）

| 页码 | 版式 | 标题                    | 页面要点                                                         | 配图                  |
| ---: | ---- | ----------------------- | ---------------------------------------------------------------- | --------------------- |
|  P59 | 章节 | **04 · 工作负载与存储** | 第 2 天 · 上午                                                   | —                     |
|  P60 | 图文 | 3.1 工作负载选型 ★      | Deployment：无状态；DaemonSet：每节点一个；StatefulSet：稳定标识 | `kubernetes-arch.png` |
|  P61 | 内容 | DaemonSet 典型场景      | 日志采集、监控 Agent、CNI；tolerations: Exists                   | —                     |
|  P62 | 内容 | StatefulSet 关键特性    | 稳定 Pod 名/DNS；Headless Service；volumeClaimTemplates          | —                     |
|  P63 | 🔬   | Lab：三种工作负载对比   | 目标：观察 DS/STS/Deploy 行为；验收：删 STS Pod 同名重建         | —                     |
|  P64 | 流程 | 3.2 存储对象关系        | PVC 申请 → StorageClass → PV 绑定 → Pod 挂载                     | PV/PVC 示意图         |
|  P65 | 内容 | PV / PVC / StorageClass | 静态供给 vs 动态供给；accessModes                                | —                     |
|  P66 | 🔬   | Lab：PVC 数据持久化     | 目标：写文件 → 删 Pod → 重建后数据仍在                           | —                     |
|  P67 | 内容 | 3.3 Scheduler 职责      | Filter → Score → Bind                                            | —                     |
|  P68 | 双栏 | requests vs limits      | requests：调度依据；limits：上限/OOMKill                         | —                     |
|  P69 | 内容 | Taints & Tolerations    | 节点排斥 Pod；专用节点、GPU 节点场景                             | —                     |
|  P70 | 内容 | Node Affinity           | 节点亲和：disktype=ssd 等                                        | —                     |
|  P71 | 内容 | Pod Anti-Affinity       | 副本分散到不同节点；高可用                                       | —                     |
|  P72 | 🔬   | Lab：调度策略 Demo      | 目标：污点容忍 + 反亲和各验证一次                                | —                     |
|  P73 | 内容 | 第 2 天上午收束         | 会选工作负载；理解 PV/PVC；掌握调度入门                          | —                     |
|  P74 | 章节 | **05 · 配置与运维**     | 第 2 天 · 下午                                                   | —                     |
|  P75 | 内容 | 下午议程预览            | ConfigMap/Secret → 发布探针 → 排障 → 可观测 → AIOps              | —                     |
|  P76 | 内容 | （缓冲 / 签到回顾）     | 昨日回顾 3 条                                                    | —                     |

> **说明**：P76 为可选缓冲；合并 P75–P76 则本章 **17 页**。

---

### 第 4 章 · 配置发布与运维概览（22 页）

| 页码 | 版式 | 标题                         | 页面要点                                            | 配图                             |
| ---: | ---- | ---------------------------- | --------------------------------------------------- | -------------------------------- |
|  P77 | 内容 | 4.1 ConfigMap                | 非敏感配置；env 或 volume 注入                      | —                                |
|  P78 | 内容 | Secret 与 imagePullSecrets ★ | 敏感信息；私有镜像：Secret → SA → Pod               | `chapter-3-1.png`                |
|  P79 | 内容 | 1.33 镜像拉取新特性          | EnsureSecretPulledImages；Secret-less pulls（了解） | —                                |
|  P80 | 内容 | 4.2 滚动更新与回滚           | set image；rollout status/history/undo              | —                                |
|  P81 | 内容 | 健康探针 ★                   | startup / readiness / liveness 区别与失败后果       | 探针对比表                       |
|  P82 | 内容 | Sidecar 容器（1.33 Stable）  | initContainers + restartPolicy: Always              | —                                |
|  P83 | 流程 | 4.3 排障通用流程 ★           | get → describe → logs → exec → 节点 crictl          | 流程图                           |
|  P84 | 内容 | 典型现象速查                 | Pending / CrashLoop / ImagePull / Service 不可达    | 表格 4 行                        |
|  P85 | 图文 | 4.4 扩展生态全景             | CRD / Operator / Ingress / CSI / CNI                | `openshift-k8s.svg`              |
|  P86 | 内容 | Gateway API（了解）          | 替代 Ingress 方向；本课不展开                       | `apigateway-servicediscover.png` |
|  P87 | 内容 | 4.5.1 可观测性三板斧         | Metrics / Logs / Traces                             | —                                |
|  P88 | 流程 | 4.5.2 Prometheus 概览        | Pull 模型；Exporter；cAdvisor / kube-state-metrics  | Prometheus 架构简图              |
|  P89 | 内容 | metrics-server               | kubectl top nodes/pods                              | —                                |
|  P90 | 双栏 | 4.5.3 日志方案对比           | EFK/ELK vs Loki；stdout 约定                        | —                                |
|  P91 | 内容 | 4.5.4 生产部署要点 ★         | 控制面 HA；探针+回滚；PSS；etcd 备份                | `multi-region-caas.png`          |
|  P92 | 图文 | 4C 安全模型                  | Code / Container / Cluster / Cloud                  | `what-is-security.png`           |
|  P93 | 内容 | Pod Security Standards       | privileged / baseline / restricted；替代 PSP        | —                                |
|  P94 | 内容 | 4.5.5 AIOps 概览             | 告警聚合、日志摘要、Runbook 问答；不宜自动修复      | —                                |
|  P95 | 🔬   | Lab：综合发布闭环            | 构建→部署→配置→更新→回滚→crictl 对照                | 七步流程图                       |
|  P96 | 双栏 | 4.7 何时引入 K8S             | 适合：多服务、多环境、需自愈 / 不必：单体小工具     | —                                |
|  P97 | 内容 | 交付形态选型                 | 实验：KubeClipper；生产：托管 K8S / 裸集群+平台     | —                                |
|  P98 | 内容 | 第 2 天收束                  | 完整发布闭环；监控日志认知；扩展生态全景            | —                                |

---

### 第 5 章 · 收束（4 页）

| 页码 | 版式 | 标题               | 页面要点                                                | 配图        |
| ---: | ---- | ------------------ | ------------------------------------------------------- | ----------- |
|  P99 | 内容 | 课程收获 Checklist | 10 条能力自测（来自讲义）                               | —           |
| P100 | 内容 | 版本变更速查       | dockershim→containerd；PSP→PSS；Endpoints→EndpointSlice | 对照表      |
| P101 | 内容 | 延伸阅读           | class-01~04；lab-kubernetes 最佳实践                    | 二维码/链接 |
| P102 | 致谢 | 谢谢 & Q&A         | 联系方式；讲义仓库                                      | —           |

---

## 四、页数汇总

| 大章节             |   小章节数 | 页码范围     |    页数 |
| ------------------ | ---------: | ------------ | ------: |
| 0 · 开场与总览     |          6 | P01–P06      |       6 |
| 1 · 容器与运行时   |  8 + 3 Lab | P07–P30      |      24 |
| 2 · K8S 架构与部署 |  7 + 2 Lab | P31–P58      |      28 |
| 3 · 工作负载与存储 |  3 + 3 Lab | P59–P76      |      18 |
| 4 · 配置与运维     | 11 + 1 Lab | P77–P98      |      22 |
| 5 · 收束           |          4 | P99–P102     |       4 |
| **合计**           |            | **P01–P102** | **102** |

### 精简方案（时间 ≤ 10 小时）

| 操作                               |       节省 |
| ---------------------------------- | ---------: |
| 合并 P55–P58 缓冲页                |         −3 |
| 第 1 章 containerd 演进图合并 1 页 |         −1 |
| 第 4 章 AIOps + 交付形态合并       |         −2 |
| 删除 P76 缓冲、P101 延伸           |         −2 |
| Demo 引导页仅保留标题不单独占页    |        −12 |
| **精简后约**                       | **~82 页** |

---

## 五、Demo / Lab 与 PPT 配合表

| Lab                | 对应 PPT |   时长 | PPT 上只写                      |
| ------------------ | -------: | -----: | ------------------------------- |
| Docker Quick Start |      P19 | 20 min | 目标 + 验收标准                 |
| 构建 demo-web      |      P20 | 25 min | 目录结构示意，无完整 Dockerfile |
| 节点 crictl 对照   |      P29 | 15 min | kubectl ↔ crictl 对照           |
| KubeClipper 建集群 |      P43 | 30 min | 6 步编号，无完整命令            |
| 部署 Web 应用      |      P52 | 40 min | Deployment + Service 关系图     |
| 工作负载对比       |      P63 | 25 min | 三种控制器对比表                |
| PVC 持久化         |      P66 | 20 min | PV/PVC 绑定流程                 |
| 调度策略           |      P72 | 25 min | Taint/Affinity 概念图           |
| 综合发布闭环       |      P95 | 45 min | 七步流程（不讲每步命令）        |

> **原则**：Demo 期间学员看终端/控制台，PPT 暂停或黑屏；**禁止**在 PPT 上放 20 行 bash 脚本。

---

## 六、制作 checklist

- [ ] 选用统一模板（封面 / 目录 / 章节 / 内容 / 图文 / 双栏 / 致谢）
- [ ] 从 `training-kubernetes/images/` 与 `lab-kubernetes/image/` 导入讲义插图
- [ ] 每页导出前检查：要点 ≤ 4 条、标题 ≤ 20 字
- [ ] 重点页（★）共 **12 页**，可加深色边框或图标标记
- [ ] 导出 PDF 备份；现场准备讲义 Markdown 与 kubeconfig
- [ ] 可选：用
      [generate_k8s_ppt.py](../../training-python/Case/DongFangRuiTong/dagang/generate_k8s_ppt.py)
      生成初稿再手工补图

---

## 附录：插图索引

| 章节             | 文件名                                                                       | 路径                       |
| ---------------- | ---------------------------------------------------------------------------- | -------------------------- |
| 部署演进         | `container-evolution.png`                                                    | `../images/`               |
| VM vs 容器       | `katacontainers_traditionalvskata_diagram.jpg`                               | `../images/`               |
| Namespace        | `kernel-user-mode.png`                                                       | `../images/`               |
| Docker 架构      | `docker-arch.png`, `docker-undertech.png`                                    | `../images/`               |
| Bridge 网络      | `bridge_network.jpeg`                                                        | `images/`                  |
| CRI / containerd | `k8s-CRI-OCI-docker.png`, `k8s-containerd-1-0.png`, `k8s-containerd-1-1.png` | `../images/`               |
| CRI 工具         | `k8s-cri-tools.png`, `k8s-containerd-tools.png`                              | lab-kubernetes/image       |
| K8S 架构         | `k8s-architecture.png`, `borg-arch.png`                                      | `../images/`               |
| Controller       | `kubernetes-co-loop.webp`, `kubernetes-controller-loop.webp`                 | lab-kubernetes/image       |
| Service/Ingress  | `ingress-service.drawio.svg`                                                 | lab-kubernetes/image       |
| 工作负载         | `kubernetes-arch.png`                                                        | `images/`                  |
| 镜像供应链       | `chapter-3-1.png`, `harbor-arch.png`                                         | `images/` / lab-kubernetes |
| 扩展生态         | `openshift-k8s.svg`                                                          | `../images/`               |
| Gateway          | `apigateway-servicediscover.png`                                             | lab-kubernetes/image       |
| 多区域部署       | `multi-region-caas.png`                                                      | lab-kubernetes/image       |
| 4C 安全          | `what-is-security.png`                                                       | `images/`                  |
| 生产 HA          | `openshift-ha-deployment.png`                                                | `../images/`（可选）       |

---

_文档版本：与讲义 class-05 同步 · Kubernetes 1.30+ / 1.33 特性标注_
