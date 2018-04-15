def exc1(name):
    if name == "renyi":
        print(name)
    elif name == "123":
        raise SyntaxError
    else:
        raise NameError("Unknown Error")


# exc1("renyi")
try:
    f = open("123")
    exc1("renyi")
except NameError as e:
    print(e)
    print("名字错了!!!")
except SyntaxError as e:
    print(dir(e))
    print(type(e))
    print(e)
    print("名字不能为123")
else:
    print("名字对了!!!")
finally:
    print("程序运行结束")
