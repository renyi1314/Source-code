num = 10
a = 0
b = num
count = 0
while True:
    tmp = (a + b) / 2
    if tmp ** 2 > num:
        b = tmp
    elif tmp ** 2 < num:
        a = tmp
    if (tmp ** 2 - num) ** 2 < 0.0000000001:
        break
    count += 1
    print(tmp)
    print(count)
