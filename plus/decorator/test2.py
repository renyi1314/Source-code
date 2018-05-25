class Foo:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance


a = Foo()
b = Foo()

print(id(a), id(b), a is b)
