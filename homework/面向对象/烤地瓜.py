class SweetPotato:

    def __init__(self):
        self.cookedTime = 0
        self.status = "生的"
        self.season = []

    def cook(self, time):
        self.cookedTime += time
        if self.cookedTime >= 0 and self.cookedTime < 3:
            self.status = "生的"
        elif self.cookedTime > 3 and self.cookedTime <= 6:
            self.status = "半生"
        elif self.cookedTime > 6 and self.cookedTime <= 10:
            self.status = "熟了"
        elif self.cookedTime > 10:
            self.status = "糊了"

    def addSeasoning(self, season_tmp):
        self.season.append(season_tmp)

    def __str__(self):
        msg = "地瓜已经考了{}分钟".format(self.cookedTime)
        if self.season:
            msg += ",当前状态:"
            for items in self.season:
                msg = msg + items
        else:
            pass
        return msg


sweetPotato = SweetPotato()
print(sweetPotato.__class__)
sweetPotato.cook(1)
print(sweetPotato)
sweetPotato.cook(2)
sweetPotato.addSeasoning("盐")
print(sweetPotato)
