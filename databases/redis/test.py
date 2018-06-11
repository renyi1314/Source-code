import redis

# conn = redis.Connection(host='localhost', port=6379)
conn = redis.StrictRedis(host='localhost', port=6379)
# conn.set("name", "zhjangsan")
# conn.lpush("list", "rew")
# conn.rpush("list", "1")
# for i in range(10000):
#     conn.rpush("list", i)
# while True:
#     conn.lpop("list")
pi = conn.pipeline()
pi.set("name", "zs")
pi.set("age", 18)
# pi.set("name2")
pi.execute()
