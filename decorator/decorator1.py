def debug(func):
    def decorator(*args, **kwargs):
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func(*args, **kwargs)
    return decorator


@debug
def say_hello():
    print("say hello")


n = 1
say_hello()
