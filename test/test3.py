import time
from concurrent.futures import ThreadPoolExecutor

import pymongo

executor = ThreadPoolExecutor(max_workers=3)

# with pymongo.MongoClient("192.168.133.133", port=27017, connect=False) as client:
# collection = client.xwlog.test
# collection.insert({"name": "renyi"})
# for i in range(100):

# def coll():
#     with pymongo.MongoClient("192.168.133.133", port=27017, connect=False) as client:
#         collection = client.xwlog.test
#         collection.insert({"name": "renyi"})
client = pymongo.MongoClient("192.168.133.133", port=27017)


def coll():
    collection = client.xwlog.test
    collection.insert({"name": "renyi"})


a = time.time()
for i in range(10000):
    executor.submit(coll)

print(time.time() - a)
