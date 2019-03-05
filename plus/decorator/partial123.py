import random
from functools import wraps

listOri = []
for i in range(100000):
    listOri.append(random.randint(1, 10000000))

print(listOri)


def bubbleSort(val):
    for i in range(len(val)):
        for j in range(i, len(val)):
            if val[i] > val[j]:
                val[i], val[j] = val[j], val[i]

    print(val)
    return val


# print(bubbleSort(listOri))


def decoratorSingleObject(cls):
    dictObj = {}

    @wraps(cls)
    def decorator(*args, **kwargs):
        if dictObj.get("cls") is None:
            dictObj["cls"] = cls(*args, **kwargs)
        return dictObj["cls"]

    return decorator


@decoratorSingleObject
class SingleObject:
    pass


a = SingleObject()
b = SingleObject()
print(id(a), id(b))


def quickSort(array, l, r):
    if l > r:
        return
    low = l
    high = r
    key = array[l]
    while l < r and array[r] > key:
        r -= 1
    array[r] = array[l]
    while l < r and array[l] <= key:
        l += l
    array[l] = array[r]
    quickSort(array, low, l)
    quickSort(array, l + 1, high)


listOri = []
for i in range(1000):
    listOri.append(random.randint(1, 10000000))


def quickSort2(a, l, r):
    while l > r:
        return
    low = l
    high = r
    key = a[l]
    while l < r and a[r] > key:
        r -= 1
    a[r] = a[l]
    while l < r and a[l] <= key:
        l += 1
    a[l] = ~a[r]
    quickSort2(a, low, l)
    quickSort2(a, l + 1, high)


print(listOri)
quickSort(listOri, 0, 999)
print(listOri)
