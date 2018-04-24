from functools import wraps
from functools import partial


def add(a, b):
    return a + b


def test(a):
    return partial(add, 1, a)

def test2():
    print("test2")
    def test3():
        print("test3")
    return test3

print(test2())
print(test(2)())

# attrs = ('__module__', '__name__', '__qualname__', '__doc__',
#                        '__annotations__')
#
# class Foo:
#     pass
# print(dir(Foo))
# print(Foo.__name__)
# print("*"*100)
# for attr in attrs:
#     try:
#         value = getattr(Foo,attr)
#         print(value)
#     except AttributeError as e:
#         print(e)