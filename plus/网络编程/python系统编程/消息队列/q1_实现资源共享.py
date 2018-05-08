from multiprocessing import Queue
import threading
import time
q = Queue()


class Producer(threading.Thread):

    def __init__(self):
        super(Producer, self).__init__()
        self.data = q

    def run(self):
        for i in range(5):
            self.data.put(i)
            print("正在产生数据,已放入{}".format(i))
            time.sleep(1)
            print("数据产生完成")


class Consumer(threading.Thread):
    def __init__(self):
        super(Consumer, self).__init__()
        self.data = q
    def run(self):
        for i in range(5):
            a =self.data.get()
            print("正在取出数据{}".format(a))
            time.sleep(2)
            print("数据消费成功")


producer = Producer()
consumer = Consumer()
producer.start()
consumer.start()
producer.join()
consumer.join()