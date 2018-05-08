import threading

count = 0
l1 = threading.Lock()
l2 = threading.Lock()


def add1():
    global count
    for i in range(1000000):
        l1.acquire()
        count += 1
        l1.release()


def add2():
    global count
    for i in range(1000000):
        l2.acquire()
        count += 1
        l2.release()


t1 = threading.Thread(target=add1)
t2 = threading.Thread(target=add2)
t1.start()
t2.start()
t1.join()
t2.join()
print(count)
