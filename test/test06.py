# -*- coding: utf-8 -*-
import uuid
import time
import requests
import json

baseUrl = "http://47.52.204.159:8001"

userName = None
source = None
strategy = None
ordersIdList = []
orderDataList = []
instance = None
orderStatusCallback = None


class GlobalVariable(object):
    pass


g = GlobalVariable()


class Order(object):
    def __init__(self, order_id):
        self.user_id = userName
        self.source = source
        self.strategy = strategy
        self.instance = instance
        self.time = None
        self.order_id = order_id
        self.market = None
        self.symbol = None
        self.order_type = None
        self.exchange_type = None
        self.amount = None
        self.price = None
        self.deal_amount = None
        self.avg_price = None
        self.status = None
        self.turnover_ratio = None
        self.order_total = None
        self.comment = None

    def getSendDic(self):
        self.time = int(time.time() * 1000)
        return self.__dict__


def initInfo(user, sour, stra, order):
    '''
    :param user: 用户名称
    :param sour: 数据来源，如"FMZ"
    :param stra: 策略名称，如"海龟策略"
    :param instan: 策略运行实例，区分每次策略的运行
    :param order: 为回调函数，通过此函数传入orderId得到订单信息
    :return: 无
    '''
    try:
        global userName
        global source
        global strategy
        global instance
        global orderStatusCallback
        userName = user
        source = sour
        strategy = str(stra)
        instance = str(uuid.uuid4())
        orderStatusCallback = order
    except Exception as e:
        pass


def httpPost(url, data):
    '''
    发送数据函数
    :param url: url
    :param data: data
    :return: None
    '''
    try:
        response = requests.post(url=url, json=data)
    except requests.exceptions.ConnectionError as e:
        pass
    return


class RdasLog(object):

    @classmethod
    def baseLog(cls, data, type):
        url = baseUrl + "/log/"
        data["log_type"] = type
        httpPost(url=url, data=data)

    @classmethod
    def errorAndComment(cls, market, comment, content):
        postData = {"time": int(time.time() * 1000), "market": market, "log_type": "error", "content": content,
                    "source": source,
                    "user_id": userName, "strategy": strategy, "instance": instance, "comment": comment}
        cls.baseLog(postData, "error")

    @classmethod
    def error(cls, market, *content):
        '''
        错误日志处理
        :param market:交易所
        :param content:
        :return:
        '''
        try:
            tmp = json.dumps(content, ensure_ascii=False)
            cls.errorAndComment(market, "", tmp)
        except Exception as e:
            pass

    @classmethod
    def infoAndComment(cls, market, comment, content):
        postData = {"time": int(time.time() * 1000), "market": market, "log_type": "info", "content": content,
                    "source": source,
                    "user_id": userName, "strategy": strategy, "instance": instance, "comment": comment}
        cls.baseLog(postData, "info")

    @classmethod
    def info(cls, market, *content):
        '''
            日常日志处理
        :param market:
        :param content:
        :return:
        '''
        try:
            content = json.dumps(content, ensure_ascii=False)
            cls.infoAndComment(market, "", content)
        except Exception as e:
            pass


class RdasTrans(object):

    @classmethod
    def transHelper(cls, id, tempExchange):
        '''
        convert order object to order json data
        :param id:订单id
        :return: 包含market,status,symbol,order_id,avg_price,order_type,exchange_type,amount,deal_amount,price,comment的字典
        '''
        oldOrder = Order(id)
        order = orderStatusCallback(oldOrder, tempExchange)
        # 将数据格式转化为字符串
        order = {k: str(v) for k, v in order.__dict__.items() if k != "time"}
        # 将两个字典组合
        postData = dict({"time": int(time.time() * 1000), "source": source, "user_id": userName,
                         "strategy": strategy, "instance": instance}, **order)
        return postData

    @classmethod
    def data(cls, orderId, tempExchange):
        '''
        交易数据处理函数
        :param orderId:订单id
        :return:
        '''
        try:
            url = baseUrl + "/transaction/"
            postData = cls.transHelper(orderId, tempExchange)
            orderDataList.append(orderId)
            httpPost(url=url, data=postData)
        except Exception as e:
            pass

    @classmethod
    def transIdHandler(cls, orderId):
        try:
            if orderId not in ordersIdList:
                ordersIdList.append(orderId)
        except Exception as e:
            pass


def accountHandler(account):
    '''
    账户数据处理
    :param account:
    :return:
    '''
    try:
        account = {k: str(v) for k, v in account if k != "time"}
        postData = dict({"time": int(time.time() * 1000), "source": source, "user_id": userName,
                         "strategy": strategy, "instance": instance}, **account)
        # postData = {"time": int(time.time() * 1000), "market": market, "account_type": account_type,
        #             "currency": currency,
        #             "available": available,
        #             "frozen": frozen, "cny_count": cny_count, "source": source,
        #             "user_id": userName, "comment": comment}
        url = baseUrl + "/account/"
        httpPost(url=url, data=postData)
    except Exception as e:
        pass


if __name__ == '__main__':
    initInfo("renyi", "FMZ", "海归策略", "1", 1)
    # errorLogHandler("okex", "测试日志1", "测试日志2", "测试日志3")
    RdasTrans.data(15709753972)
