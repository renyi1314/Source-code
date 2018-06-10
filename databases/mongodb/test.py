import pymongo


class MongoDbClass:
    def __init__(self, host="192.168.133.133", port=27017):
        self.host = host
        self.port = port
        self.conn = pymongo.MongoClient(host=self.host, port=self.port)
        self.db = self.conn.itsource.news

    def find(self):
        data = self.db.find()
        return data

    def insert(self, *args):
        self.db.insert(*args)


db = MongoDbClass()
db.insert([{"titile": "11111", "点击率": 122}, {"titile": "22222", "点击率": 222}, {"titile": "33333", "点击率": 33333},
           {"titile": "44444", "点击率": 444}, {"titile": "55555", "点击率": 55555}])
data = db.db.find().sort("点击率", -1)
for i in data:
    print(i)
