import pymysql

conn = pymysql.connect(host="192.168.133.133", user="root", password="Qwe@123456", database="itsource", charset='utf8')

with conn.cursor() as link:
    # link.execute("DROP TABLE IF EXISTS news")
    # link.execute("CREATE TABLE news (  id int(11) NOT NULL AUTO_INCREMENT,  title varchar(100) DEFAULT NULL,  author varchar(100) DEFAULT NULL,  content varchar(100) DEFAULT NULL,  release_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,  click_rate int(11) DEFAULT NULL,  PRIMARY KEY (id)) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8")
    # link.execute(
    #     "CREATE TABLE `news` (  `id` int(11) NOT NULL AUTO_INCREMENT, `title` varchar(100) DEFAULT NULL,`author` varchar(100) DEFAULT NULL,`content` varchar(100) DEFAULT NULL,`release_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,`click_rate` int(11) DEFAULT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;")
    # username = "大乔"
    # age = "21"
    # link.execute("select * from student where name=%s and age = %s", (username, age))
    # data = link.fetchone()
    # print(data)
    # data = link.fetchall()
    # print(data)
    # link.executemany("insert into news(title,author,content,release_time,click_rate)values(%s,%s,%s)",[("天气", "网易", "今天天气晴", "default", "0"), ("天气2", "网易2", "今天天气晴2", "default", "0")])
    # sql_insert = ''''''
    # link.execute(
    #     'INSERT INTO news(title,author,content,click_rate) VALUES("天气1111","网易","今天天气晴",0),("天气1111","网易","今天天气晴",0);')
    # conn.commit()
    # link.execute()
    conn.begin()
    try:
        username = "大乔"
        age = "21"
        link.execute("select * from student where name=%s and age = %s", (username, age))
    except Exception as e:
        conn.rollback()
    else:
        conn.commit()
