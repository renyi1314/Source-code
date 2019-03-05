class Foo:

    def __init__(self):
        self.name = "renyi"

    def func(self):
        return "ok"


obj = Foo()
res = getattr(obj, 'func')
r = res()
print(r)
setattr(obj, 'func', 20)
res2 = getattr(obj, 'func')
r2 = res()
print("-------")
print(r2)
