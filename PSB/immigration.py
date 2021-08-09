# -*- coding: utf-8 -*-
# @Time    : 2021/8/5 9:23
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : immigration.py
import datetime
import time
from dateutil import rrule
from DBUtils import select, delete, update


# 地区公安人员操作逻辑
def pub_sec_per():
    print('\033[31;5m-----------------------\033[31;0m')
    print('\033[31;5m-\t1.移民             -\033[31;0m')
    print('\033[31;5m-\t2.修改人员信誉程度   -\033[31;0m')
    print('\033[31;5m-----------------------\033[31;0m')
    operation = input('\033[33;5m请选择您要进行的操作：\033[33;0m\n')
    if operation.isdigit():
        operation = int(operation)
        if operation == 1:
            cardID = input('\033[33;5m请输入人员身份证号码：\033[33;0m\n')
            sql = 'SELECT * FROM citizen WHERE cardID = %s'
            data = [cardID]
            model = 'one'
            record = select(sql, data, model, [])
            if record is None:
                print('\033[36;5m您是未成年人还不能移民！\033[36;0m')
            else:
                if record[12] != 2:
                    print('\033[36;5m抱歉，您有犯罪历史，不能移民！\033[36;0m')
                else:
                    if record[13] < 4:
                        print('\033[36;5m您需要等待审核时间一年，才能进行移民！\033[36;0m')

                        data = record[10]
                        year = int(data[0:4])
                        month = int(data[5:7])
                        day = int(data[8:10])
                        date1 = datetime.date(year, month, day)

                        data = time.strftime('%Y-%m-%d')
                        year = int(data[0:4])
                        month = int(data[5:7])
                        day = int(data[8:10])
                        date2 = datetime.date(year, month, day)

                        months = rrule.rrule(rrule.MONTHLY, dtstart=date1, until=date2).count()
                        if months >= 12:
                            sql = 'DELETE FROM citizen WHERE cardID = %s'
                            data = [cardID]
                            delete(sql, data)
                            print('\033[34;5m移民成功！\033[34;0m')
                        else:
                            print('\033[36;5m您的审核时间还不足一年！\033[36;0m')
                    else:
                        print('\033[34;5m您可以移民！\033[34;0m')
                        sql = 'DELETE FROM citizen WHERE cardID = %s'
                        data = [cardID]
                        delete(sql, data)
        elif operation == 2:
            cardID = input('\033[33;5m请输入人员身份证号码：\033[33;0m\n')
            sql = 'SELECT * FROM citizen WHERE cardID = %s'
            data = [cardID]
            model = 'one'
            record = select(sql, data, model, [])
            if record is None:
                print('\033[36;5m该人员不存在！\033[36;0m')
            else:
                sql = 'SELECT name FROM credibility WHERE id = %s'
                data = [record[12]]
                model = 'one'
                record1 = select(sql, data, model, [])
                print('\033[34;5m该人员当前信任程度为：', record[12], record1[0], '\033[34;0m')
                sql = 'SELECT * FROM credibility'
                model = 'all'
                credibility = select(sql, [], model, [])
                print('\033[31;5m-------------------------------------')
                for key, name in credibility:
                    print('\t', key, name)
                print('-------------------------------------\033[31;0m')
                opt = input('\033[33;5m请选择该人员信用程度：\033[33;0m')
                if opt.isdigit():
                    opt = int(opt)
                    if 0 <= opt <= 6:
                        sql = 'UPDATE citizen SET credit = %s WHERE cardID = %s'
                        data = [opt, cardID]
                        update(sql, data)
                        print('\033[34;5m修改成功！\033[34;0m')
                    else:
                        print('\033[36;1m信用程度不存在！\033[36;0m')
                else:
                    print('\033[36;5m请输入数字！\033[36;0m')
        else:
            print('\033[36;5m您要进行的操作不存在！\033[36;0m')
    else:
        print('\033[36;5m请输入数字！\033[36;0m')
