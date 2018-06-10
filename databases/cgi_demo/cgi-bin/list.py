#!C:\Python3\python.exe
import pymysql
import json

conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='itsource', charset='utf8')
link = conn.cursor()
link.execute('select * from message')
data = link.fetchall()
print("Content-Type:application/json;charset=utf-8")
print()
print(json.dumps(data))
link.close()
conn.close()
