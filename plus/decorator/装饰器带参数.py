def decor_fun(info):
    def decor(function):
        def wrapper(*args, **kwargs):
            print(info * 5)
            res = function(*args, **kwargs)
            print(info * 5)
            return res

        return wrapper

    return decor


@decor_fun(info="-----")
def fun():
    print("hello,world")
    return 2


fun()
print(fun())
