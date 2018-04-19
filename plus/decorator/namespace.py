# def de_fun(old_fun):
#     print("*************")
#     print("function is:::",old_fun)
#     print("*************")
#     def warps(*args,**kwargs):
#         print("jiayou")
#         old_fun(*args,**kwargs)
#         return old_fun
#     return warps
#
# # @de_fun
# def fun(a,b):
#     print(a,b)
# # print(fun)
#
# de_fun(fun("123", "321"))
# fun("123","321")

def de_fun(old_fun):
    print("hehe")
    # print(old_fun)
    return old_fun
    # print(*args, **kwargs)
    # print("gg")
    # old_fun(*args,**kwargs)


@de_fun
def fun(a, b):
    print(a, b)
    pass
#
fun("123", "321")
print(fun)
# # de_fun(fun("123","321"))
#
# def fn1(*args):
#     print(args)
#
# def fn2(a):
#     pass
#
# fn1(fn2(123))
#
#
# print()
