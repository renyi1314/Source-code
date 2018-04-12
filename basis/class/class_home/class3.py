def decorator_single_object(cls, *args, **kwargs):
    instance = {}
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance

@decorator_single_object
class Person:
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
