def func(x):
    while x < 888:
        print(x)
        return func(x + 1)


func(5)
