import socket
import pickle


local_address = ("", 9991)
remote_address = ("192.168.133.133", 8888)


def get_handler(msg):
    s = socket.socket()
    s.connect(remote_address)
    print("已与远程主机建立连接----{}".format(remote_address))
    send_data = msg.encode("utf-8")
    s.send(send_data)
    filename = msg.split(":")[1]
    with open(filename, mode="wb") as f:
        data = s.recv(1024)
        while data:
            f.write(data)
            data = s.recv(1024)
    s.close()


def put_handler():
    pass


def list_handler():
    s = socket.socket()
    s.connect(remote_address)
    s.send("L:".encode("utf-8"))
    data = s.recv(1024)
    pick_data = pickle.loads(data)
    print("文件列表:{}".format(pick_data))


def file_client():
    msg = input("请输入要选择的功能:[G]:下载,[L]:获取列表,[P]上传")
    while not msg.startswith("quit"):
        if msg[0] == "G":
            get_handler(msg)
        elif msg[0] == "L":
            list_handler()
        elif msg[0] == "P":
            put_handler(msg)
        else:
            print("输入错误")
        msg = input("请输入要选择的功能:[G]:下载,[L]:获取列表,[P]上传")


if __name__ == '__main__':
    file_client()
