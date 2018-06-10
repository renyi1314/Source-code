import pymysql


class OpeDb:
    def __init__(self, host="192.168.133.133", user="root", password="Qwe@123456", database="itsource", charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                    charset=self.charset)
        self.link = self.conn.cursor()

    def close(self):
        self.conn.close()
        self.link.close()

    def create(self, sql):
        self.link.execute(sql)

    def find(self, sql):
        self.link.execute(sql)
        data = self.link.fetchall()
        return data

    def insert(self, sql):
        self.conn.begin()
        try:
            self.link.execute(sql)
        except Exception as e:
            self.conn.rollback()
        else:
            self.conn.commit()


a = OpeDb()

# a.create(
#     "CREATE TABLE `news` (  `id` int(11) NOT NULL AUTO_INCREMENT, `title` varchar(100) DEFAULT NULL,`author` varchar(100) DEFAULT NULL,`content` varchar(100) DEFAULT NULL,`release_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,`click_rate` int(11) DEFAULT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;")
# a.insert('INSERT INTO news(title,author,content,click_rate) VALUES("天气1111","网易","今天天气晴",0),("天气1111","网易","今天天气晴",0)')
print(a.find("select * from news order by release_time limit 5"))
