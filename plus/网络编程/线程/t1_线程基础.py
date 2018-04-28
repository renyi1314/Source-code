import threading
import time
import random


def GenThread(msg):
    print("线程{}执行开始".format(msg))
    print(threading.currentThread(),threading.currentThread().name,threading.currentThread().ident)
    time.sleep(1)
    print("线程{}执行结束".format(msg))

for i in range(100):
    t = threading.Thread(None,target=GenThread,name=None,args=(i, ))
    t.start()
    time.sleep(1)
input()