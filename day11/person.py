# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 9:25
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : person.py

class person(object):
    __age = 0
    __sex = ""
    __name = ""

    # 构造方法
    def __init__(self, age, sex, name):
        self.__age = age
        self.__sex = sex
        self.__name = name

    # 设置年龄
    def setage(self, age):
        if age < 0 or age > 100:
            print("输入非法!")
        else:
            self.__age = age

    # 获取年龄
    def getage(self):
        return self.__age

    # 设置性别
    def setsex(self, sex):
        self.__sex = sex

    # 获取性别
    def getsex(self):
        return self.__sex

    # 设置姓名
    def setname(self, name):
        self.__name = name

    # 获取姓名
    def getname(self):
        return self.__name


# 定义工人类
class worker(person):

    def work(self):
        print("正在干活")


# 定义学生类
class student(person):
    __id = 0

    # 设置学号
    def setid(self, id):
        self.__id = id

    # 获取学号
    def getid(self):
        return self.__id

    # 学习
    def study(self):
        print("学习中...")

    # 唱歌
    def sing(self):
        print("会唱歌")


w = worker(20, "男", "丁一")
print("工人:", w.getname(), w.getsex(), "今年", w.getage(), "岁")
w.work()
s = student(10, "女", "王玉")
s.setid(135)
print("学生:", s.getname(), s.getsex(), "学号:", s.getid(), "今年", s.getage(), "岁")
s.study()
s.sing()
