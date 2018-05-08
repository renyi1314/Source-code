import socket
udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
add = ("192.168.133.133",6688)
me ="kdlhfj"
udp_server.sendto(me.encode("utf-8"), add)