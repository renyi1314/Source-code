class Person:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('Expected a < 0 number')
        self.__age = value

    @age.deleter
    def age(self):
        raise AttributeError("Can't delete attribute")

p = Person()
p.age = 10
print(p._Person__age)

