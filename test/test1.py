from functools import wraps


def single(cls):
    instance = {}

    @wraps(cls)
    def decorator(*args, **kwargs):
        if instance.get('cls') is None:
            instance['cls'] = cls(*args, **kwargs)
        return instance['cls']

    return decorator


@single
class Person:
    pass


@single
class Person2:
    pass


a = Person()
b = Person2()

print(id(a))
print(id(b))

# class Person:
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Person, cls).__new__(cls)
#         return cls.instance
#
#
# a = Person()
# b = Person()
# print(id(a), id(b))
