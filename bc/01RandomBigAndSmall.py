import random
from random import randint

res = []
for i in range(100):
    PerNumbers = [randint(0, 9) for i in range(6)]
    sumResult = sum(PerNumbers)
    if sumResult >= 23:
        tmp = "大"
    else:
        tmp = "小"
    res.append(tmp)

for i in res:
    if i == "大":
        print('\033[1;35m {} \033[0m'.format(i))
    else:
        print('\033[1;32;43m {} \033[0m!'.format(i))
