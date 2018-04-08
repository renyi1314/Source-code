class Data_test(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def get_date(cls, string_date):
        year, month, day = map(int, string_date.split('-'))
        return cls(year, month, day)

    def print_date(self):
        print("The year is :%s" % self.year)
        print("The month is :%s" % self.month)
        print("The day is :%s" % self.day)


date1 = Data_test(2018, 3, 2)
date1.print_date()
date2 = Data_test.get_date("2018-3-2")
date2.print_date()
