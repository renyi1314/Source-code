'''
1.初始化对象
2.接收请求并解析
3.发送

'''

import socket
from multiprocessing import Process
import os
import mimetypes

class StaticWebServer:
    ROOT_DIR = "."
    RESPONSE_TABLE = {200: "OK", 404: "NOT FOUND"}


    def __init__(self, port=8888, max_listen=5):
        self.listen_socket = socket.socket()
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_socket.bind(("", port))
        self.listen_socket.listen(max_listen)
        self.filename = ""
        self.status = ""
        self.response_dict = {}
        self.response_headers = ""

    # 接收请求并解析
    def get_parse_header(self):
        data = self.conn.recv(1024).decode("utf-8")
        self.filename = data.splitlines()[0].split()[1][1:]


    def status_file(self):
        os.chdir(self.ROOT_DIR)
        if os.path.isfile(self.filename):
            self.status = 200
        else:
            self.status = 404

    def gen_response_headers(self):
        self.response_dict["status"] = self.status
        self.response_dict["Content-Type"] = mimetypes.guess_type(self.filename)[0]
        self.response_headers = "HTTP/1.1 {} {}\r\n".format(self.status, self.RESPONSE_TABLE[self.status])
        data = ['{}: {}\r\n'.format(k, v) for k, v in self.response_dict.items()]
        datas = "".join(data)
        self.response_data = "{}{}\r\n".format(self.response_headers, datas)



    def send_file(self):
        with open(self.filename,mode="rb") as f:
            data = f.read(1024)
            while True:
                self.conn.send(data)
                data = f.read(1024)

    def server_handler(self):
        self.get_parse_header()
        self.status_file()
        self.gen_response_headers()
        self.conn.send(self.response_data.encode("utf-8"))
        if self.status == 200:
            self.send_file()


    def runserver(self):
        while True:
            self.conn, _ = self.listen_socket.accept()
            print("有新连接:{},地址为:{}".format(self.conn, _))
            p1 = Process(target=self.server_handler)
            p1.start()


server = StaticWebServer()
server.runserver()