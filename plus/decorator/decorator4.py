class Decorator():

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("DEBUG")
        return self.func(*args, **kwargs)


@Decorator
def foo():
    print("Test")


foo()
