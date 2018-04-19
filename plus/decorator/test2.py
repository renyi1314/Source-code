# def count1():
#     fs = []
#     for i in range(1, 4):
#         def wrapper(a):
#             def f():
#                 return a * a
#             return f
#         fs.append(wrapper(i))
#
#     return fs
#
# f1, f2, f3 = count1()
# print(f1())
# print(f2())
# print(f3())
#
#
#
# def cou



def count1():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count1()

print(f1())
print(f2())
print(f3())