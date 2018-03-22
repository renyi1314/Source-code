list = [888,999,666,777,555,444,333,222,111]
#list = [111,222,333,444,555,666,777,888,999]
def bubble_sort(list):
    length = len(list)
    # 第一级遍历
    for index in range(length):
        # 第二级遍历
        for j in range(1, length - index):
            print (list[j])
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
                #取出最大值放到最后
            #print (list)
        #print (list)
    #print (list)
    return list
bubble_sort(list)