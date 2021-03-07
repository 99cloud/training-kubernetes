ckaList = [i.split() for i in open(r'ckalab.txt')]
ckaDict = {i[0]:i[1] for i in ckaList}

template = r'''Host %s
    HostName        %s
    User            root
    IdentityFile    ~/.ssh/id_rsa_lab
    ProxyCommand    ssh cka-fq -W %%h:%%p
'''

for i in sorted(ckaDict):
    print(template % (i, ckaDict[i]))
