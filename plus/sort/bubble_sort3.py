import random

n = 20
list=[]

for i in range(n):
    list.append(random.randint(1,100))
print(list)


def bubble_sort3(list):
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
                # print(list)
    print(list)


bubble_sort3(list)
