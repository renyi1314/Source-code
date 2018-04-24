class CurrencyCalculator:

    def __init__(self):
        self.usToRmb = 6.2945
        self.hkToRmb = 0.8024
        self.thToRmb = 0.2009
        self.myRmb = 0

    @property
    def rmb(self):
        return self.myRmb

    @rmb.setter
    def rmb(self, num):
        self.myRmb = num

    @property
    def usDollar(self):
        return self.myRmb / self.usToRmb

    @usDollar.setter
    def usDollar(self, num):
        self.myRmb = self.myRmb + num * self.usToRmb

    @property
    def hkDollar(self):
        return self.myRmb / self.hkToRmb

    @hkDollar.setter
    def hkDollar(self, num):
        self.myRmb = self.myRmb + num * self.hkToRmb

    @property
    def thaiBaht(self):
        return self.myRmb / self.thToRmb

    @thaiBaht.setter
    def thaiBaht(self, num):
        self.myRmb = self.myRmb + num * self.thToRmb


a = CurrencyCalculator()
a.rmb = 20
print(a.rmb)
print(a.usDollar)
# a.usDollar = 9
# print(a.usDollar)
# print(a.hkDollar)
# a.hkDollar = 9
# print(a.hkDollar)
