# class Person:
#     name = ["renyi"]
#     age = 24
#
#
# a = Person()
# a.name[0] = "mayun"
# a.age = 50
# # 这时候我们再实例化一个对象b
# b = Person()
# print(b.name, b.age)


class Person:

    def __new__(cls, *args, **kwargs):
        instance = []
        if not hasattr(cls, 'instance'):
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby


persona = Person("renyi", 23, ["睡觉"])
print(persona.__dict__)
print(id(persona))
personb = Person("huanghuan", 25, ["跑步"])
print(personb.__dict__)
print(id(personb))
