class Foo():
    def __init__(self, name):
        self.name = name

    @staticmethod
    def f1():
        print("normal f1")

    @staticmethod
    def f2():
        print("staticmethod f2")

    @classmethod
    def f3(cls):
        print("classmethod f3")


Foo.f3()
