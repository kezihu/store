# -*- coding: utf-8 -*-
# @Time    : 2021/8/4 14:52
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : citizenInt.py
import time

from DBUtils import select


class citizen:
    __cardID = None  # 身份证号码
    __name = None  # 姓名
    __sex = None  # 性别
    __age = 0  # 年龄
    __password = None  # 密码
    __status = None  # 状态
    __country = None
    __province = None
    __street = None
    __door = None
    __registDate = None  # 注册日期
    __immiDate = None  # 申请移民日期
    __credit = 0  # 信誉程度
    __education = 0  # 文化程度
    __studies = 0  # 学习次数

    def __init__(self):
        self.__cardID = None  # 身份证号码
        self.__name = None  # 姓名
        self.__sex = None  # 性别
        self.__age = 0  # 年龄
        self.__password = None  # 密码
        self.__status = None  # 状态
        self.__country = None  # 国家
        self.__province = None  # 省份
        self.__street = None  # 街道
        self.__door = None  # 门牌号
        self.__registDate = None  # 注册日期
        self.__immiDate = None  # 申请移民日
        self.__credit = 0  # 信誉程度
        self.__education = 0  # 文化程度
        self.__studies = 0  # 学习次数

    # 设置身份证号码
    def setcardID(self, cardID):
        self.__cardID = cardID

    # 获取身份证号码
    def getcardID(self):
        return self.__cardID

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
        self.__age = age

    # 获取年龄
    def getage(self):
        return self.__age

    # 设置密码
    def setpassword(self, password):
        self.__password = password

    # 获取密码
    def getpassword(self):
        return self.__password

    # 设置状态
    def setstatus(self, status):
        self.__status = status

    # 获取状态
    def getstatus(self):
        return self.__status

    # 设置国家
    def setcountry(self, country):
        self.__country = country

    # 获取国家
    def getcountry(self):
        return self.__country

    # 设置省份
    def setprovince(self, province):
        self.__province = province

    # 获取省份
    def getprovince(self):
        return self.__province

    # 设置街道
    def setstreet(self, street):
        self.__street = street

    # 获取街道
    def getstreet(self):
        return self.__street

    # 设置门牌号
    def setdoor(self, door):
        self.__door = door

    # 获取门牌号
    def getdoor(self):
        return self.__door

    # 设置注册日期
    def setregistDate(self, registDate):
        self.__registDate = registDate

    # 设置注册日期
    def getregistDate(self):
        return self.__registDate

    # 设置申请移民日期
    def setimmiDate(self, immiDate):
        try:
            time.strptime(immiDate, "%Y-%m-%d")
            year = int(immiDate[0:4])
            month = int(immiDate[5:7])
            day = int(immiDate[8:10])
            # 判断月份是否不在0-12的范围内
            if month == 0 | month > 12:
                print('没有这个月份！')
            # 如果 一三五七八十腊 那么 三十一天永不差
            else:
                if month == 1 | month == 3 | month == 5 | month == 7 | month == 8 | month == 10 | month == 12:
                    if day > 31:
                        print('超出当月最大天数！')
                    else:
                        self.__immiDate = immiDate
                # 四六九冬三十天
                else:
                    if month == 4 | month == 6 | month == 9 | month == 11:
                        if day > 30:
                            print('超出当月最大天数！')
                        else:
                            self.__immiDate = immiDate
                    # 平年二月二十八，但如果年份是400的倍数，二月还是二十九天
                    else:
                        if year % 400 != 0 & year % 4 == 0:
                            if day > 28:
                                print('超出当月最大天数！')
                            else:
                                self.__immiDate = immiDate
                        else:
                            if day > 29:
                                print('超出当月最大天数！')
                            else:
                                self.__immiDate = immiDate
        except:
            print('日期格式输入错误,例如：2021-01-01\n')

    # 获取申请移民日期
    def getimmiDate(self):
        return self.__immiDate

    # 设置信誉程度
    def setcredit(self, credit):
        self.__credit = credit

    # 获取信誉程度
    def getcredit(self):
        return self.__credit

    # 设置文化程度
    def seteducation(self, education):
        self.__education = education

    # 获取文化程度
    def geteducation(self):
        return self.__education

    # 设置学习次数
    def setstudies(self, studies):
        studies = int(studies)
        self.__studies = studies

    # 获取学习次数
    def getstudies(self):
        return self.__studies
