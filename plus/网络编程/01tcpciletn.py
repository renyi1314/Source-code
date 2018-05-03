import socket

remote_address = ("192.168.133.133", 8888)
s = socket.socket()
s.connect(remote_address)
while True:
    data = input("input something")
    s.send(data.encode("utf-8"))
