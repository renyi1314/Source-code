def consumer():
    last = ''
    while True:
        receival = yield last
        print('Consume %s' % receival)


def producer(gen, n):
    # gen.__next__()
    x = 0
    while x < n:
        x += 1
        print('Produce %s' % x)
        gen.__next__()
        # print(gen.__next__())
        # gen.send(x)


gen = consumer()
producer(gen, 5)
