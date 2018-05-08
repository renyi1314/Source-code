import socket

ip_port = ("192.168.133.135", 8888)
remote_ip = ("192.168.133.133",8888)
while True:
    with socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(ip_port)
        data, port = s.recvfrom(1024)
        print("收到数据:{},来自于{}".format(data, port))

while True:
    with socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM) as f:
        f.connect(ip_port)
        send_data = input("123")
        f.sendto(send_data.encode("utf-8"), ip_port)