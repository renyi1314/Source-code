from multiprocessing import Process
import os
import time


class GenProcess(Process):
    def __init__(self):
        Process.__init__(self)

    def run(self):
        print("子进程id:{},父进程id:{}".format(os.getpid(), os.getppid()))
        time.sleep(10)


a = GenProcess()
a.start()
