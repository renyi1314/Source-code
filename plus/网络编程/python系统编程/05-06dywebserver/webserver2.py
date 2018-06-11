import socket
from multiprocessing import Process
import threading
import mimetypes
import os
import time


class StaticWebServer:
    ROOT_DIR = "."
    RESPONSE_TABLE = {200: "OK", 404: "NOT FOUND"}

    def __init__(self, port=8888, max_listen=5):
        self.listen_socket = socket.socket()  # 初始化socket对象
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_socket.bind(("", port))  # 绑定地址
        self.listen_socket.listen(max_listen)  # 监听请求
        self.header_dict = {}  # 客户端请求头,解析成字典
        self.filename = ""  # 客户端请求静态文件(路径及文件名)
        self.response_dict = {}  # 回复信息
        self.status = 0  # 回复状态码
        self.response_headers = ""  # 回复头信息
        self.response_data = ""  # 回复body数据
        self.conn = socket.socket()  # 先定义连接,下面再使用

    # 运行服务器
    def runserver(self):
        while True:
            self.conn, _ = self.listen_socket.accept()
            print("收到客户端请求,地址为{}".format(_))
            p1 = Process(target=self.server_handler)
            p1.start()
            self.conn.close()

    # 服务器处理函数
    def server_handler(self):
        self.get_parse_headers()
        self.get_file_status()
        self.gen_response_headers()
        if self.filename.startswith("static"):
            if self.status == 200:
                self.send_file()
        else:
            from mywebserver.web_wsgi import application
            data = application(self.header_dict, self.response__)
            self.conn.send(data.encode("utf-8"))

    # 解析客户端请求头数据
    def get_parse_headers(self):
        self.data = self.conn.recv(2048).decode("utf-8")
        if self.data:
            self.filename = self.data.splitlines()[0].split()[1][1:]

    # 生成回复头部数据
    def gen_response_headers(self):
        self.response_headers = "HTTP/1.1 {} {}\r\n".format(self.status, self.RESPONSE_TABLE[self.status])
        self.header_dict["name"] = self.data.splitlines()[0].split()[1][1:]
        self.response_dict["name"] = self.data.splitlines()[0].split()[1][1:]
        self.response_dict["Content-Type"] = mimetypes.guess_type(self.filename)[0]
        # self.response_dict["Content-Type"] = "text/html"
        self.response_dict["Connection"] = "Closed"
        data = ['{}: {}\r\n'.format(k, v) for k, v in self.response_dict.items()]
        datas = "".join(data)
        self.response_data = "{}{}\r\n".format(self.response_headers, datas)
        # self.conn.send(self.response_data.encode("utf-8"))
        # print(self.response_data)

    # 简单验证请求,生成状态码
    def get_file_status(self):
        os.chdir(self.ROOT_DIR)
        if self.filename.startswith("static"):
            if os.path.isfile(self.filename):
                self.status = 200
        else:
            self.status = 200

    # 向客户端发送数据
    def send_file(self):
        with open(self.filename, mode="rb") as f:
            data = f.read(1024)
            while data:
                self.conn.send(data)
                print(data)
                data = f.read(1024)

    # 回调函数,向客户端发送响应头
    def response__(self, str_status, tuple_headers):
        response_header = "HTTP/1.1 {}\r\n".format(str_status)
        tmp = ['{}: {}\r\n'.format(x[0], x[1]) for x in tuple_headers]
        response_data = ''.join(tmp)
        data = '{}{}\r\n\r\n'.format(response_header, response_data)
        print(data)
        self.conn.send(data.encode("utf-8"))


webServer = StaticWebServer()
webServer.runserver()
