def decorator_single_obj(cls, *args, **kwargs):
    instance = {}  # 创建字典来保存实例

    def get_instance(*args, **kwargs):
        if cls not in instance:  # 若实例不存在则新建
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instance


@decorator_single_obj
class Foo(object):
    def __init__(self, name):
        self.name = name


obj1 = Foo("123")
print(obj1.name, id(obj1))
obj2 = Foo("321")
print(obj2.name, id(obj2))