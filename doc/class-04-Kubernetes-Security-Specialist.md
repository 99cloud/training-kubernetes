# Kubernetes 安全纪要和最佳实践（Kubernetes Security Specialist）

## 注意 ⚠️

- **未经允许，禁止转载**

## Prefix

- 授课时长：
    - 上午：9:30 至 12:00
    - 下午：13:30 至 16:00
- Prerequisite
    - [CKA](class-01-Kubernetes-Administration.md)

## Catalog

| Date | Time | Title | Content |
| ---- | ---- | ----- | ------- |

* kubernetes 安全/cks
  * 概述
  * 课程概述
  * 什么是安全
  * 云安全
    * cncf 项目安全相关
    * 安全考量原则
    * 理解攻击面
    * 攻击类别
    * 攻击源
    * 主动/被动 攻击
    * 安全方面的网上资源
      * NIST Cybersecurity Framework
      * High Value Asset Protection
      * National Checklist Program
      * CIS Benchmarks
      * kube-bench
    * 企业安全文化
      * 开发组安全文化
      * 安全组文化
  * k8s 风险面
    * 来自镜像的风险
      * 私有镜像仓库 -- 愤怒的员工
      * 公网镜像的风险 -- 理解镜像的供应链
      * 应对策略
    * 运行镜像引擎的风险考量 -- container runtime
      * gvisor
      * kata
      * firecrack
    * 来自于软件安装包的风险考量
      * 应对策略
        * The Update Framework (TUF)
        * Notary
  * 搭建 k8s 集群前的安全事考量
    * 找到内核的风险点 CVE
    * 利用内核功能抵御攻击
    * 搭建多节点集群
  * 加固集群访问安全
    * 加固 kube-apiserver
    * 开启审计日志
    * 合理使用 RBAC
    * 使用 Pod Security Policies
    * etcd 的安全
    * 加密 secret 数据
    * 合理使用 admission controller
    * 使用 serviceaccount
  * 加固 k8s 集群网络安全
    * 网络漏洞扫描
    * 阻止 pod 跨 namespace 访问
    * 服务网格的产品的考量
    * 尽可能的使用  mTLS
  * k8s 工作负载的安全加固和考量
    * 下载一个镜像前的考量
    * 运行一个容器前的考量
    * 保护容器 container layer 的安全
    * 容器运行后的安全分析
    * crd 和 operator 的安全考量
    * 容器运行中安全工具介绍
      * seccomp
      * selinux
      * apparmor
  * 问题风险发现
    * 理解攻击的生命周期
      * 理解 kill chain
    * 风险管控的 checklist
    * 被攻击后的应对策略
      * 被攻击后的应对策略 -- 报告机制
      * 涉及违法的应对策略
      * 建立紧急应对小组
      * 完善的故障报告
    * 入侵检测
      * 主机入侵检查
      * 网络入侵检查

## 1. 课程介绍

云安全是一个演进的过程，不是一朝一夕，而是需要经历持续的、无数的积累和实践，才能构建出让人放心的云环境。

本课程旨在介绍：

1. 如何解决云生产环境的安全问题
2. 安全容器供应链
3. K8S 集群持续安全和敏捷使用
4. 在哪里可以找到持续的安全和漏洞信息

该课程包括：

1. 用于构建和保护 Kubernetes 集群的动手实验
2. 监控和记录安全事件的动手实验

在本课程结束时，您将学到以下内容：

1. 了解云生产环境的安全问题
2. 了解如何强化系统和集群
3. 讨论围绕容器供应链的安全主题
4. 了解如何监控和记录安全事件等等

## 2. 云安全概述

### 2.1 章节梗概

* 理解安全问题的发生和防止是一个持续的过程
* 讨论安全问题的发生和应对方法
* 讨论攻击的类型
* 4C 安全层级：code / container / cluster / cloud
* 了解安全机制和安全资源

### 2.2 什么是计算机安全？

![](images/what-is-security.png)

计算机安全是对计算机或计算机系统有用资产（Asset）的保护。资产包括：硬件、软件、数据、流程、人员或其他们的组合。

