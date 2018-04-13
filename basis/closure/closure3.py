def fn1(one):
    def fn2(two):
        print(one, two)

    return fn2


fna = fn1("moring")
print("Function name is ", fna.__name__)
print("id of function is: ", id(fna))
print("*" * 100)
fnb = fn1("moring")
print("Function name is ", fnb.__name__)
print("id of function is: ", id(fnb))
