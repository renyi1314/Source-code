class SayMetaClass(type):

    # 传入三大永恒命题：类名称、父类、属性
    def __new__(cls, name, bases, attrs):
        attrs['say_' + name] = lambda self, value, saying=name: print(saying + ',' + value + '!')
        return type.__new__(cls, name, bases, attrs)


class Foo(object, metaclass=SayMetaClass):
    pass


a = Foo()
print(dir(a))
print(a.__dict__)
