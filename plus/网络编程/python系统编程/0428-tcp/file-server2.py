import socket
import os

local_address = ("192.168.133.133", 8888)


def send_file():
    with socket.socket() as s:
        s.bind(local_address)
        s.listen(5)
        conn, address = s.accept()
        with conn:
            filename = conn.recv(1024)
            print(filename)
            if filename[0] =="1":
                print("hello,world")
            with open(filename.decode("utf-8"), mode="rb") as f:
                data = f.read(1024)
                while data:
                    conn.send(data)
                    data = f.read(1024)


def send_listdir():
    with socket.socket() as s:
        s.bind(local_address)
        s.listen(5)
        conn, address = s.accept()
        with conn:
            list_dir = str(os.listdir())
            print(list_dir)
            conn.send(list_dir.encode("utf-8"))


def recive_file():
    with socket.socket() as s:
        s.bind(local_address)
        s.listen(5)
        conn, address = s.accept()
        with conn:
            filename = conn.recv(7)
            print(filename)
            with open(filename.decode("utf-8"), mode="wb") as f:
                data = conn.recv(1024)
                while data:
                    f.write(data)
                    data = conn.recv(1024)


send_file()
