# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 9:25
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : chef.py
# 定义厨师类
class chef(object):
    __name = ""
    __age = 0

    # 构造方法
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 设置姓名
    def setname(self, name):
        self.__name = name

    # 获取姓名
    def getname(self):
        return self.__name

    # 设置年龄
    def setage(self, age):
        if age < 0 or age > 100:
            print("输入非法！")
        else:
            self.__age = age

    # 获取年龄
    def getage(self):
        return self.__age

    # 蒸饭方法
    def steamRice(self):
        print("蒸饭")


# 定义厨师的子类
class son(chef):

    # 炒菜
    def cook(self):
        print("炒菜")


# 定义厨师的子类的子类
class grandson(son):

    # 蒸饭方法
    def steamRice(self):
        print("蒸饭")

    # 炒菜
    def cook(self):
        print("炒菜")


a = grandson("张丹", 10)
print("厨师", a.getname(), "今年", a.getage(), "岁")
a.steamRice()
a.cook()
