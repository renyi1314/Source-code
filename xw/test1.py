a = dict()
key = "mains"
value = 99
print(dir(a))
print({key: value})
a.__setattr__(key, value)
setattr(a, key, value)
print(a)
