import time


def func_time(func):
    def dec(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(str(func), end_time - start_time)
        return res

    return dec


@func_time
def fn1():
    li = []
    for i in range(10000):
        li.insert(-1, i)


@func_time
def fn2():
    li = []
    for i in range(10000):
        li.append(i)


@func_time
def fn3():
    li = []
    for i in range(10000):
        li = li + [i]


fn1()
fn2()
fn3()
