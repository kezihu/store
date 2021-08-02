# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 14:00
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : bread.py
"""
    厨师：0.5秒制作一个面包，3个厨师同时制作面包，当篮子的面包满了，厨师会等待0.5秒。
    顾客：每个人3000元，同时去买面包，当面包不够时，顾客需要等待一秒。
    篮子：最多容纳600个面包，每个2元。
    一共有六个顾客去抢面包。
"""
import time
from threading import Thread

basket = 0  # 篮子


# 厨师制作面包
class baker(Thread):
    def run(self) -> None:
        global basket
        t = 0  # 判断顾客是否都已买完
        while True:
            if basket == 600:
                time.sleep(0.5)
                t += 0.5
                if t == 5:
                    print('顾客已将钱全部购买面包！')
                    break
            else:
                time.sleep(0.5)
                basket += 1


# 顾客买面包
class customer(Thread):
    username = ''

    def run(self) -> None:
        money = 3000  # 每个顾客拥有的钱数
        count = 0
        while True:
            if money < 2:
                print(self.username, '顾客钱已花完，成功购买', count, '个面包。')
                break
            else:
                if basket < 1:
                    time.sleep(1)
                else:
                    count += 1
                    money -= 2
                    print('成功购买一个面包！')


baker1 = baker()
baker2 = baker()
baker3 = baker()
customer1 = customer()
customer2 = customer()
customer3 = customer()
customer4 = customer()
customer5 = customer()
customer6 = customer()
customer1.username = '一号'
customer2.username = '二号'
customer3.username = '三号'
customer4.username = '四号'
customer5.username = '五号'
customer6.username = '六号'

baker1.start()
baker2.start()
baker3.start()
customer1.start()
customer2.start()
customer3.start()
customer4.start()
customer5.start()
customer6.start()
