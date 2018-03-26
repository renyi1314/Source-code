class foo():

    def f1(self):
        print("function 1")

    def f2(self):
        print("function 2")

class decorator__foo():

    def __init__(self,decorator):
        self._decorator=decorator

    def f1(self):
        print("decorator__foo")
        self._decorator.f1()

x=foo()
y=decorator__foo(x)
y.f1()