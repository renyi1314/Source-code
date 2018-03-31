# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%s*%s=%s" % (i, j, i * j), end=" ")
#     print("\n")
# print(list("%d*%d=%d"%(i,j,i*j) for i in range(1,10)for j in range(1,i+1)))
# for x in range(1,10) for j in range(x) : print(x ** 2,end=' ')
a, b, c = "abc", "123", "xyz"
# print(list(zip(a,b,c)))
for x, y, z in zip(a, b, c):
    print(x, y, z)
