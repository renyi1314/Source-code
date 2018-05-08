import socket
import os
import pickle

local_address = ("", 8888)


def down_handler(msg, sock):
    print("进入文件下载操作----")
    filename = msg.split(":")[1]
    ret = 0
    try:
        with open(filename, mode="rb") as f:
            print("{}正在传输-----".format(filename))
            data = f.read(1024)
            while data:
                send_count = sock.send(data)
                ret += send_count
                data = f.read(1024)
    except FileNotFoundError:
        print("找不到文件")
    else:
        print("文件传输成功,共传输了{}字节".format(ret))
    sock.close()


def list_handler(conn):
    print("获取文件列表中----")
    list_data = os.listdir()
    send_data = pickle.dumps(list_data)
    conn.send(send_data)
    print("文件列表获取成功:{}".format(list_data))



def upload_handler():
    print("upload handler")


def file_server(address):
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(address)
        s.listen(5)
        while True:
            conn, add = s.accept()
            msg = conn.recv(1024).decode("utf-8")
            with conn:
                print("有客户端建立新连接,地址:{},消息:{}".format(add, msg))
                if msg[0] == "G":
                    down_handler(msg, conn)
                elif msg[0] == "L":
                    list_handler(conn)


if __name__ == '__main__':
    file_server(local_address)
