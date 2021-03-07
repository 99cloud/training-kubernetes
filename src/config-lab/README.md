# 实验环境拓扑：

客户端 ---> 阿里云上海跳板机 ---> Azure东亚跳板机 ---> 阿里云香港实验环境

```bash
ssh root@106.15.4.212
ssh apple@13.70.46.16
ssh root@cka0XX-ip
```

# 免密码登陆步骤

1. 阿里云到处 Name 和公网 IP 两列，复制到 ckalab.txt
2. 生成 .ssh/config 文件配置：`python gen-ssh-config.py`
3. 配置密钥：`cat ckalab.txt | awk '{print $1}' | xargs -I{} ssh-copy-id -i ~/.ssh/id_rsa_lab.pub {}`
4. 配置 bastion ssh：

    ```
    Host cka-bastion
        HostName        106.15.4.212
        User            root

    Host cka-fq
        HostName        13.70.46.16
        User            apple
        ProxyCommand    ssh cka-bastion -W %h:%p
    ```

5. 配置 cka 机器密钥：`ansible-playbook -i hosts config-lab.yml`
6. 配置好之后，就可以直接：`ssh cka001`
