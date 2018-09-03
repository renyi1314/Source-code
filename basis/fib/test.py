def fib(x):
    n, a, b = 0, 0, 1
    while n < x:
        a, b = b, a + b
        n += 1
    print(b)

fib(1)