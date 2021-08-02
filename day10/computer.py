# -*- coding: utf-8 -*-
# @Time    : 2021/7/29 16:31
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : computer.py
# 定义笔记本电脑类
class Computer:
    __screenSize = 0  # 屏幕大小
    __price = 0  # 价格
    __cpu = ""  # cpu
    __memorySize = 0  # 内存大小
    __holdTime = 0  # 待机时长

    # 设置屏幕大小
    def setscreenSize(self, screenSize):
        if screenSize < 0:
            print("对不起，输入非法！")
        else:
            self.__screenSize = screenSize

    # 获取屏幕大小
    def getscreenSize(self):
        return self.__screenSize

    # 设置价格
    def setprice(self, price):
        if price < 0:
            print("对不起，输入非法！")
        else:
            self.__price = price

    # 获取价格
    def getprice(self):
        return self.__price

    # 设置cpu型号
    def setcpu(self, cpu):
        self.__cpu = cpu

    # 获取cpu型号
    def getcpu(self):
        return self.__cpu

    # 设置内存大小
    def setmemorySize(self, memorySize):
        if memorySize < 0:
            print("对不起，输入非法！")
        else:
            self.__memorySize = memorySize

    # 获取内存大小
    def getmemorySize(self):
        return self.__memorySize

    # 设置待机时长
    def setholdTime(self, holdTime):
        if holdTime < 0:
            print("对不起，输入非法！")
        else:
            self.__holdTime = holdTime

    # 获取待机时长
    def getholdTime(self):
        return self.__holdTime

    # 展示笔记本电脑
    def show(self):
        print("屏幕大小:", self.__screenSize, "寸,价格:", self.__price, "元,cpu型号:", self.__cpu,
              "内存大小:", self.__memorySize, "G,待机时长:", self.__holdTime, "小时")

    # 打字
    def typeWriting(self):
        print("可以打字。")

    # 打游戏
    def playGame(self):
        print("可以打游戏。")

    # 看视频
    def watch(self):
        print("可以看视频")


# 具体化笔记本电脑
mycomputer = Computer()
mycomputer.setscreenSize(14)
mycomputer.setprice(6000)
mycomputer.setcpu("intel")
mycomputer.setmemorySize(16)
mycomputer.setholdTime(10)
print('这个电脑的屏幕为', mycomputer.getscreenSize(), "寸,价格为", mycomputer.getprice(), "元，cpu为", mycomputer.getcpu(),
      "内存大小为", mycomputer.getmemorySize(), "G,待机时长为", mycomputer.getholdTime(), "小时")
mycomputer.show()
mycomputer.typeWriting()
mycomputer.playGame()
mycomputer.watch()
