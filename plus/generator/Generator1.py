def consumer():
    last = ''
    while True:
        receival = yield last
        if receival is not None:
            print('Consume %s' % receival)
            last = receival


def producer(gen, n):
    gen.__next__()
    x = 0
    while x < n:
        x += 1
        print('Produce %s' % x)
    gen.close()


gen = consumer()
producer(gen, 5)
