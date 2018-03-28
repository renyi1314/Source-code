class foo():
    def __init__(self, name):
        self.name = name

    @staticmethod
    def f1(self):
        print("normal f1")

    @staticmethod
    def f2():
        print("staticmethod f2")

    @classmethod
    def f3(cls):
        print("classmethod f3")


foo.f3()
