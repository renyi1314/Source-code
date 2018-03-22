####第一个和第二个比，大的放后面，最后一个不用比
import random
list = [999,888,777,666,555,444,333,222,111]
#array = [111,222,333,444,555,666,777,888,999]

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