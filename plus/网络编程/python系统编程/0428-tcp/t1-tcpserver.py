import socket

local_address = ("", 8888)
with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
    s.bind(local_address)
    s.listen(5)
    conn, address = s.accept()
    with conn:
        data = conn.recv(1024)
        print(data)
        # print(conn.recv(1024), address)

    input("----")
