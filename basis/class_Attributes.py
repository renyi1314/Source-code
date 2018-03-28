class Foo:

    def __init__(self, old_price, discount):
        self.old_price = old_price
        self.discount = discount

    def _get_price(self):
        self.new_price = self.old_price * self.discount
        return self.new_price

    def _set_price(self, value):
        self.old_price = value

    def _del_price(self):
        del self.old_price

    price = property(_get_price, _set_price, _del_price)


f = Foo(100, 0.8)
print(f.price)
f.price = 200
print(f.price)
