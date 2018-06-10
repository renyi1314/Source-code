import pymongo
import pprint


class Mongo(object):
    def __init__(self, user, pwd, addr, port):
        self.user = user
        self.pwd = pwd
        self.addr = addr
        self.port = port
        self.client = ""

    def connet(self):
        # 数据库地址
        uri = "mongodb://" + self.user + ":" + self.pwd + "@" + self.addr + ":" + self.port
        # 连接数据库
        print(uri)
        try:
            self.client = pymongo.MongoClient(uri)
            print("连接成功")
        except Exception as e:
            print(e)
            print("0")
            return

    def addtext(self, dbse, coll):
        self.connet()

        db = self.client.dbse
        db.coll.insert_many([
            {"id": 1, "name": "小明", "age": 12, "height": 154, "score": 85},
            {"id": 2, "name": "小红", "age": 11, "height": 164, "score": 98},
            {"id": 3, "name": "小花", "age": 10, "height": 144, "score": 45},
        ])
        return True


mongo = Mongo("root", "litao123456789", "127.0.0.1", "27017")
print(mongo.addtext(dbse=1, coll=2))