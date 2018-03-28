class Foo:

    @staticmethod
    def f1():
        print("function 1")

    @staticmethod
    def f2():
        print("function 2")


class DecoratorFoo:

    def __init__(self, decorator):
        self._decorator = decorator

    def f1(self):
        print("decorator__foo")
        self._decorator.f1()


x = Foo()
y = DecoratorFoo(x)
y.f1()
