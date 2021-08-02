# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 9:27
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : phone.py
# 定义使用者
class person:
    __name = ""
    __sex = ""
    __age = 0
    __remainingCharge = 0
    __phoneBrand = ""
    __phoneBattery = 0
    __phoneScreen = 0
    __holdTime = 0
    __integral = 0

    # 设置姓名
    def setname(self, name):
        self.__name = name

    # 获取姓名
    def getname(self):
        return self.__name

    # 设置性别
    def setsex(self, sex):
        self.__sex = sex

    # 获取性别
    def getsex(self):
        return self.__sex

    # 设置年龄
    def setage(self, age):
        if age < 0 or age > 110:
            print("对不起，输入非法！")
        else:
            self.__age = age

    # 获取年龄
    def getage(self):
        return self.__age

    # 设置剩余话费
    def setremainingCharge(self, remainingCharge):
        self.__remainingCharge = remainingCharge

    # 获取剩余话费
    def getremainingCharge(self):
        return self.__remainingCharge

    # 设置手机品牌
    def setphoneBrand(self, phoneBrand):
        self.__phoneBrand = phoneBrand

    # 获取手机品牌
    def getphoneBrand(self):
        return self.__phoneBrand

    # 设置手机电池容量
    def setphoneBattery(self, phoneBattery):
        if phoneBattery < 0:
            print("对不起，输入非法！")
        else:
            self.__phoneBattery = phoneBattery

    # 获取手机电池容量
    def getphoneBattery(self):
        return self.__phoneBattery

    # 设置手机屏幕大小
    def setphoneScreen(self, phoneScreen):
        if phoneScreen < 0:
            print("对不起，输入非法！")
        else:
            self.__phoneScreen = phoneScreen

    # 获取手机屏幕大小
    def getphoneScreen(self):
        return self.__phoneScreen

    # 设置手机最大待机时长
    def setholdTime(self, holdTime):
        if holdTime < 0:
            print("对不起，输入非法！")
        else:
            self.__holdTime = holdTime

    # 获取手机最大待机时长
    def getholdTime(self):
        return self.__holdTime

    # 设置所拥有的积分
    def setintegral(self, integral):
        if integral < 0:
            print("对不起，输入非法！")
        else:
            self.__integral = integral

    # 获取所拥有的积分
    def getintegral(self):
        return self.__integral

    # 发短信
    def sendMessage(self, message):
        print(message)

    # 打电话
    def phone(self, remainingCharge, integral, num, time):
        if num is None:
            print("号码不为空")
        elif remainingCharge < 1:
            print("本人话费小于1元")
        else:
            print("通话成功...", time, "分钟后通话结束")
            if 0 < time < 10:
                newremainingCharge = remainingCharge - 1 * time
                newintegral = integral + 15 * time
                print("剩余话费是:", newremainingCharge, "元，拥有积分是:", newintegral)
            elif 10 <= time <= 20:
                newremainingCharge = remainingCharge - 0.8 * time
                newintegral = integral + 39 * time
                print("剩余话费是:", newremainingCharge, "元，拥有积分是:", newintegral)
            else:
                newremainingCharge = remainingCharge - 0.65 * time
                newintegral = integral + 48 * time
                print("剩余话费是:", newremainingCharge, "元，拥有积分是:", newintegral)


# 具体化使用者
a = person()
a.setname("丁一")
a.setsex("男")
a.setage(10)
a.setremainingCharge(30)
a.setphoneBrand("huawei")
a.setphoneBattery(4200)
a.setphoneScreen(5.2)
a.setholdTime(10)
a.setintegral(30)
print("姓名是:", a.getname(), "性别是:", a.getsex(), "年龄是:", a.getage(), "剩余话费是:", a.getremainingCharge(),
      "元，手机品牌是:", a.getphoneBrand(), "，电池容量是:", a.getphoneBattery(), "毫安，屏幕大小是:", a.getphoneScreen(),
      "存，待机时长是:", a.getholdTime(), "小时，积分是:", a.getintegral())

message = input("请输入短信内容:")
num = input("请输入您要拨打的电话号码:")
time = int(input("请输入通话时长:"))
a.sendMessage(message)
a.phone(a.getremainingCharge(), a.getintegral(), num, time)
