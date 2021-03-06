class Decorator():
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, fun):
        def wrapper(*args, **kwargs):
            print(self.level)
            fun(*args, **kwargs)

        return wrapper


@Decorator(level="INFO")
def foo():
    print("hello")
