import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='Qwe@123456', database='itsource', charset='utf8')
link = conn.cursor()
link.execute('insert into message(name,content) values(%s,%s)', ("rye", "olo"))
conn.commit()
link.close()
conn.close()