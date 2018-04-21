import random
import datetime


class Lottery:
    def __init__(self):
        self.list_shuangseqiu = []
        self.caipiao_file = datetime.datetime.today().strftime("%Y-%m-%d") + ".txt"

    def kaijiang(self):
        self.list_shuangseqiu = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
        with open(self.caipiao_file, 'a') as f:
            f.write(datetime.datetime.today().strftime("%Y-%m-%d"))
            f.write(str(self.list_shuangseqiu))
        return self.list_shuangseqiu


a = Lottery()
print(a.kaijiang())
