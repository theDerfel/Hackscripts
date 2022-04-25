import socket, sys

#!/usr/share/python
from numpy import setxor1d

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org", 43))
s.send(bytes(sys.argv[1] + "\r\n", "UTF-8"))
resposta = s.recv(1024).split()
whois = resposta[19].decode("utf-8")

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((whois, 43))
s1.send(bytes(sys.argv[1] + "\r\n", "UTF-8"))
resp = s1.recv(1024)
print(resp.decode("utf-8"))