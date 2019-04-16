from functools import wraps, partial


def update_wrapperr(wrapper,wrapped):
    for attr in dir(wrapped):
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            # try:
            setattr(wrapper, attr, value)
            # except TypeError as e:
            #     print(e)
        finally:
            setattr(wrapper, "__qualname__", "renyi")
    for attr in ('__dict__',):
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
    # Issue #17482: set __wrapped__ last so we don't inadvertently copy it
    # from the wrapped function when updating __dict__
    wrapper.__wrapped__ = wrapped
    # Return the wrapper so this can be used as a decorator via partial()
    return wrapper


def decora(wrapped):
    return partial(update_wrapperr, wrapped=wrapped)


def fn():
    pass


def decorator_single_obj(cls, *args, **kwargs):
    instance = {}  # 创建字典来保存实例
    @decora(cls)
    def get_instance(*args, **kwargs):
        if cls not in instance:  # 若实例不存在则新建
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instance


@decorator_single_obj
class Foo:
    age = 24

    def __init__(self, name):
        self.name = name

    @classmethod
    def test(cls):
        pass


obj1 = Foo("123")
print(Foo)
print(dir(Foo))
# print(Foo.upper())
# print(dir(Foo))
# print(id(obj1))
# obj2 = Foo("321")
# print(id(obj2))
# obj1 = Foo("123")
# print(Foo)
# Foo.age
# Foo.test
# print(dir(Foo))
# print(Foo.__wrapped__)

# ('__module__', '__name__', '__qualname__', '__doc__',
#                        '__annotations__')
# print(dir(Foo))
# print(obj1.age)
# print(Foo.age)
# print(Foo)
# obj2 = Foo("321")
# print(Foo.test)
# print(Foo.age)
