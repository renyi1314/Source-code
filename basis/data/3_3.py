dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}

# a. 请循环输出所有的key
dic_a = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
print(list(dic_a.keys()))

# b. 请循环输出所有的value
dic_b = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
print(list(dic_a.values()))
# c. 请循环输出所有的key 和value
dic_c = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
print(list(dic_c.items()))

# d. 请在字典中添加⼀个键值对， "k4": "v4"， 输出添加后的字典
dic_d = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
dic_d["k4"] = "v4"
print(dic_d)

# e. 请在修改字典中 “k1” 对应的值为 “posekakaka”， 输出修改后的字典
dic_e = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
dic_e["k1"] = "posekakaka"
print(dic_e)