class Foo:
    def __init__(self, name):
        self.name = name
        self.age = 20

    age = 18


f = Foo("nick")
print(Foo.age)
print(f.name)
print(f.age)
