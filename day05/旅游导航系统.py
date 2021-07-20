# -*- coding: utf-8 -*-
# @Time    : 2021/7/20 15:08
# @Author  : Kevin_liu
# @File    : 旅游导航系统.py
from 商城系统 import shopping
from 景点 import place


def sight(choose):
    for i in choose:
        print(i)


print('-'.center(60, '-'))
for i in place:
    print(i.center(60))
print('-'.center(60, '-'))

while True:
    city = input('请选择您想要旅游的城市：\n')
    if city in place:
        print('-'.center(60, '-'))
        sight(place[city])
        print('-'.center(60, '-'))

        sight1 = input('请输入您想要了解的景点：\n')
        if sight1 in place[city]:
            sight(place[city][sight1])

            note = input('请输入您想要了解的内容：\n')
            if note in place[city][sight1]:
                print(place[city][sight1][note])
                a = input('您是否需要购买一些纪念品：y/n\n')
                if a == 'y':
                    shopping()
                else:
                    break
            else:
                print('请正确输入您想要了解的内容！')
        else:
            print('请正确输入您想要了解的景点！')
    else:
        print('请正确输入您想要旅游的城市！')
