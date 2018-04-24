class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @age.deleter
    def age(self):
        del self.__age

    # aa = property(get_age, set_age, del_age)


stu1 = Person("renyi")
# stu1.test = 99
# print(stu1.test)

# stu1.aa = 2873
# print(stu1.aa)
stu1.age = 213
print(stu1.age)
print(stu1._Person__age)
