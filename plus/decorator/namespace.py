s = "string in global"
num = 99


def numFunc(a, b):
    num = 100
    print("print s in numFunc: ", s)

    def addFunc(a, b):
        s = "string in addFunc"
        print("print s in addFunc: ", s)
        print("print num in addFunc: ", num)
        print("locals of addFunc: ", locals())
        return "%d + %d = %d" % (a, b, a + b)

    print("locals of numFunc: ", locals())
    return addFunc(a, b)


numFunc(3, 6)
print("globals: ", globals())
