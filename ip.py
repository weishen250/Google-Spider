import socket

url = "http://www.baidu.com"

host1 = url.replace('http:','').replace('https:','').replace('/','')
# res = socket.gethostbyname(socket.gethostname(host1))
# res = socket.getaddrinfo(host1, 'www')
# ip = socket.gethostbyname(socket.getaddrinfo(host1))
hostname = socket.gethostname()
# 获取本机ip
ip = socket.gethostbyname(host1)

print(ip)