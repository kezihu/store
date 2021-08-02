# -*- coding: utf-8 -*-
# @Time    : 2021/7/29 15:04
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : cup.py
class Cup:
    __height = 0  # 高度
    __volume = 0  # 容积
    __color = ''  # 颜色
    __material = ''  # 材质

    # 设置高度
    def setHeight(self, height):
        if height < 0:
            print('高度输入错误！')
        else:
            self.__height = height

    # 获取高度
    def getHeight(self):
        return self.__height

    # 设置容积
    def setVolume(self, volume):
        if volume < 0:
            print('容积输入错误！')
        else:
            self.__volume = volume

    # 获取容积
    def getVolume(self):
        return self.__volume

    # 设置颜色
    def setColor(self, color):
        self.__color = color

    # 获取颜色
    def getColor(self):
        return self.__color

    # 设置材质
    def setMaterial(self, material):
        self.__material = material

    # 获取材质
    def getMaterial(self):
        return self.__material

    # 展示水杯
    def show(self):
        print("高度:", self.__height, "cm,容积:", self.__volume, "ml,颜色:", self.__color, "材质:", self.__material)

    # 盛水
    def holdWater(self):
        print("能存放液体")


# 具体化水杯
mycup = Cup()
mycup.setHeight(500)
mycup.setVolume(1000)
mycup.setColor("红色")
mycup.setMaterial("水晶")
print('这个水杯的高度为', mycup.getHeight(), "容积为", mycup.getVolume(), "颜色为", mycup.getColor(), "材质为", mycup.getMaterial())
mycup.show()
mycup.holdWater()
