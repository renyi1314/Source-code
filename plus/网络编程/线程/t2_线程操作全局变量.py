import threading
import time

var = 0


def GenThread1(msg):
    global var
    print("第一个线程{}开始执行,var目前值为{}".format(msg, var))
    var += 1
    time.sleep(1)
    print("第一个线程{}执行结束,var目前值为{}".format(msg, var))


def GenThread2(msg):
    global var
    print("第二个线程{}开始执行,var目前值为{}".format(msg, var))
    var += 100
    time.sleep(1)
    print("第二个线程{}执行结束,var目前值为{}".format(msg, var))



for i in range(10):
    t1 = threading.Thread(target=GenThread1, args=(i,))
    t2 = threading.Thread(target=GenThread2, args=(i,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    time.sleep(1)
