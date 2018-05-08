import socket

host = '192.168.133.133'
port = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    with open('123', 'rb') as f:
        while True:
            data = s.recv(1024*4)
            f.write("423423")
            if not data:
                break

print('Recevied', repr(data))