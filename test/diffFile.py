import difflib
import sys

textfile1 = "uwsgi.ini"
# textfile2 = sys.argv[2]
textfile2 = "uwsgi2.ini"


def readFile(filename):
    with open(filename, encoding="utf-8", mode="r") as fileHandle:
        text = fileHandle.read()
        fileHandle.close()
    return text


text1 = readFile(textfile1)
text2 = readFile(textfile2)
diff = difflib.Differ()

res = diff.compare(text1.splitlines(), text2.splitlines())
for item in res:
    if item.startswith(("+", "-", "?", "^")):
        print(item)
print("""
说明:
 - 	包含在第一个系列行中，但不包含第二个。
 + 	包含在第二个系列行中，但不包含第一个。
 "" 两个序列行一致(已过滤)
 ? 	标志两个序列行存在增量差异
 ^ 	标志着两个序列行存在的差异字符
 """)
# print('\n'.join(list(res)))
# print("aaaa\n12\t32\r1".splitlines())
# import os
from IPy import IP
