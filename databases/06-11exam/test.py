import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="Qwe@123456", database="itsource",charset='utf8')
db = conn.cursor()
db.execute("SELECT * FROM product WHERE pro_name LIKE '%华为%';")
data = db.fetchall()
print(data)
