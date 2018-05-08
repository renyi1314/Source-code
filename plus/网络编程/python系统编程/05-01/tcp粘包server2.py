import socket
import struct

# header = ["hehe","one","two"]
# a = struct(*header)
# print(a)
# local_address = ("192.168.133.133", 8888)
# with socket.socket() as s:
#     s.bind(local_address)
#     s.listen(5)
#     conn, adress = s.accept()
#     data = conn.recv(1024)
#     print(data)

import struct
import json

ver = 1
body = json.dumps(dict(hello="world"))
print(body)  # {"hello": "world"}
cmd = 101
header = [ver, 99, cmd]
headPack = struct.pack("!3I", *header)
print(headPack)  # b'\x00\x00\x00\x01\x00\x00\x00\x12\x00\x00\x00e'
print(body.__len__())
