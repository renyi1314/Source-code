import socket
from multiprocessing import Process


class TCPBaseSocketServer:

    def __init__(self, port=8888, max_listen=5):
        self.listen_socket = socket.socket()
        self.listen_socket.bind(("", port))
        self.listen_socket.listen(max_listen)
        self.conn = socket.socket()

    def run_server(self):
        while True:
            self.conn, add = self.listen_socket.accept()
            print("有客户端新进连接了,地址为{}".format(add))
            p1 = Process(target=self.process_handle)
            p1.start()
            self.conn.close()

    def process_handle(self):
        data = self.conn.recv(1024)
        while data:
            print(data.decode("utf-8"))
            data = self.conn.recv(1024)
        self.conn.close()


def main_process():
    server = TCPBaseSocketServer()
    server.run_server()


if __name__ == '__main__':
    main_process()
