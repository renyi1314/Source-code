import socket


local_address = ("", 8888)

with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(local_address)
    s.listen(5)
    conn, address = s.accept()
    with conn:
        while True:
            re_data = conn.recv(1024)
            filename = re_data.decode("utf-8")
            with open(filename, "rb") as f:
                data = f.read(1024**3)
                while data:
                    conn.send(data)
                    data = f.read(1024**3)

