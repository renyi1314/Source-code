class Foo():

    def __init__(self, name):
        if not hasattr(self, 'initFlag'):
            self.initFlag = True
            self.name = name

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):  # 当对象不存在instance属性,即类还没有被实例化时,返回实例化对象
            cls.instance = super(Foo, cls).__new__(cls)  # 创建当前类的对象,相当于object.__new__(cls)
        return cls.instance


obj1 = Foo("123")
print(obj1.name)
print(dir(obj1))
print("-------------")
print(id(obj1.instance))
print(id(obj1))
print("-------------")
print(dir(Foo))
obj2 = Foo("321")
print(obj1 == obj2)
print(obj1.name, obj2.name)
print(id(obj1), id(obj2))
print("------------------")
print(id(Foo.instance));
print(dir(Foo))