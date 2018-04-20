s = "string in global"
num = 99


def numfunc(a, b):
    num = 100
    print("print s in numFunc: 11111111", s)

    def addfunc(a, b):
        s = "string in addFunc"
        print("print s in addFunc: 3333333333", s)
        print("print num in addFunc: 444444444", num)
        print("locals of addFunc: 55555555", locals())
        print("66666666666666")
        return "%d + %d = %d" % (a, b, a + b)

    print("locals of numFunc: 2222222222", locals())
    print("777777777")
    return addfunc(a, b)


numfunc(3, 6)
print("globals: ", globals())
