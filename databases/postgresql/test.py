import psycopg2

conn = psycopg2.connect(database="test", user="postgres", password="postgres", host="192.168.133.133", port="5432")

db = conn.cursor()

db.execute("select * from t_warn_real_time")
data = db.fetchall()
for i in data:
    print(i)
