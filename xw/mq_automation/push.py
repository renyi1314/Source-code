#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import rabbitmq


class jsonCaptor(object):

    @staticmethod
    def loadJson():
        with open("mq_pro.json", mode="r") as f:
            try:
                loadDict = json.load(f)
                # a = 1
                return loadDict
            except ValueError as e:
                print("配置格式错误请检查")
                print(e)
                exit(1)
            return None

    def define(self):
        loadDict = self.loadJson()
        if not loadDict:
            exit(1)
        exchanges = loadDict.get("exchanges")
        if exchanges:
            needCreateExchanges = []
            for exchange in exchanges:
                if exchange.get("name"):
                    needCreateExchanges.append(exchange.get("name").strip())
            print("需要创建的exchange: {}".format(needCreateExchanges))
        queues = loadDict.get("queues")
        if queues:
            needCreateQueues = []
            for queue in queues:
                if queue.get("name"):
                    needCreateQueues.append(queue.get("name").strip())
            print("需要创建的queue: {}".format(needCreateQueues))
        bindings = loadDict.get("bindings")
        if bindings:
            needBindings = []
            for binding in bindings:
                bind = {"exchange": binding.get("source"), "queue": binding.get("destination"),
                        "routing_key": binding.get("routing_key")}
                needBindings.append(bind)
            print("需要创建的绑定关系: {}".format(needBindings))
        unBindings = loadDict.get("unBindings")
        if unBindings:
            needUnBindings = []
            for unBinging in unBindings:
                unBind = {"exchange": unBinging.get("source"), "queue": unBinging.get("destination"),
                          "routing_key": unBinging.get("routing_key")}
                needUnBindings.append(unBind)
            print("需要解除的绑定关系: {}".format(needUnBindings))

    def pushConfig(self):
        mq = rabbitmq.MQ()
        loadDict = self.loadJson()
        if not loadDict:
            exit(1)
        exchanges = loadDict.get("exchanges")
        if exchanges:
            for exchange in exchanges:
                if exchange.get("name"):
                    mq.putExchange(exchange.get("name"))
        queues = loadDict.get("queues")
        if queues:
            for queue in queues:
                if queue.get("name"):
                    mq.putQueue(queue.get("name"))
        bindings = loadDict.get("bindings")
        if bindings:
            for binding in bindings:
                mq.bind(binding.get("source"), binding.get("destination"), binding.get("routing_key"))


if __name__ == '__main__':
    captor = jsonCaptor()
    captor.loadJson()
    captor.define()
    captor.pushConfig()
    print(1111)
