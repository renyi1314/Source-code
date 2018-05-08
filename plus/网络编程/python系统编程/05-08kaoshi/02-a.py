import random


def random_num():
    list_gt_zero = []
    for i in range(15):
        num = random.randrange(-30, 31)
        if num > 0:
            list_gt_zero.append(num)
    return list_gt_zero


if __name__ == '__main__':
    a = random_num()
    print(sorted(a))
    print(a)
