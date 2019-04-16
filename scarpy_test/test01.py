if not isZero(self.coinName, self.currentCoinAmount):
    if currentPrice < (lowMin * (1 - bublePercent * 0.01)) or currentPrice < currentMa:
        # 卖出币
        self.ex.Sell(-1, self.currentCoinAmount)
        haveExchanged = True
        Log("已触发卖出交易行为：卖出{}个{},买入{}".format(self.currentCoinAmount, self.coinName, self.bananceName)
        if not isZero(self.bananceName, self.currentBananceAmount):
            if
        currentPrice > (upMax * (1 + bublePercent * 0.01)):
        self.ex.Buy(-1, self.currentBananceAmount)
        haveExchanged = True
        Log("已触发买入交易行为：买入{},卖出{}个{}".format(self.coinName, self.currentBananceAmount, self.bananceName)