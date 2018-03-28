class str():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self):
        return self.a + self.b

    def __sub__(self):
        return self.a - self.b


a = "123"
b = "321"
# print(a-b)
