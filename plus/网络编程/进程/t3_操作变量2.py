import threading

value1 = 0
value2 = 0
v_lock = threading.Lock()


def writeValue():
    global value1
    global value2
    count = 0
    while True:
        count += 1
        with threading.Lock():
            value1 = count
            value2 = count


def readValue():
    while True:
        with threading.Lock():
            if value1 == value2:
                print("Value1 is :{}-----Value2 is:{}".format(value1, value2))


t1 = threading.Thread(target=writeValue)
t2 = threading.Thread(target=readValue)
t1.start()
t2.start()
t1.join()
t2.join()
