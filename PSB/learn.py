# -*- coding: utf-8 -*-
# @Time    : 2021/8/4 20:27
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : learn.py
# education = [
#     '没有教育历史（包括幼儿园）',
#     '小学文化',
#     '初中文化',
#     '高中文化',
#     '大学文化（研究生）',
#     '研究生',
#     '博士生',
#     '教授'
# ]
# # 打印文化程度列表
# def culture():
#     print('-'.center(40, '-'))
#     for key, name in enumerate(education):
#         print('\t\t\t', key, name)
#     print('-'.center(40, '-'))
from DBUtils import select, update
from addUser import add_citizen

textbook = [
    '小学课本',
    '初中课本',
    '高中课本',
    '大学课本',
    '研究生课本',
    '博士生课本',
    '教授课本'
]


# 打印课本列表
def book():
    print('-'.center(40, '-'))
    for key, name in enumerate(textbook):
        print('\t\t\t', key, name)
    print('-'.center(40, '-'))


def library(record, choose):
    if record[13] < choose:
        return 0
    elif record[13] == choose:
        return 1
    elif record[13] > choose:
        return 2


# 普通公民操作逻辑
def ordinaryCitizen():
    print('\033[31;5m-------------------------\033[31;0m')
    print('\033[31;5m-\t\t1.注册信息\t\t-\033[31;0m')
    print('\033[31;5m-\t\t2.学习\t\t\t-\033[31;0m')
    print('\033[31;5m-------------------------\033[31;0m')
    operation = input('\033[33;5m请选择您要进行的操作：\n\033[33;0m')
    if operation.isdigit():
        operation = int(operation)
        if operation == 1:
            add_citizen()
        elif operation == 2:
            cardId = input('\033[33;5m请输入您的身份证号码：\033[33;0m\n')
            sql = 'SELECT * FROM citizen WHERE cardID = %s'
            data = [cardId]
            model = 'one'
            record = select(sql, data, model, [])
            if record is None:
                print('\033[36;5m抱歉，该用户不存在！\033[36;0m')
            else:
                book()
                choose = input('\033[33;5m请选择您想要学习的课本编号：\033[33;0m\n')
                if choose.isdigit():
                    choose = int(choose)
                    if choose > 7:
                        print('\033[36;5m抱歉，您选择的课本不存在！\033[36;0m')
                    else:
                        datum = library(record, choose)
                        if datum == 0:
                            print('\033[36;5m抱歉，您文化程度不够，请先学习相对低水平的课本。\033[36;0m')
                        elif datum == 1:
                            sql = 'UPDATE citizen SET education = %s WHERE cardID =%s '
                            data = [choose + 1, cardId]
                            update(sql, data)
                            sql = 'SELECT NAME FROM edulevel WHERE id = %s;'
                            data = [choose]
                            model = 'one'
                            record1 = select(sql, data, model, [])
                            print('\033[34;5m您开始学习', textbook[choose], '!\033[34;0m')
                            print('\033[34;5m您当前的文化水平为', record1[0], '!\033[34;0m')
                        elif datum == 2:
                            print('\033[36;5m程度已经达到，没必要在学习本课程！\033[36;0m')
                else:
                    print('\033[36;5m抱歉，编号输入错误！\033[36;0m')
        else:
            print('\033[36;5m您选择的操作不存在！\033[36;0m')
    else:
        print('\033[36;5m请输入数字！\033[36;0m')
