"""

"""
from multiprocessing import Process
import socket
import os
import mimetypes


class DyWebServer(object):
    ROOT_DIR = '.'
    RESPONSE_TABLE = {'200': 'OK', '404': 'Not Found'}

    def __init__(self, port, maxfd=5):
        self.listen_sock = socket.socket()      # 监听socket对象
        self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_sock.bind(('', port))
        self.listen_sock.listen(maxfd)

        self.server_name = 'WHN_webserver'

        self.client_sock = socket.socket()      # 客户端新连接的socket对象
        self.client_sock.close()

        self.request_dict = {}                  # 客户端发起的http请求头字典结构

        self.filename = ''                      # 客户端请求的文件名绝对路径

        self.response_dict = {}                 # 客户端响应头字典结构
        os.chdir(self.ROOT_DIR)

    def forever(self):
        while True:
            self.client_sock, _ = self.listen_sock.accept()
            print("一个新的连接到来了", self.client_sock)
            # 创建一个新进程来处理这个连接
            p1 = Process(target=self.client_handler)
            p1.start()
            self.client_sock.close()

    def _add_response(self, key, value):
        self.response_dict[key] = value

    def client_handler(self):
        # 接收请求头
        request_data = self.client_sock.recv(2048)
        # 解析请求头
        self._parse_header(request_data.decode('utf-8'))
        # 获得请求文件信息
        status = self._get_request_file()
        # 判断请求状态
        if status == 800:
            from py_web.mywsgi import application
            cnt = application(self.request_dict, self.start_response)
            self.client_sock.send(cnt.encode('utf-8'))
        else:
            # 设置响应文件类型
            self._set_resp_type()
            # 根据状态值，构造响应头
            self.send_response(200)
            self.send_file()

        self.client_sock.close()

    # 判断用户请求的是静态文件还是动态内容
    def _get_request_file(self):
        if self.request_dict['name'].startswith('/static/'):
            # 静态内容
            self.filename = self.request_dict['name'][1:]
            if os.path.isfile(self.filename):
                return 200
        else:
            return 800

    # wsgi的回调函数
    def start_response(self, status, response_headers):
        self._add_response('Server_info', self.server_name)
        for item in response_headers:
            self._add_response(item[0], item[1])
        self.send_response(status)

    # 发送响应头
    def send_response(self, status):
        h1 = 'HTTP/1.1 {} {}\r\n'.format(status, self.RESPONSE_TABLE[str(status)])
        cnt_list = ['{}: {}\r\n'.format(k, v) for k, v in self.response_dict.items()]
        cnt = ''.join(cnt_list)
        response_header = '{}{}\r\n'.format(h1, cnt)
        self.client_sock.send(response_header.encode('utf-8'))

    # 构造Content-type的响应字段
    def _set_resp_type(self):
        ends = os.path.splitext(self.filename)[1]
        self._add_response('Content-Type', mimetypes.types_map[ends])

    # 发送文件内容
    def send_file(self):
        with open(self.filename, 'rb') as fp:
            buf = fp.read(1024)
            while buf:
                self.client_sock.send(buf)
                buf = fp.read(1024)

    # 解析请求头
    def _parse_header(self, request_data):
        # 将数据包按行进行拆分，以列表形式进行后续处理
        req_lists = request_data.splitlines()
        # 逐行处理HTTP的请求头信息
        for x in req_lists:
            if x.find(': ') != -1:
                tmp_list = x.split(': ')
                self.request_dict[tmp_list[0]] = tmp_list[1].strip()
            elif x.find('HTTP/1.1') != -1:
                tmp_header = x.split(' ')
                self.request_dict['method'] = tmp_header[0]
                self.request_dict['name'] = tmp_header[1]


if __name__ == '__main__':
    w1 = DyWebServer(8080)
    w1.forever()
