# 生成器
def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


res = fib()
print(next(res))


# 指定位置的值
def fib2(n):
    a, b, i = 0, 1, 1
    while i < n:
        a, b = b, a + b
        i += 1
    return b


