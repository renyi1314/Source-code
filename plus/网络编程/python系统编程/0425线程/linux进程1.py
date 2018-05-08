import os
import time

os.fork()
print("----------", end="\n")
time.sleep(1)
os.wait()