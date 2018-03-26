import random

list =[]
for i in range(10):
    list.append(random.randint(1,100))

def bubble_sort(list):
    for i in range(len(list)):
        for j in range (i,len(list)):
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]
        print (list)
                #取出最小值放到第一个
            #print (list)
    print (list)

bubble_sort(list)