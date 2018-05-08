import socket

# remote_ip_port = ("192.168.133.133", 8888)
remote_ip_port = ("172.16.17.113", 12348)
# remote_ip_port = ("192.168.153.133", 8885)
local_ip_port = ("192.168.133.135", 8888)
with socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    # s.connect(remote_ip_port)
    while True:
        # send_data = input("输入内容")
        send_data = "h"*100
        s.sendto(send_data.encode("utf-8"), remote_ip_port)

with socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM) as s2:
    s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s2.bind(local_ip_port)
    while True:
        data, port = s.recvfrom(1024)
        print("收到数据:{},来自于{}".format(data, port))
