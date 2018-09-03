import threading
import time

locka = threading.Lock()
lockb = threading.Lock()
a = 0
list_a = []


def fun_a():
    global a
    while a < 100:
        locka.acquire()
        print("fun_a is {}".format(a))
        a += 1
        list_a.append(a)
        lockb.release()


def fun_b():
    global a
    while a < 100:
        lockb.acquire()
        print("fun_b is {}".format(a))
        list_a.append(a)
        locka.release()


lockb.acquire()
t1 = threading.Thread(target=fun_a)
t2 = threading.Thread(target=fun_b)

t1.start()
t2.start()
t1.join()
t2.join()
print(list_a)
