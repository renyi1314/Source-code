import socket

remote_ip_port = ("192.168.153.135", 8888)
local_ip_port = ("192.168.133.133", 8888)
with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(local_ip_port)
    while True:
        data, addr = s.recvfrom(1024)
        print("从{}接收到数据{}".format(addr, data))
