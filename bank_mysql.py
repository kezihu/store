# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 15:05
# @Author  : Kevin_liu
# @Email   : 87281094@xxx.com
# @File    : bank_mysql.py
import pymysql
import random

con = pymysql.connect(host='localhost', user='root', password='123456', database='bank')
cur = con.cursor()
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称


def bank_addUser(account, username, password, country, province, street, gate, money):
    # 1.判断数据库是否已满
    cur.execute("SELECT * from user")
    record = cur.fetchone()
    if len(record) >= 100:
        return 3
    else:
        # 2.判断用户是否存在
        cur.execute("SELECT * from user where account = %s" % account)
        record1 = cur.fetchone()
        if record1 is not None:
            return 2
        else:
            # 3.正常开户
            sql = "insert into  user values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            a = [account, username, password, country, province, street, gate, money, bank_name]
            cur.execute(sql, a)
            con.commit()
            return 1


# 银行的存钱逻辑
def bank_saveMoney(account, saveMon):
    cur.execute("SELECT account FROM `user` where account = %s " % account)
    record = cur.fetchone()
    if record is None:
        return False
    else:
        sql = 'UPDATE `user` SET money = money + %s WHERE account = %s'
        a = [saveMon, account]
        cur.execute(sql, a)
        con.commit()


# 银行的取钱逻辑
def bank_getMoney(account, pwd, getMon):
    cur.execute("SELECT * FROM `user` where account = %s" % account)
    record = cur.fetchone()
    li = [record]
    if record is None:
        return 1
    if li[0][2] != pwd:
        return 2
    if li[0][7] < getMon:
        return 3


# 银行的转账逻辑
def bank_transferMoney(account, account1, pwd, transferMon):
    cur.execute("SELECT * FROM `user` where account = %s" % account)
    record = cur.fetchone()
    li = [record]
    if record is None:
        return 1
    cur.execute("SELECT * FROM `user` where account = %s" % account1)
    record = cur.fetchone()
    if record is None:
        return 1
    if li[0][2] != pwd:
        return 2
    if li[0][7] < transferMon:
        return 3


# 银行的查询逻辑
def bank_query(account, pwd):
    cur.execute("SELECT * FROM `user` where account = %s" % account)
    record = cur.fetchone()
    li = [record]
    if record is None:
        print('\033[33;1m您输入的账号不存在！\033[0m')
        query()
    else:
        if li[0][2] != pwd:
            print('\033[33;1m您输入的密码不正确！\033[0m')
            query()
        else:
            print('查询成功，您的个人信息如下:')
            info = '''\033[35;1m
                        ----------个人信息----------
                        用户名：%s
                        密码：%s
                        账号：%s
                        地址信息
                            国家：%s
                            省份：%s
                            街道：%s
                            门牌号: %s
                        余额：%s
                        开户行地址：%s
                        ---------------------------\033[35;0m
                    '''
            print(info % (li[0][1], li[0][2], li[0][0], li[0][3], li[0][4], li[0][5], li[0][6], li[0][7],
                          li[0][8]))


# 菜单界面
def welcome():
    print('*'.center(40, '*'))
    print('*         中国工商银行-账户管理系统         *')
    print('*'.center(40, '*'))
    print('*                1.开户                 *')
    print('*                2.存钱                 *')
    print('*                3.取钱                 *')
    print('*                4.转账                 *')
    print('*                5.查询                 *')
    print('*                6.Bye!                *')
    print('*'.center(40, '*'))


