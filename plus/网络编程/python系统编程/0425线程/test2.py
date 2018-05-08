import threading
import time



def GenThread(msg):
    print(threading.currentThread(),threading.currentThread().name,threading.currentThread().ident)


for i in range(100):
    t = threading.Thread(None,target=GenThread,name=None,args=(i, ))
    t.start()
input()