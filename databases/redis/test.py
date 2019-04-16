import redis

conn = redis.StrictRedis(host='192.168.133.133', port=6379)
dict_a = {"coin_name": "btc", "time": 110}
conn.sadd("test", dict_a)
a = 0
