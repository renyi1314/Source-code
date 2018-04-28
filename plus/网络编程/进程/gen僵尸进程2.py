from multiprocessing import Process
import time
import os
def test():
    input("")

def fun():
    t = Process(target=fun, name="testfun")
    t.start()
    print("ppid:{},pid:{},实例id:{}".format(os.getppid(), os.getpid(), p.pid))
    time.sleep(100)

p = Process(target=fun, name="testfun")
print("process实例名称:{}".format(p.name))
p.start()
