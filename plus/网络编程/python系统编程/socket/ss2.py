import socket

host = '192.168.133.133'
port = 9999
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print("Connected By", addr)
        with open("123", 'rb') as f:
            while True:
                data = f.read()
                conn.sendall(b"12345")
                if not data:
                    break