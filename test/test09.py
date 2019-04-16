import json
import traceback
import random
import pandas as pd
import math
import time
from datetime import datetime, timedelta, timezone


def getRandomValue():
    return random.uniform(-1, 1)


def clearTimeOutOrders(orders):
    for order in orders:
        createdTime = exchangeTimeToLocal(order.Info["info"]["createdAt"])
        if (getNowDateTime() - createdTime).seconds > orderTimeOut:
            exchange.CancelOrder(order.Id)
            printfTableAddData("本轮开始时间", getNowDateTime().strftime("%Y-%m-%d %H:%M:%S"))
            printfTableAddData("存量订单数量", len(orders))
            printfTableAddData("交易类型", "超时撤单")
            printfTableAddData("价格", order.Price)
            printfTableAddData("数量", order.Amount)
            printfTableAddData("备注", "ID:" + str(order.Id))
            printfTableAddData("操作", "")
            printfTable()


def onTicker():
    # Log(cls.nextSendOrderTime,time.time())
    if ext.nextSendOrderTime < time.time():
        # Log("轮询存单，准备挂单")
        refreshSendOrderTime()
        while True:
            orders = exchange.GetOrders()
            clearTimeOutOrders(orders)
            printfTableAddData("本轮开始时间", getNowDateTime().strftime("%Y-%m-%d %H:%M:%S"))
            if len(orders) >= maxOrdersCount:
                break

            ticker = exchange.GetTicker()
            if (ticker.Sell - ticker.Buy) < minDepth:
                Log("市场深度不足以开仓", "#FF0000")
                break
            printfTableAddData("存量订单数量", len(orders))
            price = _N((ticker.Buy / 2 + ticker.Sell / 2) + priceFloat * getRandomValue(), minPeiceDiffrent)
            count = _N(oneceCount + oneceCountFloat * getRandomValue(), minCountDiffrent)
            printfTableAddData("交易类型", "挂单")
            printfTableAddData("价格", price)
            printfTableAddData("数量", count)
            if count >= minExchangeCount:
                printfTableAddData("备注", "")
                func = getRandomSendOrderFunc(exchange)
                printfTableAddData("操作", func[1])
                func[0](price, count)
            else:
                printfTableAddData("备注", "低于最低成交限制,未成交")
            printfTable()
    else:
        # Log(_N(cls.nextSendOrderTime - time.time(),2),"秒后查看存单情况以挂单")
        pass

    if ext.nextEatOrderTime < time.time():
        # Log("轮询存单，准备吃单")
        refreshEatOrderTime()
        orders = exchange.GetOrders()
        clearTimeOutOrders(orders)
        printfTableAddData("本轮开始时间", getNowDateTime().strftime("%Y-%m-%d %H:%M:%S"))
        # 找到自己的买单里面的最高价和卖单里面的最低价单子
        highPriceBuyOrder = None
        lowPriceSellOrder = None
        # Log("吃单判断前order情况",json.dumps(orders))
        printfTableAddData("存量订单数量", len(orders))
        for tempOrder in orders:
            if tempOrder.Type == ORDER_TYPE_BUY:
                if highPriceBuyOrder is None or highPriceBuyOrder.Price < tempOrder.Price:
                    highPriceBuyOrder = tempOrder
            else:
                if lowPriceSellOrder is None or lowPriceSellOrder.Price > tempOrder.Price:
                    lowPriceSellOrder = tempOrder

                    # 随机吃掉找出的卖单或者买单
        rivalOrder = getNotNone(highPriceBuyOrder, lowPriceSellOrder) if getRandomValue() > 0 else getNotNone(
            lowPriceSellOrder, highPriceBuyOrder)
        # Log("选中订单情况",json.dumps(rivalOrder))
        if rivalOrder:
            printfTableAddData("交易类型", "吃单")
            price = round(rivalOrder.Price, minPeiceDiffrent)
            count = round(rivalOrder.Amount - rivalOrder.DealAmount, minCountDiffrent)
            printfTableAddData("价格", price)
            printfTableAddData("数量", count)
            if count >= minExchangeCount:
                printfTableAddData("备注", "对手ID" + str(rivalOrder.Id))
                func = getOrderRivalFunc(rivalOrder.Type)
                printfTableAddData("操作", func[1])
                func[0](price, count)
            else:
                printfTableAddData("备注", "撤销(" + str(rivalOrder.Id) + ")")
                exchange.CancelOrder(rivalOrder.Id)
            printfTable()
    else:
        # Log(_N(cls.nextEatOrderTime - time.time(),2),"秒后查看存单情况以吃单")
        pass


def getOrderRivalFunc(orderType):
    return {
        ORDER_TYPE_BUY: (exchange.Sell, "卖出"),
        ORDER_TYPE_SELL: (exchange.Buy, "买入")
    }[orderType]


def getNotNone(*args):
    for arg in args:
        if arg:
            return arg


def getRandomSendOrderFunc(tempExchange):
    return {
        True: (tempExchange.Sell, "卖出"),
        False: (tempExchange.Buy, "买入")
    }[getRandomValue() > 0]


def exchangeTimeToLocal(fromTimeString):
    return datetime.strptime(fromTimeString, "%Y-%m-%dT%H:%M:%S.%f%z")


def getNowDateTime():
    return datetime.now().astimezone(timezone(timedelta(hours=8)))


def printfTableAddData(key, value):
    ext.logStatusArrBuffer[key] = [value]


def clearStatusArrBuffer():
    ext.logStatusArrBuffer = pd.DataFrame()


def printfTable():
    ext.logStatusArr = pd.concat([ext.logStatusArrBuffer, ext.logStatusArr], axis=0, join="outer", ignore_index=True)
    while len(ext.logStatusArr) > historyCount:
        ext.logStatusArr.drop([historyCount], axis=0, inplace=True)
    keys = ext.logStatusArr.columns.values.tolist()
    values = ext.logStatusArr.values.tolist()

    runStatusTable = {"type": 'table', "title": '运行状态', "cols": keys, "rows": values}
    LogStatus("`" + json.dumps(runStatusTable) + "`")


def refreshEatOrderTime():
    ext.nextEatOrderTime = time.time() + eatOrderTime + eatOrderTimeFloat * getRandomValue()

json.dumps(ensure_ascii=False)
def refreshSendOrderTime():
    ext.nextSendOrderTime = time.time() + sendOrderTime + sendOrderTimeFloat * getRandomValue()


def main():
    LogReset(1)

    ext.logStatusArr = pd.DataFrame()
    clearStatusArrBuffer()

    refreshEatOrderTime()
    refreshSendOrderTime()

    while True:
        # onTicker()
        try:
            # Log("---------------------------------------------------")
            onTicker()
            pass
        except Exception as e:
            Log(e)
        finally:
            Sleep(2000)