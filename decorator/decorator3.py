def foo():
    print("hello")


class decorator():
    def __init__(self, decorate_foo):
        self._decorate_foo = decorate_foo

    def foo(self):
        print("decorator")
        self._decorate_foo()


foo_decorator = decorator(foo)
foo_decorator.foo()
