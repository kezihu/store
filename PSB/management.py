# -*- coding: utf-8 -*-
# @Time    : 2021/8/5 10:29
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : management.py
from DBUtils import *


# 查询人员
def sel_user(cardID):
    sql = 'SELECT * FROM citizen WHERE cardID = %s'
    data = [cardID]
    model = 'one'
    record = select(sql, data, model, [])
    if record is None:
        return False
    else:
        return record


# 删除人员
def del_user(cardID):
    sql = 'SELECT * FROM citizen WHERE cardID = %s'
    data = [cardID]
    model = 'one'
    record = select(sql, data, model, [])
    if record is None:
        print('\033[36;5m人员身份未备案！\033[36;0m')
    else:
        sql = 'DELETE FROM citizen WHERE cardID = %s'
        data = [cardID]
        delete(sql, data)
        print('\033[34;5m删除成功！\033[34;0m')


# 查询人员
def select_user():
    cardID = input('\033[33;5m请输入您的身份证号码：\033[33;0m\n')
    data = sel_user(cardID)
    li = [data]
    if data:
        info = '''\033[35;1m
            --------------个人信息--------------
                身份证号码：%s
                姓名：%s
                性别：%s
                年龄：%s
                密码：%s
                状态：%s
                地址信息
                    国家：%s
                    省份：%s
                    街道：%s
                    门牌号: %s
                注册日期：%s
                申请移民日期：%s
                信誉程度：%s
                文化程度：%s
                学习次数：%s
            -------------------------------\033[35;0m
        '''
        print(info % (li[0]))
    else:
        print('\033[36;5m抱歉，该用户不存在！\033[36;0m')


# 国家人员操作逻辑
def nationalStaff():
    print('\033[31;5m-------------------------\033[31;0m')
    print('\033[31;5m-\t\t1.查询人员\t\t-\033[31;0m')
    print('\033[31;5m-\t\t2.增加人员\t\t-\033[31;0m')
    print('\033[31;5m-\t\t3.删除人员\t\t-\033[31;0m')
    print('\033[31;5m-------------------------\033[31;0m')
    choose = input('\033[33;5m请选择您要进行的操作：\033[33;0m\n')
    if choose.isdigit():
        choose = int(choose)
        if choose == 1:
            print('\033[31;5m-------------------------\033[31;0m')
            print('\033[31;5m-\t1.按省份查询\t\t\t-\033[31;0m')
            print('\033[31;5m-\t2.按身份证号码查询\t\t-\033[31;0m')
            print('\033[31;5m-------------------------\033[31;0m')
            chose = input('\033[33;5m请选择您要查询的方式：\033[33;0m\n')
            if chose.isdigit():
                chose = int(chose)
                if chose == 1:
                    name = input('\033[33;5m请输入您要查询的省份：\033[33;0m\n')
                    sql = 'SELECT pid FROM province WHERE pname = %s'
                    data = [name]
                    model = 'one'
                    Id = select(sql, data, model, [])
                    if Id is None:
                        print('\033[36;5m输入的省份不存在！\033[36;0m')
                    else:
                        sql = 'SELECT * FROM citizen WHERE province = %s'
                        data = [Id]
                        model = 'all'
                        record = select(sql, data, model, [])
                        for key, name in enumerate(record):
                            print(key, name)
                elif chose == 2:
                    select_user()
                else:
                    print('\033[36;5m您输入的业务不存在！\033[36;0m')
            else:
                print('\033[36;5m请输入数字！\033[36;0m')

        elif choose == 2:
            pass
        elif choose == 3:
            cardID = input('\033[33;5m请输入您要查询的身份证号码：\033[33;0m\n')
            del_user(cardID)
        else:
            print('\033[36;5m业务不存在！\033[36;0m')
    else:
        print('\033[36;5m请输入数字！\033[36;0m')
