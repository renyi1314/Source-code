def test1():
    print("------")
    return 1, 2, 3


def test2():
    a, b, c = test1()
    print(c, b, a)


test2()
