import socket

with socket.socket() as s:
    s.bind(("192.168.133.133", 8888))
    s.listen(5)
    conn = s.accept()
    data = conn.recv(1024)
    print(data)
