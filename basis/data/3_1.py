name = "posekakaka"

print(name)
# a.移除两边的空格
print(name.strip())
# b.判断变量是否以po开头
print("po" == name[0:2])
# c.判断变量是否以a结尾
print("a" == name[-1])
# d.将变量中"k"替换为"c"
print(name.replace("k", "c"))
# e.将变量根据"k"分割
print(name.split("k"))
# f.将变量分割后得到列表
print(type(name.split("k")))
