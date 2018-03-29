import random

n = 11
list_a = []
for k in range(n):
    list_a.append(random.randint(1, 100))
print(list_a)


# def quick_sort(array, l, r):
#     if l < r:
#         q = partition(array, l, r)
#         quick_sort(array, l, q - 1)
#         quick_sort(array, q + 1, r)
#
#
# def partition(array, l, r):
#     x = array[r]
#     i = l - 1
#     for j in range(l, r):
#         if array[j] <= x:
#             i += 1
#             array[i], array[j] = array[j], array[i]
#     array[i + 1], array[r] = array[r], array[i + 1]
#     return i + 1

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


quick_sort(list_a, 0, 10)
print(list_a)
