def fib():
    a = 1
    b = 1
    while b < 1000:
        c = a
        a = b
        b = c + b
        print(a)


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(10000))
