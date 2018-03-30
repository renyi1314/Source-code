def pr_3(i):
    print(i)
    i = i + 1
    if i <= 3:
        pr_3(i)
    print(i - 1)


pr_3(1)
