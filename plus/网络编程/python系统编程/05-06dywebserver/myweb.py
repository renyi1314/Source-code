import socket
from multiprocessing import Process
import pprint
import os
import mimetypes


class StaticWebSever(object):
    ROOT_DIR = '.'
    STATUS_CODE = {200: 'OK', 404: 'Not Found'}
    def __init__(self, port=8888, maxfd=5):
        self.listen_sock = socket.socket()
        self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_sock.bind(('', port))
        self.listen_sock.listen(maxfd)
        print("监听socket:{}对象成功".format(port))

        self.request_dict = {}          # 保存请求HTTP头的字段信息
        self.filename = ''              # 保存实际的文件路径

        self.response_dict = {'Server_name': 'PY_web', 'abc': 123}

        self.new_sock = socket.socket()

    def run_server(self):
        while True:
            self.new_sock, _ = self.listen_sock.accept()
            print("有一个新链接...")
            p1 = Process(target=self.process_handler)
            p1.start()
            self.new_sock.close()               # 有新的进程维护了新链接,服务器进程没有必要保留

    # 循环接收请求头信息
    def _recv_request_header(self):
        buf = self.new_sock.recv(100)
        while buf.find(b'\r\n\r\n') == -1:
            buf += self.new_sock.recv(100)
        return buf.decode('utf-8')

    # 解析请求字符串,转换为字典类型
    def _parse_request(self, buf):
        datas = buf.splitlines()
        head = datas[0]
        num = 1
        self.request_dict['method'] = head.split(' ')[0].strip()
        self.request_dict['name'] = head.split(' ')[1].strip()
        while num < len(datas):
            item = datas[num].split(':')
            if len(item) == 2:
                k = item[0].strip()
                self.request_dict[k] = item[1].strip()
            num += 1

    def _check_file(self):
        filename = '{}{}'.format(self.ROOT_DIR, self.request_dict['name'])
        if os.path.isfile(filename):
            self.filename = filename
            return 200
        else:
            return 404

    def send_response(self, status):
        response_header = 'HTTP/1.1 {} {}\r\n'.format(status, self.STATUS_CODE[status])
        # 字典转换为字符串
        tmp = ['{}: {}\r\n'.format(k, v) for k, v in self.response_dict.items()]
        response_data = ''.join(tmp)
        data = '{}{}\r\n'.format(response_header, response_data)
        self.new_sock.send(data.encode('utf-8'))

    def send_file(self):
        with open(self.filename, 'rb') as fp:
            buf = fp.read(1024)
            while buf:
                self.new_sock.send(buf)
                buf = fp.read(1024)

    def _set_response_header(self, k, v):
        self.response_dict[k] = v

    def _set_content_type(self):
        value = mimetypes.guess_type(self.filename)[0]
        self._set_response_header('Content-Type', value)

    def old(self, code_str, response_list):
        response_header = 'HTTP/1.1 {}\r\n'.format(code_str)
        tmp = ['{}: {}\r\n'.format(x[0], x[1]) for x in response_list]
        response_data = ''.join(tmp)
        data = '{}{}\r\n'.format(response_header, response_data)
        self.new_sock.send(data.encode('utf-8'))

    def process_handler(self):
        buf = self._recv_request_header()
        self._parse_request(buf)
        pprint.pprint(self.request_dict)
        if self.request_dict['name'].startswith('/static/'):
            status = self._check_file()
            if status != 200:
                self.send_response(status)
            else:
                # 构造响应头
                self._set_content_type()
                self.send_response(status)
                self.send_file()
        else:
            from mydjango.mywsgi import applictaion
            cnt = applictaion(self.request_dict, self.old)
            self.new_sock.send(cnt.encode('utf-8'))
        self.new_sock.close()

def main_process():
    server = StaticWebSever()
    server.run_server()


if __name__ == '__main__':
    main_process()
