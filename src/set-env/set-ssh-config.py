import os

BASE_DIR = os.path.dirname(__file__)

aList = [i.split() for i in open(os.path.join(BASE_DIR, "cka.txt"))]
aList = [i for i in aList if i]
print(aList)

bStr = '''
Host %s
    HostName        %s
    User            root
    IdentityFile    ~/.ssh/id_rsa_common
'''

for i, j in sorted(aList):
    print(bStr % (i.lower(), j), end='')

# for i, j in sorted(aList):
#     os.system('ssh-copy-id -i ~/.ssh/id_rsa_common.pub root@%s' % j)

# ansible inventory
ini = open(os.path.join(BASE_DIR, 'ckaservers.ini'), 'w')
ini.write('[ckaservers]\n')
for i, j in sorted(aList):
    ini.write('%s\n' % i.lower())

ini.write('\n[ckamasters]\n')
for i, j in enumerate(x for x, y in sorted(aList) if "master" in x):
    ini.write('%s cidr=192.168.%d.0/16\n' % (j.lower(), i + 1))

ini.write('\n[ckaslaves]\n')
for i, j in enumerate(x for x, y in sorted(aList) if "slave" in x):
    ini.write('%s\n' % j.lower())
