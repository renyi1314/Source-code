class foo:

    def __init__(self, old_price, discount):
        self.old_price = old_price
        self.discount = discount

    @property
    def price(self):
        self.new_price = self.old_price*self.discount
        return self.new_price

    @price.setter
    def price(self, value):
        self.old_price = value

    @price.deleter
    def price(self):
        del self.old_price


f = foo(100, 0.8)
print(f.price)
f.price = 200
print(f.price)
