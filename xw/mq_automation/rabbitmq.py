#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author:renyi
date:20191031
https://rawcdn.githack.com/rabbitmq/rabbitmq-management/v3.7.3/priv/www/api/index.html
"""
import requests
import json


class MQ(object):
    def __init__(self):
        self.host = "http://192.168.133.134:15672"
        self.request = requests.session()
        self.request.auth = ('guest', 'guest')
        self.headers = {
            'content-type': 'application/json',
        }

    def getOverView(self):
        url = self.host + "/api/overview"
        response = self.request.get(url)
        print(response.text)

    def getExchange(self, exchangeName):
        url = self.host + "/api/exchanges/%2F/{}".format(exchangeName)
        response = self.request.get(url=url, headers=self.headers)
        if response.status_code == 200:
            print("exchange: {}已经存在!".format(exchangeName))
        elif response.status_code == 404:
            print("exchange: {}不存在!".format(exchangeName))

    def putExchange(self, exchangeName):
        url = self.host + "/api/exchanges/%2F/{}".format(exchangeName)
        data = {"type": "direct", "durable": "true"}
        response = self.request.put(url=url, headers=self.headers, data=json.dumps(data))
        print("正在创建exchange: {}".format(exchangeName))
        if response.status_code == 201:
            print("创建exchange: {}成功".format(exchangeName))
        elif response.status_code == 204:
            print("exchange: {}已经存在!".format(exchangeName))
        else:
            print("未知返回,请检查!")

    def deleteExchange(self, exchangeName):
        url = self.host + "/api/exchanges/%2F/{}".format(exchangeName)
        response = self.request.delete(url, headers=self.headers)
        if response.status_code == 204:
            print("删除exchange: {}成功".format(exchangeName))
        elif response.status_code == 404:
            print("exchange: {}已经删除或不存在!".format(exchangeName))
        else:
            print("未知返回,请检查!")

    def getQueue(self, queueName):
        url = self.host + "/api/queues/%2F/{}".format(queueName)
        response = self.request.get(url=url, headers=self.headers)
        if response.status_code == 200:
            print("queue: {}存在!".format(queueName))
        elif response.status_code == 404:
            print("queue: {}不存在!".format(queueName))
            return None
        queuesMessageUrl = self.host + "/api/queues/%2F/{}/bindings".format(queueName)
        queuesMessage = self.request.get(url=queuesMessageUrl, headers=self.headers)
        # print(queuesMessage.text)
        return queuesMessage.text

    def putQueue(self, queueName):
        url = self.host + "/api/queues/%2F/{}".format(queueName)
        # data1 = {"auto_delete": "false", "durable": "true", "arguments": {}, "node": "rabbit@renyi"}
        data = {"auto_delete": "false", "durable": "true", "arguments": {}}
        response = self.request.put(url=url, headers=self.headers, data=json.dumps(data))
        if response.status_code == 201:
            print("创建queue: {}成功".format(queueName))
        elif response.status_code == 204:
            print("queue: {}已经存在!".format(queueName))
        else:
            print("未知返回,请检查!")

    def deleteQueue(self, queueName):
        url = self.host + "/api/queues/%2F/{}".format(queueName)
        response = self.request.delete(url, headers=self.headers)
        if response.status_code == 204:
            print("删除queue: {}成功".format(queueName))
        elif response.status_code == 404:
            print("queue: {}已经删除或不存在!".format(queueName))
        else:
            print("未知返回,请检查!")

    def bind(self, exchangeName, queueName, routingKey, arguments=None):
        url = self.host + "/api/bindings/%2F/e/{}/q/{}".format(exchangeName, queueName)
        arguments = arguments or {}
        data = {"routing_key": routingKey, "arguments": arguments}
        response = self.request.post(url, headers=self.headers, data=json.dumps(data))
        print("{},{},{}".format(exchangeName, queueName, routingKey) + "开始绑定")
        if response.status_code == 201:
            print("{},{},{}".format(exchangeName, queueName, routingKey) + "绑定成功")
        elif response.status_code == 500:
            print("{},{},{}".format(exchangeName, queueName, routingKey) + "绑定失败")
        else:
            print("未知返回,请检查status_code" + response.status_code)

    def getPropertiesKey(self, exchangeName, queueName, routingKey, arguments=None):
        """
        根据exchangeName,queueName,routingKey,arguments,获取properties_key
        :return: properties_key
        """
        arguments = arguments or {}
        queueInfos = self.getQueue(queueName)
        if queueInfos:
            queueInfos = json.loads(queueInfos)
            for queueInfo in queueInfos:
                if queueInfo.get("source") == exchangeName and queueInfo.get(
                        "routing_key") == routingKey and queueInfo.get("arguments") == arguments:
                    return queueInfo.get("properties_key")
        return None

    def unBind(self, exchangeName, queueName, routingKey, arguments=None):
        propertyKey = self.getPropertiesKey(exchangeName, queueName, routingKey, arguments=arguments)
        url = self.host + "/api/bindings/%2F/e/{}/q/{}/{}".format(exchangeName, queueName, propertyKey)
        response = self.request.delete(url, headers=self.headers)
        if response.status_code == 204:
            print("{}, {}, {},解除成功".format(exchangeName, queueName, routingKey))
        elif response.status_code == 404:
            print("{}, {}, {},绑定关系不存在".format(exchangeName, queueName, routingKey))
        else:
            print("{}, {}, {},解除绑定失败,请检查".format(exchangeName, queueName, routingKey))


if __name__ == '__main__':
    mq = MQ()
    # mq.deleteExchange("myExchange111")
    # mq.getExchange("myExchange111")
    # mq.putExchange("myExchange111")
    # mq.getExchange("myExchange111")
    # mq.deleteExchange("myExchange111")
    # mq.getQueue("MyQueue23")
    mq.putQueue("MyQueue9999")
    # mq.getQueue("MyQueue23")
    # mq.deleteQueue("MyQueue23")
    # mq.getQueue("MyQueue23")
    # mq.bind("myExchange", "MyQueue23", "my_routing_key111")
    # mq.getQueue("MyQueue23")
    # mq.unBind("myExchange", "MyQueue23", "my_routing_key111")
    # mq.getQueue("MyQueue23")
    # mq.bind("CMP_MQ_INS_EXCHANGE", "CMP.ins_claims_notice", "CMP.ins_claims_notice")
    # mq.unBind("CMP_MQ_INS_EXCHANGE", "CMP.ins_claims_notice", "CMP.ins_claims_notice")
