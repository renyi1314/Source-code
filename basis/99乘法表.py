def cf_9(i):
    j = 1
    while j <= i:
        print("%s * %s = %s"%(j, i, i*j), end=" ")
        j += 1
    print("\n")
    i += 1
    if i <= 9:
        cf_9(i)
cf_9(1)