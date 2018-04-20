def generate_fun(k, b):
    def fun(x):
        return k * x + b

    return fun


a = generate_fun(1, 1)
print(a(2))
