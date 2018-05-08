import socket
import threading

remote_ip_port = ("192.168.133.135", 8888)
local_ip_port = ("192.168.133.133", 8888)
lock1 = threading.Lock()
lock2 = threading.Lock()
with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(local_ip_port)
    while True:
        # lock1.acquire()
        data_rec, addr = s.recvfrom(1024)
        print("从{}接收到数据{}".format(addr, data_rec.decode("utf-8")))
        # time.sleep(1)
        # lock1.release()
        data_input = input("请输入内容")
        s.sendto(data_input.encode("utf-8"), remote_ip_port)
