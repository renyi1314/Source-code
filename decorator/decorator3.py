def decorator(fun):
    def debug():
        print("DEBUG")
        return fun()
    return debug

@decorator
def foo():
    print("foo")

foo()