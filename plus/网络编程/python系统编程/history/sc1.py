import socket

# host = '192.168.133.133'
host = "172.16.17.253"
port = 8889

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'abbbb')
    data = s.recv(1024)
print('Recevied', repr(data))
