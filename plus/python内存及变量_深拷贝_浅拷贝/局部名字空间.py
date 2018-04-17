def fn1():
    local_var1 = 100
    print(locals())
    print(locals)


def fn2():
    local_var2 = 100
    print(locals())


# fn1()
# fn2()
print(globals())

# for key, value in globals().items():
#     try:
#         print(key, value)
#     except Exception as e:
#         print(e)

for key in list(globals().keys()):
    try:
        print(key)
    except Exception as e:
        print(e)

for value in list(globals().values()):
    try:
        print(value)
    except Exception as e:
        print(e)
# a = globals()
# print(a)
