from functools import partial
from functools import wraps
@wraps()
def add(a,b):
    return a+b

print(partial(add,2))