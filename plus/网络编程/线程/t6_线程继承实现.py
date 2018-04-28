import threading


class Genthread(threading.Thread):
    def __init__(self):
        super(Genthread, self).__init__()

    def run(self):
        print("Thread is running----{}".format(self.getName()))
        for i in range(10):
            print("Thread{}>>>>{}".format(self.getName(), i))
        print("Thread finish")


a = Genthread()
a.start()
