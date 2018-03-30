from functools import reduce

# lambda函数
a = lambda x, y: x + y
print(a(1, 6))
a = lambda x: x + 1
print(a(1))

# filter函数 用于过滤,接受参数(函数,迭代对象),即过滤迭代对象中符合函数的值,返回filter对象,可迭代,可配合lambda使用
filter_a = list(filter(lambda x: x > 5, range(100)))  # 打印0-99中大于5的数(当x>5为真)
print(filter_a)

# map函数 用于计算,接受参数(函数,迭代对象(可传入多个)),会将迭代对象对象的值都通过函数计算后返回,返回map对象,可迭代,通常配合lambda使用
map_a = list(map(lambda x, y: x + y, range(100), range(200))) #计算range(100)+range(200)的值
print(map_a)

# reduce函数, 用于依次将序列的值在函数中计算,如下例子依次传入1-99,每次执行x+y,相当于求(((0+1)+2)+..)即0-99的和
# 注:python3中reduce不再作为内置函数使用需要使用from functools import reduce导入
reduce_a = reduce(lambda x, y: x + y, range(100))  #计算0-99的和
print(reduce_a)

# 三个函数可以嵌套使用,比如下列可以计算1-100中所有偶数和
print(reduce(lambda x, y: x + y, list(filter(lambda x: x % 2 == 0, range(100)))))
print('\n'.join(['\t'.join(['%d * %d = %d'%(y,x,x*y) for y in range(1,x+1)])for x in range(1,10)]))