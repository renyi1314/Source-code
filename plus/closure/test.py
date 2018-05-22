def count1():
    fs = []
    global i
    for i in range(1, 4):

        def f():
            return i * i
        # print("---------*-------")
        # print(f())
        fs.append(f)
    print("----------------")
    f1, f2, f3 = fs

    print(f1())
    print(f2())
    print(f3())
    print("----------------")
    return fs


f1, f2, f3 = count1()

print(f1())
print(f2())
print(f3())
