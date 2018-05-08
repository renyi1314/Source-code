"""

"""

from multiprocessing import Process
from threading import Thread
import time

# IO密集型的代码
def fun():
    with open('1.txt', 'r') as fp:
        fp.read
    # 网络传输等

# CPU密集型的代码
def task1():
    cnt = 0 
    res = 0
    for x in range(1000000):
        cnt += 1
        res += cnt **2


def test2():
    plist = []
    start_time = time.time()
    for p in range(3):
        p = Process(target=task1)
        plist.append(p)
        p.start()
    for p in plist:
        p.join()
    end_time = time.time()
    print("进程调用, 运行时间:{}".format(end_time - start_time))

def test1():
    start_time = time.time()
    for x in range(3):
        task1()
    end_time = time.time()
    print("普通调用,运行时间:{}".format(end_time - start_time))

def test3():
    tlist = []
    start_time = time.time()
    for p in range(3):
        p = Thread(target=task1)
        tlist.append(p)
        p.start()
    for t in tlist:
        t.join()
    end_time = time.time()
    print("线程调用, 运行时间:{}".format(end_time - start_time))


if __name__ == '__main__':
    test1()
    test2()
    test3()
