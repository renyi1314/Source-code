from multiprocessing import Pool
import time


def genProcess(num):
    print("这是第一种进程{}".format(num))


def genProcess2(num):
    print("这是第二种进程{}".format(num))


p = Pool(10)
for i in range(100):
    p.apply_async(genProcess, (i,))
    p.apply_async(genProcess2,(i,))
print("start----")
p.close()
p.join()
