#!/usr/bin/python
import urllib3, socket
from bs4 import BeautifulSoup

def removebarra(s):
    removido = ''
    if s[-1] == '/':
        removido = s[:-1]
    else:
        return s
    return removido

url = "businesscorp.com.br"

http = urllib3.PoolManager()
site = http.request('GET', url)
print("=========================================================================================")
print(url, "--->", socket.gethostbyname(url))
print("=========================================================================================")
print("INFORMAÇÕES")
print("=========================================================================================")
print("Status Code:", site.status)
server = site.headers["Server"]
print("Server:", server)
html = site.data
soup = BeautifulSoup(html, "html.parser")
urls = []

print("=========================================================================================")
print("URLS E IPS NO SITE")
print("=========================================================================================")

for link in soup.findAll('a'):
    if 'http' not in link.get('href'):
        continue
    else:
        if 'https' in link.get('href'):
            urls.append(removebarra(link.get('href')[8:]))
        else:
            urls.append(removebarra(link.get('href')[7:]))

for link in urls:
    try:
        print(link, "--->", socket.gethostbyname(link))
    except:
        print(link)

subdomains = input("Deseja fazer bruteforce de subdomínios?\n1 - SIM\n2 - NÃO\n")

if subdomains == '1':
    print("=========================================================================================")
    arq = open("subdomains.txt", 'r')
    domains = arq.readlines()
    for linha in domains:
        bruteforce = linha + '.' + url
        bruteforce = bruteforce.replace('\n', '')
        try:
            site2 = http.request('GET', bruteforce)
            print(bruteforce, site2.status)
        except:
            continue
    arq.close()
print("=========================================================================================")