import random
n=10
list =[]
for i in range(n):
    list.append(random.randint(1,100))
print(list)

def selection_sort1(list):
    for i in range(len(list)):
        j = i
        for k in range(i,len(list)):
            if list[i] > list[k]:
                j = k
        if j !=k:
            list[j],list[k]=list[k],list[j]
    print(list)
selection_sort1(list)

