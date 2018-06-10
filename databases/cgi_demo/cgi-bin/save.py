#!C:\Python3\python.exe


# cgi模块
import cgi, cgitb
import pymysql

# 接收form数据
form = cgi.FieldStorage()
# 获取输入内容
username = form.getvalue('username')
content = form.getvalue('content')
# print(username, content)
# 将数据插入数据库
conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='itsource', charset='utf8')
link = conn.cursor()
link.execute('insert into message values(%s,%s)', (username, content))
link.close()
conn.close()
print("Content-Type:text/html;charset=gbk")
print()
print(f"<script>alert('留言成功,用户名:{username},内容:{content}');location.href='/index.html';</script>")