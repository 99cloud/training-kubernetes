# 实验环境拓扑：

客户端 ---> 阿里云上海跳板机 ---> Azure东亚跳板机 ---> 阿里云香港实验环境

```bash
ssh root@106.15.4.212
ssh apple@13.70.46.16
ssh root@cka0XX-ip
```

# 免密码登陆步骤

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
