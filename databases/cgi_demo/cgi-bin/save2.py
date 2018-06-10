#!C:\Python3\python.exe


# cgi模块
import cgi, cgitb
import pymysql
import json

# 接收form数据
form = cgi.FieldStorage()
# 获取输入内容
username = form.getvalue('username')
content = form.getvalue('content')
# 将数据插入数据库
conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='itsource', charset='utf8')
link = conn.cursor()
link.execute('insert into message values(%s,%s)', (username, content))
link.close()
conn.close()
data = {"status": 200}
print("Content-Type:application/json;charset=utf-8")
print()
print(json.dumps(data))
