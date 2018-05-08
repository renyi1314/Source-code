import socket
import os

local_address = ("192.168.133.133", 8888)


def file_server():
    s = socket.socket()
    s.bind(local_address)
    s.listen(5)
    conn, address = s.accept()
    data = conn.recv(1024).decode("utf-8")
    print("有客户端连接:{},选项为{}".format(address, data))
    if data[0] == "1":
        filename = data.split(":")[1]
        print("请求文件名:{}".format(filename))
        try:
            with open(filename, mode="rb") as f:
                data = f.read(1024)
                while data:
                    print(data)
                    conn.send(data)
                    data = f.read(1024)
            conn.close()
            s.close()
        except FileNotFoundError:
            print("找不到文件")
        else:
            print("文件传输完成")
    if data[0] == "2":
        list_dir = str(os.listdir())
        conn.send(list_dir.encode("utf-8"))
    if data[0] == "3":
        filename = conn.recv(1024)
        print(filename)
        with open(filename.decode("utf-8"), mode="wb") as f:
            data = conn.recv(1024)
            while data:
                f.write(data)
                data = conn.recv(1024)


if __name__ == '__main__':
    file_server()
