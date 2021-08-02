# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 16:25
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : phone.py
import time


# 定义老手机类
class oldphone(object):
    __brand = ""

    # 构造方法
    def __init__(self, brand):
        self.__brand = brand

    # 设置品牌
    def setbrand(self, brand):
        self.__brand = brand

    # 获取品牌
    def getbrand(self):
        return self.__brand

    # 打电话
    def call(self, number):
        print("正在给", number, "打电话")
        for i in range(8):
            print(".", end="")
            time.sleep(1)


# 定义新手机类
class newphone(oldphone):

    # 打电话
    def call(self, number):
        # 语音拨号中交给新手机
        print("语音拨号中")
        for i in range(3):
            print(".", end="")
            time.sleep(1)

        # 正在打电话交给老手机来运行
        super().call(number)

    # 展示
    def show(self):
        print("品牌为:", super().getbrand(), "的手机很好用...")


phone = newphone("huawei")
phone.show()
phone.call("15227067110")
