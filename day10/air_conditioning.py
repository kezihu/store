# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 9:26
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : air_conditioning.py
import time


# 定义空调类
class air_conditioning:
    __grand = 0  # 屏幕大小
    __price = 0  # 价格

    # 设置品牌
    def setgrand(self, grand):
        self.__grand = grand

    # 获取品牌
    def getgrand(self):
        return self.__grand

    # 设置价格
    def setprice(self, price):
        if price < 0:
            print("对不起，输入非法！")
        else:
            self.__price = price

    # 获取价格
    def getprice(self):
        return self.__price

    # 空调开机
    def turn_on(self):
        print('空调开机了...')

    # 关闭空调
    def turn_off(self, num):
        if num.isdigit():
            num = int(num)
            print('空调将在', num, '分钟后自动关闭...')
            n = num * 60
            time.sleep(n)
            print('空调已关机！')
        else:
            print('对不起，输入非法！')

    # 展示笔记本电脑
    def show(self):
        print("品牌:", self.__grand, "价格:", self.__price, "元。")


# 具体化空调
myair_conditioning = air_conditioning()
myair_conditioning.setgrand('格力')
myair_conditioning.setprice(5000)
myair_conditioning.show()
myair_conditioning.turn_on()
myair_conditioning.turn_off('1')
