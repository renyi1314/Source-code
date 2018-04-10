def fn(*args, **kwargs):
    print(args)
    print(kwargs)


a = (1, 2, 3,)
b = {"name": "renyi", "age": 27}
fn(a, **b)
