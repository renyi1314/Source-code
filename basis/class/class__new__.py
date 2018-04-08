class Foo():

    def __init__(self):
        print("This is init func")

    def __new__(cls, *args, **kwargs):
        print("This is new func")
        return super(Foo, cls).__new__(cls) #返回类的实例化对象
        # return object.__new__(cls)


obj1 = Foo()
