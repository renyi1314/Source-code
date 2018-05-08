import socket

local_address = ("192.168.133.133", 8888)
with socket.socket() as s:
    s.bind(local_address)
    s.listen(5)
    conn, adress = s.accept()
    data = conn.recv(1024)
    print(data)