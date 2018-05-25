# def decora_foo(fn,*args,**kwargs):
#     print("decora_fn start")
#     print(*args,**kwargs)
#     fn(*args,**kwargs)
#     print("decora_fn end")
#
# @decora_foo
# def foo(a,b):
#     print("foo")

# class DecoraFoo:
#     def __init__(self,fn):
#         self.__fn = fn
#
#     def __call__(self, *args, **kwargs):
#         print("decora fn start")
#         self.__fn(*args,**kwargs)
#         print("decora fn end")
#
# @DecoraFoo
# def foo(a,b):
#     print("foo")
#
# foo(1,2)


# def decora_Foo(cls,*args,**kwargs):
#     instance = {}
#     def warps(*args,**kwargs):
#         if cls not in instance:
#             instance[cls] = cls(*args,**kwargs)
#         return instance[cls]
#     return warps
# @decora_Foo
# class Foo:
#     pass
#
#
# a = Foo()
# b = Foo()
#
# print(id(a), id(b), a is b)


class Foo:
    def __new__(cls, *args, **kwargs):
        return super().__new__(*args, **kwargs)


a = Foo()
b = Foo()

print(id(a), id(b), a is b)
