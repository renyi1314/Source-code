def closure_func(args1):
    def greeting(arg2):
        print(args1, arg2)

    return greeting


f1 = closure_func("参数1")
f1("参数2")
print(dir(f1))
print(f1.__closure__)
print(type(f1.__closure__[0]))
print(f1.__closure__[0].cell_contents)
