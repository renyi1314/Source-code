from functools import reduce


def sum_number(*args, **kwargs):
    result = reduce(lambda x, y: x + y, args) #构造函数得出结果
    print(result)
    # s = 0
    # for i in args:
    #     s+=i    # 方法2,循环args取值


if __name__ == "__main__":
    sum_number(5, 5, 1, 2, 6, 7, 22, 11)
