def consumer():
    i = 0
    while True:
        tmp = yield i
        print("我是消费者: {}".format(tmp))


def producer(gen, n):
    gen.__next__()
    for i in range(n):
        print("我是生产者: {}".format(i))
        gen.send(i)


gen = consumer()
producer(gen, 5)
