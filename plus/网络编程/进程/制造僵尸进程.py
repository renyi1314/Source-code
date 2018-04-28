import os
import time

rpid = os.fork()
if rpid == 0:
    print("Child process")
elif rpid > 1:
    print("P process")
    input("---------")
