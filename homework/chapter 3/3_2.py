li = ['ethan', 'zoran', 'jim']

# a. 计算列表⻓度并输出
print(len(li))

# b. 列表中追加元素 “lucy”， 并输出添加后的列表
list_append = ['ethan', 'zoran', 'jim']
list_append.append("lucy")
print(list_append)

# c. 请在列表的第 1 个位置插⼊元素 “Tony”， 并输出添加后的列表
list_insert = ['ethan', 'zoran', 'jim']
list_insert.insert(0, "Tony")
print(list_insert)

# d. 请修改列表第 2 个位置的元素为 “Kelly”， 并输出修改后的列表
list_update = ['ethan', 'zoran', 'jim']
list_update[1] = "Kelly"
print(list_update)

# e. 请删除列表中的元素 “ethan”， 并输出修改后的列表
list_delete = ['ethan', 'zoran', 'jim']
list_delete.remove('ethan')
print(list_delete)

# f. 请删除列表中的第 2 个元素， 并输出删除的元素的值和删除元素后的列表
list_delete = ['ethan', 'zoran', 'jim']
del (list_delete[1])
print(list_delete)
