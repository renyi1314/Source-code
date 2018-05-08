from multiprocessing import Process,process
import time
import os

def fun():
    print("ppid:{},pid:{},实例id:{}".format(os.getppid(), os.getpid(), p.pid))
    time.sleep(100)

p = Process(target=fun, name="testfun")
print("process实例名称:{}".format(p.name))
p.start()
p.start()
p.start()
p.start()