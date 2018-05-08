import os
import time

rpid = os.fork()
if rpid < 0:
    print("fork调用失败。")
elif rpid == 0:
    time.sleep(2)
    print("我是子进程（%s），我的父进程是（%s）,rpid是(%s)" % (os.getpid(), os.getppid(), rpid))
    print("当前时间是{}".format(time.time()))
else:
    # time.sleep(1)
    print("我是父进程（%s），我的子进程是（%s）,rpid是(%s)" % (os.getpid(), rpid, rpid))
    print("当前时间是{}".format(time.time()))
    time.sleep(1)

#  123