import socket

local_ip_port = ("192.168.133.133", 8888)
remote_ip_port = ("192.168.133.135", 8888)
with socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(local_ip_port)
    while True:
        data, port = s.recvfrom(1024)
        print("收到数据:{},来自于{}".format(data.decode("utf-8"), port))

with socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM) as s2:
    s2.connect(remote_ip_port)
    while True:
        send_data = input("请输入内容")
        s2.sendto(send_data.encode("utf-8"), remote_ip_port)
