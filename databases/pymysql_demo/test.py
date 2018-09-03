import pymysql

conn = pymysql.connect(host='192.168.133.133', user='root', password='Qwe@123456', database='test', charset='utf8')
link = conn.cursor()
link.execute('insert into message(name,content) values(%s,%s)', ("rye", "olo"))
conn.commit()
link.close()
conn.close()
