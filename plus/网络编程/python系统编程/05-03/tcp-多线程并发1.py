import socket
import threading


s = socket.socket()
s.bind(("", 8888))
s.listen(5)


def threading_conn():
    data = conn.recv(1024)
    while data:
        print("收到数据:{},来自于:{}".format(data.decode("utf-8"),add))
        data = conn.recv(1024)
    conn.close()


while True:
    conn, add = s.accept()
    print("有新连接啦:{},地址为:{}".format(conn, add))
    t1 = threading.Thread(target=threading_conn)
    t1.start()
    # conn.close()