# 开户
def addUser():
    username = input("请输入您的用户名：")
    while True:
        password = input("请输入您的开户密码：")
        if len(password) != 6:
            print('\033[33;1m密码必须设置为6位！\033[0m')
        else:
            if password.isdigit():
                password = int(password)
                break
            else:
                print('\033[33;1m密码必须为数字！\033[0m')
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    money = input("请输入您的开户初始余额：")
    if money.isdigit():
        money = int(money)
    else:
        print('初始金额请输入数字！')
    account = random.randint(10000000, 99999999)  # 随机产生8位数字

    data = bank_addUser(account, username, password, country, province, street, gate, money)

    if data == 3:
        print("\033[33;1m对不起，用户库已满，请携带证件到其他银行办理！\033[0m")
    elif data == 2:
        print("\033[33;1m对不起，该用户已存在！请勿重复开户！\033[0m")
    elif data == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''\033[35;1m
            ----------个人信息----------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号: %s
            余额：%s
            开户行地址：%s
            ---------------------------\033[35;0m
        '''
        print(info % (username, password, account, country, province, street, gate, money, bank_name))


# 存钱
def saveMoney():
    account = input('请输入您的账号：\n')
    if account.isdigit():
        account = int(account)
        saveMon = input('请输入您要存入的金额：￥')
        if saveMon.isdigit():
            saveMon = int(saveMon)
            data = bank_saveMoney(account, saveMon)
            if data is False:
                print('\033[33;1m账号不存在！\033[0m')
                saveMoney()
            else:
                cur.execute("SELECT * FROM `user` where account = %s " % account)
                record = cur.fetchone()
                li = [record]
                print('\033[34;1m存钱成功，您当前余额为', li[0][7], '元！\033[0m')
        else:
            print('\033[33;1m金额输入错误，请重新输入！\033[0m')
    else:
        print('\033[33;1m账号格式输入错误，请重新输入！\033[0m')
        saveMoney()


# 取钱
def getMoney():
    account = input('请输入您的账号：\n')
    if account.isdigit():
        account = int(account)
        pwd = input('请输入您的密码：\n')
        if pwd.isdigit():
            pwd = int(pwd)
            getMon = input('请输入您要提取的金额：￥')
            if getMon.isdigit():
                getMon = int(getMon)
                data = bank_getMoney(account, pwd, getMon)
                if data == 1:
                    print('\033[33;1m您输入的账号不存在！\033[0m')
                    getMoney()
                else:
                    if data == 2:
                        print('\033[33;1m您输入的密码错误！\033[0m')
                        getMoney()
                    else:
                        if data == 3:
                            print('\033[33;1m您的账号余额不足！\033[0m')
                            getMoney()
                        else:
                            sql = "UPDATE `user` SET money = money - %s WHERE account = %s"
                            a = [getMon, account]
                            cur.execute(sql, a)
                            con.commit()
                            cur.execute("SELECT * FROM `user` where account = %s" % account)
                            record = cur.fetchone()
                            li = [record]
                            print('\033[34;1m取钱成功，您的当前余额为', li[0][7], '元！\033[0m')
            else:
                print('\033[33;1m金额输入错误，请重新输入！\033[0m')
                getMoney()
        else:
            print('\033[33;1m密码必须为数字！\033[0m')
            getMoney()
    else:
        print('\033[33;1m账号输入错误，请重新输入！\033[0m')
        getMoney()


# 转账
def transferMoney():
    account = input('请输入您的账号：\n')
    if account.isdigit():
        account = int(account)
        account1 = input('请输入您要转入的账号：\n')
        if account1.isdigit():
            account1 = int(account1)
            if account == account1:
                print('\033[33;1m不能自己给自己转账！\033[0m')
                transferMoney()
            else:
                pwd = input('请输入您的密码：\n')
                if pwd.isdigit():
                    pwd = int(pwd)
                    transferMon = input('请输入您要转的金额：\n')
                    if transferMon.isdigit():
                        transferMon = int(transferMon)
                        data = bank_transferMoney(account, account1, pwd, transferMon)
                        if data == 1:
                            print('\033[33;1m您输入的账号不存在！\033[0m')
                            transferMoney()
                        else:
                            if data == 1:
                                print('\033[33;1m您要转入的账号不存在！\033[0m')
                                transferMoney()
                            else:
                                if data == 2:
                                    print('\033[33;1m您输入的密码不正确！\033[0m')
                                    transferMoney()
                                else:
                                    if data == 3:
                                        print('\033[33;1m您的账号余额不足！\033[0m')
                                        transferMoney()
                                    else:
                                        cur.execute("SELECT * FROM `user` where account = %s" % account)
                                        record = cur.fetchone()
                                        li = [record]
                                        cur.execute('UPDATE `user` SET money = money - %s WHERE account = %s' % (transferMon, account))
                                        cur.execute('UPDATE `user` SET money = money + %s WHERE account = %s' % (transferMon, account1))
                                        con.commit()
                                        print('\033[34;1m转账成功，您向账号', account1, '转账', transferMon,
                                              '元，您的账号当前余额为：', li[0][7], '元！\033[0m')
                    else:
                        print('\033[33;1m金额请输入数字！\033[0m')
                else:
                    print('\033[33;1m密码必须为数字！\033[0m')
                    transferMoney()
        else:
            print('\033[33;1m您输入的要转入的账号格式错误！\033[0m')
            transferMoney()
    else:
        print('\033[33;1m您输入的账号格式错误！\033[0m')
        transferMoney()


# 查询
def query():
    account = input('请输入您的账号：\n')
    if account.isdigit():
        account = int(account)
        pwd = input('请输入您的密码：\n')
        if pwd.isdigit():
            pwd = int(pwd)
            bank_query(account, pwd)
        else:
            print('\033[33;1m密码必须为数字！\033[0m')
            query()
    else:
        print('\033[33;1m账号格式输入错误！\033[0m')
        query()


def exit():
    print('Bye!')


while True:
    welcome()
    num = input('请输入您要进行的业务:\n')
    if num.isdigit():
        num = int(num)
        if num == 1:
            addUser()  # 开户
        elif num == 2:
            saveMoney()  # 存钱
        elif num == 3:
            getMoney()  # 取钱
        elif num == 4:
            transferMoney()  # 转账
        elif num == 5:
            query()  # 查询
        elif num == 6:
            exit()  # 退出
            break
        else:
            print('\033[33;1m您选择的业务不存在，请重新输入！\033[0m')
    else:
        print('\033[33;1m请输入数字！\033[0m')
cur.close()
con.close()
