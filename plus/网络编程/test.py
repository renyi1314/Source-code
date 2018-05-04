import struct
import json

ver = 1
body = json.dumps(dict(hello="world"))
print(body)
cmd = 101
header = [ver, body.__len__(), cmd]
headPack = struct.pack("!3I", *header)