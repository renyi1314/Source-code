# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
大话设计模式
设计模式——命令模式
命令模式(Command Pattern):将请求封装成对象，从而使可用不同的请求对客户进行参数化；对请求排队或记录请求日志，以及支持可撤消的操作.
"""


# 命令类
class Command(object):

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        pass


# 执行接收者的操作
class ConcreteCommand(Command):

    def execute(self):
        self.receiver.action()


# 接收命令
class Invoker(object):

    def __init__(self):
        # self.command = ''
        pass

    def setCommand(self, command):
        self.command = command

    def excuteCommand(self):
        self.command.execute()

    def setAndExcuteCommand(self, command):
        self.command = command
        self.command.execute()


# 具体执行类
class Receiver(object):

    @staticmethod
    def action():
        print("执行请求")


def excuteCommand(arg):
    if arg == "task":
        print("task")
    elif arg == "task2":
        print("1111")


if __name__ == "__main__":
    r = Receiver()  # 创建需要执行的命令
    c = ConcreteCommand(r)  # 绑定要执行的命令
    i = Invoker()  # 创建命令执行者
    i.setCommand(c)  # 接受命令
    i.excuteCommand()  # 执行命令
