# import time
#
#
# def count_factory(old_fn):
#     def new_fn(*args, **kwargs):
#         ret = old_fn(*args, **kwargs)
#         print("时间为:", time.time())
#         return ret
#
#     return new_fn
#
#
# @count_factory
# def fn(arg):
#     def f(x):
#         return x * x
#
#     rs = map(f, arg)
#     print(list(rs))


#
# a = [i for i in range(1, 101)]
# print(fn(a))
# print("+" * 100)
# a = [i for i in range(1, 10000)]
# print(fn(a))
map_a = list(map(lambda x, y: x + y, range(200), range(200)))
print(map_a)