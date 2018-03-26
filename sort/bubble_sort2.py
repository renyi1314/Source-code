import random
n=10
list =[]
for i in range(n):
    list.append(random.randint(1,100))

print(list)
def bubble_sort(list):
    length = len(list)
    # 第一级遍历
    for index in range(length):
        # 第二级遍历
        for j in range(1, length - index):
            print (list[j])
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
    return list
# bubble_sort(list)