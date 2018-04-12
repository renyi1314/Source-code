class student():

    def __init__(self, name, age, sex, hometown):
        self.name = name
        self.age = age
        self.sex = sex
        self.hometown = hometown

    def showself(self):
        print("hello")
        print(self.__dict__)
        # return

    def __add__(self, other):
        if isinstance(other, student):
            return self.age + other.age
        # else:
        #     raise TypeError("The instance must be same object")
            # continue

    # def __str__(self):
    #     return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


class animal():

    def __init__(self, age):
        self.age = age


student1 = student("renyi", 24, "man", "nanchong")
student2 = student("huanghuan", 23, "women", "duofu")
print(student1.__getattribute__("age"))
# dog = animal(40)
# print(student1 + dog)
# print(dir(dog))
# student1.showself()
# print(student1)
