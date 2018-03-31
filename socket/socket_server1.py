import socket

host = '192.168.133.133'
port = '8888'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print("Connected By", addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
