import socket
import threading

def init_listen_sock(port, maxfd=3):
    tsock = socket.socket()
    tsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tsock.bind(('', port))
    tsock.listen(maxfd)
    return tsock

# 子线程处理新连接
def thread_handler(nsock):
    raw_data = nsock.recv(1024)
    while raw_data:
        print(f"收到{raw_data.decode('utf-8')} 内容")
        raw_data = nsock.recv(1024)
    nsock.close()


def main_handler():
    listen_sock = init_listen_sock(8888)
    while True:
        nsock, _ = listen_sock.accept()
        print(f"一个新的连接{nsock}")
        client_pid = threading.Thread(target=thread_handler, args=(nsock,))
        client_pid.start()
        # nsock.close()

if __name__ == '__main__':
    main_handler()