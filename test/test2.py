import threading


class A:
    def __init__(self):
        self.num = 1

    def add_num(self, num):
        for _ in range(100000):
            self.num += num
        return self.num


a = A()

t1 = threading.Thread(target=a.add_num, args=[1, ])
t2 = threading.Thread(target=a.add_num, args=[1, ])
t1.start()
t2.start()
print(a.num)
