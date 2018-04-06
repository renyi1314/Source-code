# def foo(n):
#     for i in range(1, n+1):
#         for j in range(1, i + 1):
#             print("%s*%s=%s" % (i, j, i * j), end="\t")
#         print("\n")
# print(list("%d*%d=%d"%(i,j,i*j) for i in range(1,10)for j in range(1,i+1)))
# for x in range(1,10) for j in range(x) : print(x ** 2,end=' ')
# a, b, c = "abc", "123", "xyz"
# # print(list(zip(a,b,c)))
# for x, y, z in zip(a, b, c):
#     print(x, y, z)

# foo(11)


def add(x, y):
    return x + y


print(add(5, 10))
