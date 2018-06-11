class Foo:

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


a = Foo("renyi")
b = Foo("zhangsan")

print(id(a))
print(id(b))
