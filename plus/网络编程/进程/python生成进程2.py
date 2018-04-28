from multiprocessing import Process
import time
import os

def fun():
    print("ppid:,pid:,实例id:")
    time.sleep(100)

p = Process(target=fun, name="testfun")
print("process实例名称:")
p.start()
p.start()
p.start()
p.start()
