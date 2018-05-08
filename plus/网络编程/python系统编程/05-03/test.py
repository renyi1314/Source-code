import socket
from multiprocessing import Process

local_address = ("", 8888)

s = socket.socket()
s.bind(local_address)
s.listen(5)


def process_conn():
    data = conn.recv(1024)
    while data:
        print(data)
        data = conn.recv(1024)
    conn.close()

while True:
    conn, add = s.accept()
    print("有新连接{},地址:{}".format(conn,add))
    p1 = Process(target=process_conn)
    p1.start()
    conn.close()