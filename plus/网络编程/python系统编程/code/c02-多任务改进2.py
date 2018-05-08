import threading
# 如何解决听音乐和烧开水的问题
import time


# 全局变量,代表经验值
exp = 0

# 听音乐,花费时间3秒
def do_music():
    global exp
    print("开始听音乐...")
    for x in range(3):
        exp += 1
        # print("在听音乐的时候,经验值{}".format(exp))
        time.sleep(1)
    print("听音乐结束...")

# 烧开水,花费时间5秒
def do_kaishui():
    print("开始烧开水...")
    for x in range(5):
        time.sleep(1)
        print("我的经验值是{}".format(exp))
    print("水已经烧开...")

# 如何安排事情的执行
def task1():
    start_time = time.time()
    do_kaishui()
    do_music()
    end_time = time.time()
    print("做事情,总共花费了{}秒".format(end_time - start_time))


def task2():
    start_time = time.time()
    p1 = threading.Thread(target=do_music)
    p2 = threading.Thread(target=do_kaishui)

    # 让任务开始运行
    p1.start()
    p2.start()

    # 等待所有任务执行完成,主进程才进行最后的统计
    p1.join()
    p2.join()

    end_time = time.time()
    print("做事情,总共花费了{}秒".format(end_time - start_time))

if __name__ == '__main__':
    task2()
