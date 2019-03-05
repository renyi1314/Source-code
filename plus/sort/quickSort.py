# def partition(array, l, r):
#     x = array[r]
#     i = l - 1
#     for j in range(l, r):
#         if array[i] <= x:
#             i += 1
#             array[i], array[j] = array[j], array[i]
#     array[i + 1], array[r] = array[r], array[i + 1]
#     return i + 1
#
#
# def quick_sort(array, l, r):
#     if l < r:
#         partition(array, l, r)
#         quick_sort(array, l, q - 1)
#         quick_sort(array, q + 1, r)


def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


import random

n = 100
list_a = []
for k in range(n):
    list_a.append(random.randint(1, 100000))


def quick_sort2(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
        print(list_a)
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


def quickSort3(array, left, right):
    if left > right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
        print(array)
    array[right] = key
    quickSort3(array, low, left - 1)
    quickSort3(array, left + 1, high)


def quickSort4(a, l, r):
    if l > r:
        return
    low = l
    high = r
    key = a[l]

    while l < r:
        while l < r and a[r] > key:
            r -= 1
            a[l] = a[r]
        while l < r and a[l] <= key:
            l += 1
            a[r] = a[l]
    a[r] = key
    quickSort4(a, low, l - 1)
    quickSort4(a, l + 1, high)


def quickSort5(a, l, r):
    while l > r:
        return
    low = l
    high = r
    key = a[l]
    while

print(list_a)
quickSort4(list_a, 0, 99)
print(list_a)
