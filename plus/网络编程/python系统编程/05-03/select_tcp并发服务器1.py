import socket
import select

s = socket.socket()
s.bind(("", 8888))
s.listen(5)
read_list = []
read_list.append(s)
while True:
    read_tables, _, _ = select.select(read_list, [], [])
    for sock in read_tables:
        if sock is s:
            conn, add = s.accept()
            read_list.append(conn)
            print("有新连接:{},地址为:{}".format(conn, add))
        else:
            buf = sock.recv(1024)
            if buf:
                print("收到消息:{}".format(buf.decode("utf-8")))
            else:
                sock.close()
                read_list.remove(sock)
                print("关闭连接".format(sock))
