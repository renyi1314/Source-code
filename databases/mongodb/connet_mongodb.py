import pymongo




conn  = pymongo.MongoClient()
db = conn.database.collections
db.find()
db.insert()

