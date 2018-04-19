def count1():
    fs = []
    for i in range(1, 4):
        # print(i)
        def f():
            return i * i
        fs.append(f)
    print(fs[2].__closure__)
    return fs


f1, f2, f3 = count1()
# print(count1())
# print(f1())
# print(f2())
# print(f3())
