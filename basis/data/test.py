def singe_class(cls):
    instance = {}

    def wrap(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrap


@singe_class
class Foo:
    pass


a = Foo()
b = Foo()
print(id(a), id(b))