- **资产的生命周期**：安全始于获取资产。重要的是，实物资产有一个保管链，直到资产上电。
- **软件开发的生命周期**：包括设计、开发、测试和部署的过程。在项目的设计阶段考虑安全性是至关重要的。
- **制定组织政策和程序**：制定政策和程序可以降低意外或故意伤害的风险。
- **定义角色和职责**：建立事件响应的层次结构非常重要。由于工作的艰巨性，需要有一个明确的领导者或分配领导者的预案。

安全从来不是一朝一夕的事情，他需要经历持续的、无数的积累和实践才能构建出让人放心的云环境。因为工具手段不停的在更新和演进，所以我们也需要不停的学习和实践，才能保证我们的云平台安全。

### 2.3 攻击面

每个云平台中的组件都是一个可能被攻击的点，每个组件都由代码构成，都会存在风险。最安全的做法是不让这些数据通过网络暴露出来（锁在安全级别高的房间里），但是这样我们也不能对外正常提供服务了，也就失去了存在的意义，所以控制好平衡很有必要。

#### 2.3.1 ETCD 数据库安全

k8s 中存放最核心数据的是 etcd 数据库，一但数据文件被恶意摧毁，如果没有备份，就很难恢复。

- 默认 kubeadm 会将 etcd 和 controller 部署在一起，etcd 数据目录上挂载到 /var/lib/etcd，如果攻击者删除这个目录话，就会对集群造成致命影响。
- **从安全角度来说一个分离部署的 etcd 数据库集群是更理想**，你可以参照 [集群数据库分离](https://github.com/justmeandopensource/kubernetes/blob/master/kubeadm-external-etcd/3%20setup-kubernetes-with-external-etcd.md) 来搭建数据库和 k8s 集群分离的场景

```yaml
# default kubeadm etcd static pod
$ cat /etc/kubernetes/manifests/etcd.yaml
# output
    volumeMounts:
  - mountPath: /var/lib/etcd
    name: etcd-data
 ...
volumes:
...
- hostPath:
    path: /var/lib/etcd
    type: DirectoryOrCreate
  name: etcd-data

# separete etcd cluster config
$ kubectl get cm -nkube-system kubeadm-config -o yaml
apiVersion: v1
data:
  ClusterConfiguration: |
    apiServer:
      certSANs:
      - kubernetes
      - kubernetes.default
      - kubernetes.default.svc
      - kubernetes.default.svc.mec01.com
      - localhost
      - 127.0.0.1
      - vip.mec01.com
      - 172.xx.xx.100
      - master-1
      - master-1.mec01.com
      - 172.xx.xx.207
      - master-2
      - master-2.mec01.com
      - 172.xx.xx.228
      - master-3
      - master-3.mec01.com
      - 172.xx.xx.225
      - 10.xx.xx.1
      extraArgs:
        authorization-mode: Node,RBAC
        bind-address: 0.0.0.0
        feature-gates: CSIStorageCapacity=true,ReadWriteOncePod=true,RotateKubeletServerCertificate=true
      timeoutForControlPlane: 4m0s
    apiVersion: kubeadm.k8s.io/v1beta3
    certificatesDir: /etc/kubernetes/pki
    clusterName: mec01.com
    controlPlaneEndpoint: vip.mec01.com:6443
    controllerManager:
      extraArgs:
        bind-address: 0.0.0.0
        cluster-signing-duration: 87600h
        feature-gates: RotateKubeletServerCertificate=true,CSIStorageCapacity=true,ReadWriteOncePod=true
        node-cidr-mask-size: "24"
      extraVolumes:
      - hostPath: /etc/localtime
        mountPath: /etc/localtime
        name: host-time
        readOnly: true
    dns:
      imageRepository: registry-1.ict-mec.net:18443/coredns
      imageTag: 1.9.3
    etcd:
      external:
        caFile: /etc/ssl/etcd/ssl/ca.pem
        certFile: /etc/ssl/etcd/ssl/node-master-1.pem
        endpoints:
        - https://xx.xx.xx.xx:2379
        - https://xx.xx.xx.xx:2379
        - https://xx.xx.xx.xx:2379
        keyFile: /etc/ssl/etcd/ssl/node-master-1-key.pem
    imageRepository: registry-1.ict-mec.net:18443/kubesphere
    kind: ClusterConfiguration
    kubernetesVersion: v1.27.2
    networking:
      dnsDomain: mec01.com
      podSubnet: 10.xx.xx.0/18
      serviceSubnet: 10.xx.xx.0/18
    scheduler:
      extraArgs:
        bind-address: 0.0.0.0
        feature-gates: CSIStorageCapacity=true,ReadWriteOncePod=true,RotateKubeletServerCertificate=true
kind: ConfigMap
metadata:
  creationTimestamp: "2023-08-23T05:47:44Z"
  name: kubeadm-config
  namespace: kube-system
  resourceVersion: "233"
  uid: fd244790-167b-4024-b465-60caaf9c04ea
```

#### 2.3.2 网络安全

网络也需要额外注意，我们期望正常访问不受影响，同时阻拦非正常的访问。可以配置防火墙白名单，比如我们对 kube-apiserver 的可访问地址段做配置，只能从 172.25.0.0/24 这个网段来访问 kube-apiserver。

- k8s 近期的版本所有的请求基本都是 zero trust 所有通讯都用 mTls (双向 tls) 认证的方式来访问，但是如果由于处于某原因，比如贪图方便直接通过 `kubectl proxy"` 来开放 kube-apiserver 访问方式就增加不安全风险
- 更糟的情况 `kubectl proxy --address="0.0.0.0"` 如果你的集群有配置 san 名比如 abc.com ，前面的命令会造成更大的安全问题，攻击者很容易就通过配置 .kube/config 配合 /etc/hosts 中伪装 abc.com 指向，就可以通过其他节点攻击 kube-apiserver 了

```console
# 查看访问路径
$ kubectl get node -v=10 2>&1 | tee output
$ cat output | grep -i "GET https:"
# output
I1009 10:05:38.708661   36252 round_trippers.go:553] GET https://xx.xx.xx.xx:6443/api/v1/nodes?limit=500 200 OK in 8 milliseconds
$ kubectl proxy
# 无证书直接访问 api-server
$ curl http://127.0.0.1:8001/api/v1/nodes?limit=500 
```

k8s 中的 kube-proxy、kubelet 都需要和 kube-apiserver 安全通讯机制。不能为了方便妥协。

#### 2.3.3 其它安全考量

云平台通常是有很多个项目组合而成的，项目越多自然攻击平面就越广泛，我们应该选择 cncf 的**毕业项目**，这些项目应该已经充分考虑的安全因素，**孕育中的项目** 则会多多少少欠缺一点安全性，比如：CNI, CRI-O, Linkerd, OpenTracing, Thanos 等。**Sandbox 项目**则会比会”孕育中的项目“安全情况可能更严峻一些，比如 Artifact Hub，k3s，in-toto，Keylime，Parsec。**Archived 项目**则是已经停止维护的项目，用户如果使用这些项目，则要自己面对安全风险。

k8s 有专门的 sig 负责安全方面的工作 [Kubernetes Security Profiles Operator SIG](https://github.com/kubernetes-sigs/security-profiles-operator), 并且 cncf 有专门的小组负责所有项目的安全 [CNCF Special Interest Group for Security](https://github.com/cncf/sig-security)

#### 2.3.4 风险的来源、类别和应对

资源的分配 -- 可能会造成各种风险的提升比如

- SSO 单点登陆的方案看似很好管理，但是他提高的安全的风险，如果 sso 服务出现的了问题，则所有的平台都不可登录。
- 每多增加一个安全管理成员就多一份安全风险，这是从人事任命角度的观点。因为人有很多不可控的因素比如情绪、生活压力等，当然只有一个安全管理也是一个安全风险。
- 耦合度过高服务应用 -- 比如将很多关键服务部署在了没有灾备方案的主机群或者平台上，如果平台或者主机群出现的断电则这些服务都将停止服务。

应对策略

- Prevention / 防止机制 -- 我们需要经可能的防止使安全风险上升的事情发生，我们可以通过硬件或者软件的手段来达成这样的目标。
    - 通过安全登录软件来控制 `人/应用` 对特定的 `软件/硬件` 的访问
    - 增加管理流程，比如 `appA` 需要访问 `数据库A` 需要填写必要的申请并等待审核通过
    - 根据安全等级，我们甚至可以将物理设备离线管理，唯一能够登录的地方可以设置在一间带有密码锁，或者需要授权的员工卡才能打开的房间里
- Detection/检测机制 -- 当然光靠 `Prevention/防止机制` 是不可能完全屏蔽安全风险的，一旦有影响安全事件发生时，我们需要能够通过各种手段检测到， 在我们称之为 `Intrusion Detection and Prevention Systems/入侵检测和防止系统(IDPS)` 中的 `Prevention Systems/防止系统` 就是我们上面讨论的问题。 `Intrusion Detection/入侵检测` 对我们来说比较直观的方法是 `静态数据监控` 即通过 `监控/日志` 收集的方式来实现比如我们可以在 k8s 上安装 `Prometheus`
    - Reaction/应对机制 -- 应对总是被动的，但是我们可以把应对变的尽可能不这么被动， 比如当 k8s 彻底宕机了，但如果我们在每天定时做了 etcd 数据库全量备份或者使用 velero 做了对象备份，那么可能我们至少能将集群回复到一个最接近宕机前的状态

攻击者的类别

- White Hat/白帽 -- 通常就职于安全公司，他们会遵守法律将发现的漏洞通知对应的机构
- Black Hat/黑帽 -- 也是我们常说的黑客他们会入侵计算机 窃取 或者 摧毁 宝贵的数据，用于他们自己的目的
- Script Kiddie/脚本小子 -- 不是高手只是懂点皮毛，他们拿着别人写好的脚本或者工具来进行攻击
- Hacktivist/有黑客行为者 -- 这些人一般带有宣传目的来攻击，他们一般攻击网页篡改首页显示的文字来达到他们的目的
- Nation State/国家组织 -- 这些攻击者隶属于一个国家的机构
- Organized Crime/有组织的犯罪 -- 处于某些利益，有组织的攻击计算机
- Bots/机器人 -- 被攻击这控制的电脑或者终端，被控制后用来攻击计算机

攻击来源

- 内部 -- 内部攻击一般来自于内部员工，最常见的比如窃取了他们本身有权访问的源码或者设计图纸，但是将这些信息贩卖给了竞争对手
- 外部 -- 通过网络的手段作为非法的用户登录的计算机上窃取信息

攻击类别

- Active Attacks/主动 -- 主动攻击类型，主要目的是摧毁正常工作的应用和服务，通常的手段有 拒绝、泛洪攻击等即通过增加应用的负载或者贷款来让服务变得几乎不可用
  - Denial of service/拒绝服务 -- 通常通过让客户端负载超负荷，比如疯狂发起对 kube-apiserver 请求导致 kube-apiserver 无法相应正常的请求，导致 k8s 平台不可用
  - Spoofing attacks/欺骗攻击 -- 或者收茂名顶替的攻击通常发生在 ARP、DNS、IP地址和MAC容易受到欺骗，比如服务 ```appA``` 使用 ip 为 10.0.0.100 身份认证 api ```apiA``` ，如果攻击者假装成为 10.0.0.100 上的 ```apiA``` 并授权所有从 ```appA``` 请求的用户那么 ```appA``` 怎完全失去了认证授权的保护了
  - Port scanning/端口扫描 -- 攻击者通过使用 nmap 来扫描主机上的端口，返回的结果可以给攻击者充分的服务应用列表正在运行在目标节点之上
- Passive Attacks/被动 -- 被动攻击者通常不会修改任何东西，他们只是查看一些敏感的数据，并拍照或者复制下来，很难被察觉。

4c 安全层级--我们的安全实现的思路是尽可能不让 code 层的风险外溢到 container 外面。

- code -- 代码层级位于最内层
- container -- 容器层级位于第二层
- Cluster -- 集群层级位于第三层
- Cloud -- 云平台层级位于最外层

![](images/4c-1.png)

硬件方面安全演进 -- 在硬件层面安全软件也在蓬勃发展中比如 [Platform AbstRaction for SECurity (PARSEC)](https://github.com/parallaxsecond/parsec) 为硬件提供通用的安全的 api

Federal Information Processing Standard (FIPS)/联邦信息安全处理标准 -- 是美国关于计算机安全的一个标准，大家有兴趣的话可以查看 [Computer Security Resource Center Publications web page](https://csrc.nist.gov/publications) 长篇大论，总结核心内容如下：

- Asset Management/资产管理
- Business Environment/商业环境
- Governance/政府相关决策
- Risk Assessment/风险把控
- Risk Management Strategy/风险管理机制
- Supply Chain Risk Management/供应链安全管理

High Value Asset Protection/高价值资产保护 -- 一些非常敏感的业务做好服务与安全的平衡非常重要，比如银行信用卡信息查询的接口，如果过度保护起来则他将不再有能为大家提供必要的查询服务，所以我们需要走出妥协，在美国我们可以向 ```Cybersecurity and Infrastructure Security Agency (CISA)``` 协会申请对应用进行必要的风险评估，以确认他的安全机制是有能力抵御安全风险的

National Checklist Program/国家安全检查程序列表 -- 是一个网站在他背后有数据库(National Vulnerability Database (NVD))记录着大量的软件或者云平台各个版本中存在的漏洞或者风险,大家可以访问 [NATIONAL VULNERABILITY DATABASE](https://nvd.nist.gov/) 来查看一个全局的信息，或者直接通过查询页面来查询 k8s 特定版本存在的问题  [NIST 查询页面](https://nvd.nist.gov/ncp/repository)

[National Vulnerability Database](https://nvd.nist.gov/)

![nist 页面](images/nist-1.png)

[NIST 查询页面](https://nvd.nist.gov/ncp/repository)

![nist 页面](images/nist-2.png)

CIS Benchmarks/cis 安全压力测试 -- [Center for Internet Security, Inc. (CIS®)](https://www.cisecurity.org/) 是一个 ```非盈利性组织``` 他提供一些免费的最佳实践信息以及一些免费安全压力测试组件，有兴趣的同学可以自行了解下

kube-bench -- [kube-bench](https://github.com/aquasecurity/kube-bench) 是一个工具用来做 k8s 的安全测试工具来自于一家安全公司 ```Aqua Security``` 它提供的测试可能并没有 ```CIS Benchmarks``` 来的那么全面但是还是值得一用的

More on High Value Asset Protection/更多高价值资源防护信息 -- 你可以访问 ```Homeland Security/国土安全``` 的页面 [Cybersecurity Directives/安全漏洞目录](https://www.cisa.gov/news-events/directives) 来查看目前存在的安全漏洞，以及查看 [Securing High Value Assets page](https://cyber.dhs.gov/bod/18-02/) 页面来了解来自 ```Homeland Security/国土安全``` 部门对高价值资产保护的建议

Improve Security Team Culture/安全部门的文化建设 -- 经常在研发团队内，大家谈到安全都会略有反感，可能觉得一些安全考量会影响我们的开发工作觉得很麻烦，这种抵触的情绪应该通过培训和学习来装便这样的观念，安全团队应该尽可能的介入每个项目的开发生命周期中，同时安全团队需要建设良好的协助机制，来协助研发完成开发工作并同时兼顾安全，比如当研发团队提出的功能实现设计安全风险时，安全团队不应该立刻拒绝这个功能的实现，而是帮助研发如何实现这个功能并且兼顾安全。

Limit Access/访问限制 -- 通过限制各个访问关键的节点也是有效的提高安全的一种的方法

- 节点与节点之间的网络安全 -- ```工作节点``` 到 ```工作节点``` 之间的网络应有 ```软件/硬件``` 的防火墙存在，包括 ```工作节点``` 到 ```infa node/基础节点(通常在 k8s 中是南北向网络出入的节点即 k8s 外部访问 k8s 内部的节点)``` 之间也应该有 ```软件/硬件``` 的防火墙
- ci/cd 环境--经常会因为代码的更新不停的迭代，我们也不应该忽视风险的存在，比如 ci/cd 的环境应该拒绝从公网被访问，因为这些代码刚被写出来可能存在者安全的风险，同时我们应该增加安全扫描软件在整个 pipeline 的构建过程。
- 非容器化的安全工具 -- 比如 SELinux, Kerberos, SAML ,这里 SELinux 比较有争议 软件/平台 都会建议大家关闭他，我们的态度是如果 软件/平台 没有显式的提出需要关闭它，那么我们建议就开着 SELinux

### 2.4 lab

### lab-1 -- install aio k8s

参考 [实验：k8s 的部署](class-01-Kubernetes-Administration.md#27-实验k8s-的部署)

## 3. 安装准备

## 4. 安装 K8S 集群

## 5. Kube-APIServer 的安全防护

## 6. 网络

## 7. 工作负载考虑事项

## 8. 问题检测

## 9. Domain 审查
