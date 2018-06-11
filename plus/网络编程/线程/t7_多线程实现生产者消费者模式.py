import threading
import random
import time

data = []



class Producer(threading.Thread):

    def __init__(self):
        super(Producer, self).__init__()
        self.lock = threading.Lock()

    def run(self):
        for i in range(5):
            self.lock.acquire()
            data.append(i)
            print("正在产生数据,已放入{},当前列表:{}".format(i, data))
            time.sleep(1)
            print("数据产生完成,当前列表:{}".format(data))
            self.lock.release()


class Consumer(threading.Thread):
    def __init__(self):
        super(Consumer, self).__init__()
        self.lock = threading.Lock()

    def run(self):
        for i in range(5):
            self.lock.acquire()
            print("正在取出数据{},当前列表:{}".format(i, data))
            a = data.pop(0)
            time.sleep(5)
            print("数据消费成功,当前列表:{}".format(data))
            self.lock.release()


producer = Producer()
consumer = Consumer()
producer.start()
consumer.start()
# producer.join()
# consumer.join()
