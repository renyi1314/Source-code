class f1:
    __name = "renyi"


class f2(f1):
    pass

a=f1()
b=f2()
print(f1._f1__name)
print(b._f2__name)