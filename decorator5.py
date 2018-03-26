class decorator():
    def __init__(self,level='INFO'):
        self.level=level

    def __call__(self,fun):
        def wrapper(*args,**kwargs):
            print(self.level)
            fun(*args,**kwargs)
        return wrapper

@decorator(level="INFO")
def foo():
    print("hello")