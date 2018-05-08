import threading

buf = ""
l1 = threading.Lock()
l2 = threading.Lock()


def wait_input():
    global buf
    while True:
        l1.acquire()
        buf = input("请输入内容:-----")
        l2.release()


def check_input():
    global buf
    while True:
        l2.acquire()
        count = 0
        for x in buf:
            if x.isdigit():
                count += 1
        print("用户输入字符中含有{}个数字".format(count))
        l1.release()


l2.acquire()
t1 = threading.Thread(target=wait_input)
t2 = threading.Thread(target=check_input)

t1.start()
t2.start()
