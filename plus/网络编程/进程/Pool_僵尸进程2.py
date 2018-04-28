import time
from multiprocessing import Pool


def genProcess(n):
    print("Test---{n}".format(n))
    time.sleep(1)

p = Pool(10)
for i in range(100):
    p.apply_async(genProcess, (i,))

p.close()
p.join()
