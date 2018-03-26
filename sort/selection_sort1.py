import random
n=10
list =[]
for i in range(n):
    list.append(random.randint(1,100))
# print(list)

def selection_sort(list):
    for i in range(len(list)):
        k = len(list)
        for j in range(k):
            if list[i] > list[j]:
                return list[j]
            k-=1
        list[i]=list[j]
    print(list)

selection_sort(list)