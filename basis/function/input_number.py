from functools import reduce


def sum_number(*args, **kwargs):
    # s = 0
    # for i in args:
    #     s+=i
    # print(s)  $循环取值
    result = reduce(lambda x, y: x + y, args) #构造函数得出结果
    print(result)
    return result


sum_number(5, 5, 1, 2, 6, 7, 22, 11)
