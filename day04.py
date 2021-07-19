# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 15:41
# @Author  : Kevin_liu
# @File    : demo.py
"""
    需求：
        购物流程。
        1.商品在货架上
        2.空的购物车
        3.自己的初始化资金
    技术选型：
        1.容器
            列表： []
        2.循环技术
            while
            for i in  enumerate(li)
        3.判断
        4.键盘输入
    任务：
        [10张老干妈：7折优惠券，20张联想电脑1折优惠券]
        开始买东西之前，提示是否要抽一张优惠券。
            若是：随机给一张，最终要进行使用优惠券的进行结算。
            若否：正常买东西
"""
import random

mycart = []  # 空的购物车
consume = 0  # 消费的钱数
a = random.randint(1, 30)  # 随机产生一个优惠券
use = 0  # 用来判断是否已使用
j = 0  # 用来统计购买商品的数量

shop = [
    ['饮水机', 100],
    ['空调', 2000],
    ['联想电脑', 6000],
    ['老干妈', 10],
    ['电扇', 50],
    ['音响', 80],
    ['办公桌椅', 100]
]


# 欢迎界面
def welcome():
    print('*'.center(60, '*'))
    print('欢迎来到汉科软商场'.center(52))
    print('*'.center(60, '*'))


# 商品列表
def notice():
    print('-'.center(60, '-'))
    print('商    品   列   表'.center(57))
    print('-'.center(60, '-'))
    for name, price in enumerate(shop, 1):  # 展示商品列表
        print('\t\t\t\t\t', name, price)
    print('*\t', '温馨提示：输入 q 或者 Q 退出系统！'.center(40), '\t\t*')
    print('-'.center(60, '-'))


# 购物清单
def receipt():
    print('-'.center(60, '-'))
    print('汉    科   软   商   场   购   物   清   单'.center(54))
    print('-'.center(60, '-'))
    for name, price in enumerate(mycart, 1):
        print('\t\t\t\t\t', name, price)
    print('您本次共购买了', j, '个商品，共消费', consume, '元，您还剩余', money, '元！')
    print('-'.center(60, '-'))
    print('期    待   您   的   下   次   光   临   ！'.center(54))
    print('-'.center(60, '-'))


welcome()
# 询问是否需要优惠券
while True:
    num = input('请问您是否需要抽取一张超市优惠券？   1.需要   2.不需要\n')
    if num.isdigit():  # 输入的初始资金是数字
        num = int(num)
        if num == 1:
            if a > 10:
                print('*'.center(60, '*'))
                print('恭喜您获得联想电脑一折优惠券！'.center(52))
                print('*'.center(60, '*'))

            else:
                print('*'.center(60, '*'))
                print('恭喜您获得老干妈七折优惠券！'.center(52))
                print('*'.center(60, '*'))

            break
        elif num == 2:
            break
        else:
            print('请正确输入选项！')
    else:
        print('请正确输入选项！')

while True:
    # 初始化资金
    money = input('请输入您的初始资金：￥')
    if money.isdigit():  # 输入的初始资金是数字
        money = int(money)
        while True:
            notice()
            chose = input('请输入您要购买的商品编号：\n')  # 开始买东西
            if chose.isdigit():  # 输入的商品编号是数字
                chose = int(chose)
                chose = chose - 1
                if chose >= 7:  # 输入的商品不存在
                    print('对不起，您输入的商品不存在！')
                elif a > 10 and chose == 2 and num==1:  # 抽到联想电脑的优惠券且购买联想电脑
                    if use == 0:
                        if money < (shop[chose][1]) * 0.1:
                            print('很抱歉，您的资金不充足！')
                        else:
                            mycart.append(shop[chose])  # 将选择的商品添加到购物车中
                            consume = consume + (shop[chose][1]) * 0.1
                            money = money - (shop[chose][1]) * 0.1
                            print('-'.center(60, '-'))
                            print('购买成功，', shop[chose][0], '已加入到您的购物车里!剩余余额：￥', money)
                            use = use + 1
                            j = j + 1
                    else:
                        if money < shop[chose][1]:
                            print('很抱歉，您的资金不充足！')
                        else:
                            mycart.append(shop[chose])  # 将选择的商品添加到购物车中
                            consume = consume + shop[chose][1]
                            money = money - shop[chose][1]
                            print('-'.center(60, '-'))
                            print('购买成功，', shop[chose][0], '已加入到您的购物车里!剩余余额：￥', money)
                            j = j + 1
                elif a < 10 and chose == 3 and num == 1:  # 抽到老干妈的优惠券且购买老干妈
                    if use == 0:
                        if money < (shop[chose][1]) * 0.7:
                            print('很抱歉，您的资金不充足！')
                        else:
                            mycart.append(shop[chose])  # 将选择的商品添加到购物车中
                            consume = consume + (shop[chose][1]) * 0.7
                            money = money - (shop[chose][1]) * 0.7
                            print('-'.center(60, '-'))
                            print('购买成功，', shop[chose][0], '已加入到您的购物车里!剩余余额：￥', money)
                            use = use + 1
                            j = j + 1
                    else:
                        if money < shop[chose][1]:
                            print('很抱歉，您的资金不充足！')
                        else:
                            mycart.append(shop[chose])  # 将选择的商品添加到购物车中
                            consume = consume + shop[chose][1]
                            money = money - shop[chose][1]
                            print('-'.center(60, '-'))
                            print('购买成功，', shop[chose][0], '已加入到您的购物车里!剩余余额：￥', money)
                            j = j + 1
                else:
                    if money < shop[chose][1]:
                        print('很抱歉，您的资金不充足！')
                    else:
                        mycart.append(shop[chose])  # 将选择的商品添加到购物车中
                        consume = consume + shop[chose][1]
                        money = money - shop[chose][1]
                        print('-'.center(60, '-'))
                        print('购买成功，', shop[chose][0], '已加入到您的购物车里!剩余余额：￥', money)
                        j = j + 1
            elif chose == 'q' or chose == 'Q':
                receipt()
                break
            else:
                print('请您正确选择商品！')
    else:
        print('初始资金输入错误，系统自动退出！')
    break
