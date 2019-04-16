klineDatas = [{"Volume": 148.5277, "High": 0.00170793, "Low": 0.00170603, "Time": 1538283120000, "Close": 0.00170793,
               "Open": 0.00170606},
              {"Volume": 504.047, "High": 0.00170768, "Low": 0.00170511, "Time": 1538283180000, "Close": 0.00170768,
               "Open": 0.00170511},
              {"Volume": 266.59341, "High": 0.00170864, "Low": 0.00170756, "Time": 1538283240000, "Close": 0.00170756,
               "Open": 0.00170864},
              {"Volume": 1342.20852, "High": 0.00170754, "Low": 0.00170715, "Time": 1538283300000, "Close": 0.00170754,
               "Open": 0.00170715},
              {"Volume": 1973.5338, "High": 0.00170525, "Low": 0.00170525, "Time": 1538283360000, "Close": 0.00170525,
               "Open": 0.00170525}]


def exchangeIfNeed(self):
    # 高点数据列表
    klineHighListOfHigh = []
    # 低点数据列表
    klineHighListOfLow = []
    # 最近数据
    currentKlineData = klineDatas.pop(-1)
    # 最近数据高点
    currentKlineDataOfHigh = klineDatas.pop(-1)['High']
    # 最近数据低点
    currentKlineDataOfLow = klineDatas.pop(-1)['Low']
    for klineData in klineDatas:
        klineHighListOfHigh.append(klineData['High'])
        klineHighListOfLow.append(klineData['Low'])
    if currentKlineDataOfHigh > max(klineHighListOfHigh):
        return True
    elif currentKlineDataOfLow < min(klineHighListOfLow):
        return True
