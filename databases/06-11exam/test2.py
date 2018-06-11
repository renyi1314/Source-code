import pymongo

conn = pymongo.MongoClient()
db = conn.itsource.user
data = db.find()
for i in data:
    print(i)
