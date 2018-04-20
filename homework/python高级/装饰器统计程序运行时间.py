import datetime


def collect_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        res = func(*args)
        end_time = datetime.datetime.now()
        print(end_time - start_time)
        return res

    return wrapper


@collect_time
def fun(num):
    return sum(i ** 2 for i in range(num))


print(fun(1000000))
