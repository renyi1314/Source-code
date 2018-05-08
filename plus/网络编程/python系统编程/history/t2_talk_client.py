import socket
import threading

remote_ip_port = ("192.168.133.133", 8888)
local_ip_port = ("192.168.133.135", 8888)

s = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(local_ip_port)


def send_data():
    while True:
        send_data = input("")
        s.sendto(send_data.encode("utf-8"), remote_ip_port)


def recive_data():
    while True:
        data, port = s.recvfrom(1024)
        print("收到数据:{},来自于{}".format(data, port))


t1 = threading.Thread(target=send_data)
t2 = threading.Thread(target=recive_data)
t1.start()
t2.start()
t1.join()
t2.join()
