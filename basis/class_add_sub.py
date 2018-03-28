class Programer(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __eq__(self, other):
    #     if isinstance(other, Programer):
    #         if self.age == other.age:
    #             return True
    #         else:
    #             return False
    #     else:
    #         raise Exception("The type must be same father class")
    #
    # def __add__(self, other):
    #     if isinstance(other, Programer):
    #         return self.age + other.age
    #     else:
    #         raise Exception("The type must be same father class")
    #
    # def __sub__(self, other):
    #     if isinstance(other, Programer):
    #         return self.age - other.age
    #     else:
    #         raise Exception("The type must be same father class")


if __name__ == "__main__":
    a = Programer("renyi", 25)
    b = Programer("huanghuan", 25)
    print(a.age + b.age)
    # print(a == b)
    # print(a - b)
