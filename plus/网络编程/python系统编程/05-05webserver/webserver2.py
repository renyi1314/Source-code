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
        self.listen_socket = socket.socket()
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_socket.bind(("", port))
        self.listen_socket.listen(max_listen)
        self.header_dict = {}  # 客户端请求头,解析成字典
        self.filename = ""  # 客户端请求静态文件(路径及文件名)
        self.response_dict = {}  # 回复信息
        self.status = 0
        self.response_headers = ""
        self.response_data = ""
        self.conn = socket.socket()

    def runserver(self):
        while True:
            self.conn, _ = self.listen_socket.accept()
            print("收到客户端请求,地址为{}".format(_))
            p1 = Process(target=self.server_handler)
            p1.start()
            self.conn.close()

    def server_handler(self):
        self.get_parse_headers()
        self.get_file_status()
        self.gen_response_headers()
        if self.status == 200:
            self.send_file()

    def get_parse_headers(self):
        data = self.conn.recv(2048).decode("utf-8")
        if data:
            self.filename = data.splitlines()[0].split()[1][1:]

    def gen_response_headers(self):
        self.response_headers = "HTTP/1.1 {} {}\r\n".format(self.status, self.RESPONSE_TABLE[self.status])
        self.response_dict["Content-Type"] = mimetypes.guess_type(self.filename)[0]
        self.response_dict["Connection"] = "Closed"
        data = ['{}: {}\r\n'.format(k, v) for k, v in self.response_dict.items()]
        datas = "".join(data)
        self.response_data = "{}{}\r\n".format(self.response_headers, datas)
        self.conn.send(self.response_data.encode("utf-8"))
        print(self.response_data)

    def get_file_status(self):
        os.chdir(self.ROOT_DIR)
        if os.path.isfile(self.filename):
            self.status = 200
        else:
            self.status = 404

    def send_file(self):
        with open(self.filename, mode="rb") as f:
            data = f.read(1024)
            while data:
                self.conn.send(data)
                print(data)
                data = f.read(1024)


webServer = StaticWebServer()
webServer.runserver()
