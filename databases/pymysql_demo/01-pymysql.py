 # encoding-utf-8
import pymysql

# import MySQLdb

# db = pymysql.connect()

# with pymysql.connect('192.168.133.133', 'root', 'Tansun@123456', 'itsource', charset='utf8') as db:
#
#     print(db)
#     print(dir(db))
#
#     link = db.cursor()
#     link.execute('select * from student')
#     data = link.fetchall()
#     print(type(data[1][1]))
#     print(data)
db = pymysql.connect(host='192.168.133.133', user='root', password='Tansun@123456', database='itsource', charset='utf8')

print(db)
print(dir(db))

link = db.cursor()
link.execute('select * from student')
data = link.fetchall()
print(type(data[1][1]))
print(data)
