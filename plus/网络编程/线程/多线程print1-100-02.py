import threading

buf = ''
lock1 = threading.Lock()
lock2 = threading.Lock()


def user_input_thread():
    while True:
        lock1.acquire()
        print("aaaaaa")
        lock2.release()


def parse_data_thread():
    while True:
        lock2.acquire()
        print("bbbb")
        lock1.release()


# 主任务
def main_process():
    t1 = threading.Thread(target=user_input_thread)
    t2 = threading.Thread(target=parse_data_thread)
    lock2.acquire()
    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    main_process()
