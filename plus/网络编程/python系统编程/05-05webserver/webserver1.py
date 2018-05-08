import socket
import os
from multiprocessing import Process
import mimetypes

'''
    1.初始化socket开放并监听端口
    2.接受客户端连接,接收客户端数据
    3.解析客户端数据
    4.定义返回码,定义静态文件路径
    5.若有请求静态文件,定位到文件,发送给客户端
'''


class StaticWebServer:
    ROOT_DIR = "."
    RESPONSE_TABLE = {200: "OK", 404: "NOT FOUND"}

    def __init__(self, port=8888, max_listen=5):
        self.listen_socket = socket.socket()
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_socket.bind(("", port))
        self.listen_socket.listen(max_listen)
        self.header_dict = {}  # 客户端请求头,解析成字典
        self.filename = ""  # 客户端请求静态文件(路径及文件名)
        self.response_dict = {}  # 回复信息

    # 接收解析请求头数据
    def receive_parse_request_head(self):
        # 接收客户端数据转码并分割
        data = self.conn.recv(1024 * 1024).decode("utf-8").split("\r\n")
        print(data)
        if data:
            while "" in data:
                data.remove("")
            self.header_dict["method"] = data[0].split()[0]
            self.header_dict["filename"] = data[0].split()[1]
            self.header_dict["pro"] = data[0].split()[2]
            self.header_dict.update({i.split(":")[0]: i.split(":")[1] for i in data[1:]})
        return self.header_dict

    # 根据客户请求数据判断文件是否存在
    def get_request_file_status(self):
        os.chdir(self.ROOT_DIR)
        self.filename = self.header_dict["filename"][1:]
        self.mimetypes_file(self.filename)
        if os.path.isfile(self.filename):
            status = 200
        else:
            status = 404
        return status

    def add_send_response(self, status):
        header = "HTTP/1.1 {} {}\r\n".format(status, self.RESPONSE_TABLE[status])
        data = ['{}: {}\r\n'.format(k, v) for k, v in self.response_dict.items()]
        datas = "".join(data)
        response_header = '{}{}\r\n'.format(header, datas)
        print(response_header)
        self.conn.send(response_header.encode("utf-8"))

    def add_response(self, key, value):
        self.response_dict[key] = value

    def send_file(self):
        with open(self.filename, mode="rb") as f:
            data = f.read(1024)
            while data:
                self.conn.send(data)
                data = f.read(1024)

    def mimetypes_file(self, filename):
        self.response_dict["Content-Type"] = mimetypes.guess_type(filename)[0]

    def server_handler(self):
        self.receive_parse_request_head()
        status = self.get_request_file_status()
        self.add_response('Connection', 'Closed')
        self.add_send_response(status)
        if status == 200:
            self.send_file()

    def runserver(self):
        while True:
            self.conn, add = self.listen_socket.accept()
            print("有客户端新进连接了,地址为{}".format(add))
            p1 = Process(target=self.server_handler)
            p1.start()
            self.conn.close()


webServer1 = StaticWebServer()
webServer1.runserver()
