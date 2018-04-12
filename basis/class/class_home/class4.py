class Person:
    def __init__(self, name, age, hobby):
        self.name = name
        self._age = age
        self.__hobby = hobby

    def __str__(self):
        return str(self.__hobby)


a = Person(1, 2, "hobby")
print(a)
print(a._Person__hobby)
a._Person__hobby = "123"
print(a)
print(a._Person__hobby)
