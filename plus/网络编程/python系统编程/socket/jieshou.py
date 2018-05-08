import socket


fu = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
fu.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
add = ("", 6688)
fu.bind(add)
data, shouji = fu.recvfrom(1024)
print("获得到{}从{}".format(data.decode("utf-8"), shouji))