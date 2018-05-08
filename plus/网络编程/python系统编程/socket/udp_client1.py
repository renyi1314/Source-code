import socket

ip_server = ("192.168.133.133",8888)
with socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM) as s:
    s.sendto('hello'.encode("utf-8"),ip_server)
