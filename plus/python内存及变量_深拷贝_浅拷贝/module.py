# import sys
# print(sys.path)
# # sys.path.append("E:/")
# # print(sys.path)
#
def outer():
    a_var = '闭包里的值'
    x = 1

    def inner():
        x = 1
        x = x + 1
        a_var = '局部空间的值'
        print(a_var, x)

    inner()


outer()

x = 1


def change():
    x = x + 1
    # print(b)


change()
