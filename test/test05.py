import json, requests, copy
copy.deepcopy()

def DebugLog(*args):
    Log(*args)
    pass


# 判断币余额是否大于0
def isZero(coinName, amount):
    if ext.coinsPriceLevel[coinName] * amount < 5:
        return True
    else:
        return False


# 获取原始精度api数据
def getPrecisionOriginal():
    url = "https://api.huobi.pro/v1/common/symbols"
    response = requests.get(url=url)
    data = json.loads(response.text)
    return data


# 根据交易对查询精度
def getPrecision(data, symbol):
    for item in data["data"]:
        if item["symbol"] == symbol.lower().replace("_", ""):
            return item["amount-precision"]


class ExchangeInfo:
    def __init__(self, tempExchange):
        self.ex = tempExchange
        self.currency = tempExchange.GetCurrency()
        self.coinName = self.currency.split("_")[0]
        self.bananceName = self.currency.split("_")[1]
        # 精度
        self.precision = getPrecision(precisionOriginalData, self.currency.lower())
        # Log(self.precision)

    def reinit(self):
        self.currentCoinAmount = None
        self.currentBananceAmount = None
        self.klines = None

    def setCount(self, tempInfo):
        # Log("----tempInfo:-------")
        # Log(json.dumps(tempInfo))
        # Log(self.currency)
        for data in tempInfo["data"]["list"]:
            if data["currency"] == self.coinName.lower() and data["type"] == "trade":
                self.currentCoinAmount = float(data["balance"])
            if data["currency"] == self.bananceName.lower() and data["type"] == "trade":
                self.currentBananceAmount = float(data["balance"])
        # Log(self.coinName.lower(),self.currentCoinAmount)
        # Log(self.bananceName.lower(),self.currentBananceAmount)
        # Log("----tempInfo load结束-------")

    def loadKLineIfNeed(self):
        if not isZero(self.coinName, self.currentCoinAmount) or not isZero(self.bananceName, self.currentBananceAmount):
            self.klines = self.ex.GetRecords()

    def exchangeIfNeed(self, haveBoughtInThisCircle):
        if self.klines is None:
            Log("账户金额为0,未触发交易")
            return

        tempKlines = self.klines[:]
        ma = TA.MA(tempKlines, MABubleCircle)
        currentMa = ma[-1]
        currentPrice = tempKlines[-1].Close
        tempKlines.pop(-1)
        upMax = TA.Highest(tempKlines, upBubleCircle, 'High')
        lowMin = TA.Lowest(tempKlines, lowBubleCircle, 'Low')
        haveBoughtInThisSymbol = False
        haveSoldInThisSymbol = False
        Log("判断交易开始,当前交易所为:{},交易对为:{}".format(self.ex.GetName(), self.currency))
        Log("当前价格是 {} ,在 {} 根k线内最高价为 {} ,在 {} 根k线内最低价为 {} ，当前 MA{} 为 {}".format(
            currentPrice, upBubleCircle, upMax, lowBubleCircle, lowMin, MABubleCircle, currentMa))
        if not isZero(self.coinName, self.currentCoinAmount):
            Log("当前{}资产不为0".format(self.coinName))
            if currentPrice < (lowMin * (1 - bublePercent * 0.01)) or currentPrice < currentMa:
                # 卖出币
                Log("-------卖出-------")
                self.ex.Sell(-1, _N(self.currentCoinAmount, self.precision))
                haveSoldInThisSymbol = True
                Log("市价卖出{}个{}".format(self.currentCoinAmount, self.coinName))
            else:
                Log("不符合卖出条件")
        else:
            Log("当前{}资产为0".format(self.coinName))

        if not isZero(self.bananceName, self.currentBananceAmount) and not haveBoughtInThisCircle:
            Log("当前{}资产不为0".format(self.bananceName))
            if currentPrice > (upMax * (1 + bublePercent * 0.01)):
                self.ex.Buy(-1, _N(self.currentBananceAmount, self.precision))
                haveBoughtInThisSymbol = True
                Log("用{}个{}市价买入".format(self.currentBananceAmount, self.bananceName))
            else:
                Log("不符合买入条件")
        else:
            Log("当前{}资产为0".format(self.bananceName))
        if not (haveBoughtInThisSymbol or haveSoldInThisSymbol):
            Log("本轮未触发任何交易行为")
        Log("本轮交易结束")
        return haveBoughtInThisSymbol

    def clearOrders(self):
        # 清除订单
        # orders = self.ex.GetOrders()
        # for tempOrder in orders:
        #     self.ex.CancelOrder(tempOrder.Id)
        # 清除订单第二版，改为异步执行
        ordersAsyn = self.ex.Go("GetOrders")
        orders, status = ordersAsyn.wait(3)
        if not orders:
            return
        else:
            for order in orders:
                cancelOrderAsyn = self.ex.CancelOrder(order.id)
                cancelOrder, status = cancelOrderAsyn.wait(3)
                Log("取消订单：{}".format(order.id))


def onTicker():
    tmpExchangeInfos = copy.deepcopy(ext.exchangeInfos)
    # 给定是否交易的flag，锁定当前交易
    haveBoughtInThisCircle = False
    # 清除之前未完成订单
    for tempExchangeInfo in tmpExchangeInfos:
        tempExchangeInfo.clearOrders()
    # 重新初始化exchange内的信息
    # for tempExchangeInfo in tmpExchangeInfos:
    #     tempExchangeInfo.reinit()
    # 当前账户
    current_account = exchange.GetAccount()
    # 获取交易对对应的资产数量
    for tempExchangeInfo in tmpExchangeInfos:
        tempExchangeInfo.setCount(current_account.Info)
    # 如果交易对有对应资产，则需要获取对应kline
    for tempExchangeInfo in tmpExchangeInfos:
        tempExchangeInfo.loadKLineIfNeed()
    # 判断是否需要交易并进行交易
    for tempExchangeInfo in tmpExchangeInfos:
        Log("+++++++++++++{}++++++++++++++++++".format(tempExchangeInfo.ex.GetCurrency()))
        haveBoughtInThisCircle = tempExchangeInfo.exchangeIfNeed(haveBoughtInThisCircle) or haveBoughtInThisCircle


def main():
    # 获取交易所精度api数据
    global precisionOriginalData
    precisionOriginalData = getPrecisionOriginal()

    # 初始化每个交易对的信息
    ext.exchangeInfos = []
    for tempExchange in exchanges:
        ext.exchangeInfos.append(ExchangeInfo(tempExchange))
        ext.coinsPriceLevel = json.loads(coinsPriceLevelString)

    while True:
        # onTicker()
        try:
            Log("-----------------------------------------------")
            onTicker()
            # pass
        except Exception as e:
            Log(e)
        finally:
            Sleep(1000 * 3)
