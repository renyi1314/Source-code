def foo():
    print("hello")


class Decorator:
    def __init__(self, decorate_foo):
        self._decorate_foo = decorate_foo

    def foo(self):
        print("decorator")
        self._decorate_foo()


foo_decorator = Decorator(foo)
foo_decorator.foo()
