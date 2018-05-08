import socket

local_address = ("", 8888)
with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(local_address)
    s.listen(5)
    conn, address = s.accept()
    print("收到请求,来自于{}".format(conn))
    with conn:
        while True:
            data = conn.recv(1024)
            print("收到请求数据:{}".format(data.decode("utf-8")))
            send_data = input("输入回复的数据:")
            conn.send(send_data.encode("utf-8"))
