# def generate_fun(k, b):
#     def fun(x):
#         return k * x + b
#
#     return fun
#
#
# a = generate_fun(1, 1)
# print(a(2))

fs = []
for i in range(1, 4):
    def f(i):
        return i * i


    fs.append(f)

print(fs)

f1, f2, f3 = fs
print(f1(1))
print(f2(2))
print(f3(3))
