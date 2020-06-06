import os

BASE_DIR = os.path.dirname(__file__)

aStr = '''
CKA005	8.210.52.222
CKA008	8.210.48.169
CKA001	8.210.50.170
CKA004	8.210.49.73
CKA009	8.210.48.116
CKA011	8.210.49.118
CKA010	8.210.50.46
CKA006	8.210.50.244
CKA007	8.210.51.109
CKA003	8.210.52.179
CKA012	8.210.51.221
CKA002	8.210.52.145
'''

aList = [i.split() for i in aStr.split('\n') if i.strip()]

print(aList)

bStr = '''
Host %s
    HostName        %s
    User            root
    IdentityFile    ~/.ssh/id_rsa_license
'''

for i, j in sorted(aList):
    print(bStr % (i.lower(), j), end='')

for i, j in sorted(aList):
    os.system('ssh-copy-id root@%s' % j)

# ansible inventory
ini = open(os.path.join(BASE_DIR, 'ckaservers.ini'), 'w')
ini.write('[ckaservers]\n')
for i, j in sorted(aList):
    ini.write('%s\n' % i.lower())
