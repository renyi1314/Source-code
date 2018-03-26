import random

n=10
list =[]
for i in range(n):
    list.append(random.randint(1,100))

def bubble_sort(list):
    for i in range(len(list)):
        for j in range (i,len(list)):#先找第,2,3个数值,依次往后匹配
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]
                #取出最小值放到第一个
            #print (list)
    print(list)

bubble_sort(list)