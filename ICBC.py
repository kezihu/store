# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 10:46
# @Author  : Kevin_liu
# @File    : ICBC.py
import random

bank_name = "中国工商银行昌平回龙观支行"  # 银行名称
bank = {}  # 数据库


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, gate, money):
    # 1.判断数据库是否已满
    if len(bank) >= 100:
        return 3
    # 2.判断用户是否存在
    if account in bank:
        return 2
    # 3.正常开户
    bank[account] = {
        "username": username,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "gate": gate,
        "money": money,
        "bank_name": bank_name
    }
    return 1


# 银行的存钱逻辑
def bank_saveMoney(account, saveMon):
    if account not in bank:
        return False
    bank[account]['money'] = bank[account]['money'] + saveMon


# 银行的取钱逻辑
def bank_getMoney(account, pwd, getMon):
    if account not in bank:
        return 1
    if pwd != bank[account]['password']:
        return 2
    if getMon > bank[account]['money']:
        return 3


# 银行的转账逻辑
def bank_transferMoney(account, account1, pwd, transferMon):
    if account not in bank:
        return 1
    if account1 not in bank:
        return 1
    if pwd != bank[account]['password']:
        return 2
    if transferMon > bank[account]['money']:
        return 3


# 银行的查询逻辑
def bank_query(account, pwd):
    if account not in bank:
        print('您输入的账号不存在！')
        query()
    else:
        if pwd != bank[account]['password']:
            print('您输入的密码不正确！')
            query()
        else:
            print('查询成功，您的个人信息如下:')
            info = '''
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
                        ---------------------------
                    '''
            print(info % (bank[account]['username'], bank[account]['password'], account, bank[account]['country'],
                          bank[account]['province'], bank[account]['street'], bank[account]['gate'],
                          bank[account]['money'], bank_name))


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
            print('密码必须设置为6位！')
        else:
            if password.isdigit():
                password = int(password)
                break
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
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif data == 2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif data == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
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
            ---------------------------
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
                print('账号不存在！')
                saveMoney()
            else:
                print('存钱成功，您当前余额为', bank[account]['money'], '元！')
        else:
            print('金额输入错误，请重新输入！')
    else:
        print('账号格式输入错误，请重新输入！')
        saveMoney()


# 取钱
def getMoney():
    account = input('请输入您的账号：\n')
    if account.isdigit():
        account = int(account)
        pwd = input('请输入您的密码：\n')
        getMon = input('请输入您要提取的金额：￥')
        if getMon.isdigit():
            getMon = int(getMon)
            data = bank_getMoney(account, pwd, getMon)
            if data == 1:
                print('您输入的账号不存在！')
                getMoney()
            else:
                print(bank[account])
                if data == 2:
                    print('您输入的密码错误！')
                    getMoney()
                else:
                    if data == 3:
                        print('您的账号余额不足！')
                        getMoney()
                    else:
                        bank[account]['money'] = bank[account]['money'] - getMon
                        print('取钱成功，您的当前余额为', bank[account]['money'], '元！')
        else:
            print('金额输入错误，请重新输入！')
            getMoney()

    else:
        print('账号输入错误，请重新输入！')
        getMoney()


# 转账
def transferMoney():
    account = input('请输入您的账号：\n')
    if account.isdigit():
        account = int(account)
        account1 = input('请输入您的账号：\n')
        if account1.isdigit():
            account1 = int(account1)
            pwd = input('请输入您的密码：\n')
            transferMon = input('请输入您要转的金额：%\n')
            data = bank_transferMoney(account, account1, pwd, transferMon)
            if data == 1:
                print('您输入的账号不存在！')
                transferMoney()
            else:
                if data == 1:
                    print('您要转入的账号不存在！')
                    transferMoney()
                else:
                    if data == 2:
                        print('您输入的密码不正确！')
                        transferMoney()
                    else:
                        if data == 3:
                            print('您的账号余额不足！')
                            transferMoney()
                        else:
                            bank[account]['money'] = bank[account]['money'] - transferMon
                            bank[account1]['money'] = bank[account1]['money'] + transferMon
                            print('转账成功，您的账号当前余额为：', bank[account]['money'], '元！')
        else:
            print('您输入的要转入的账号格式错误！')
            transferMoney()
    else:
        print('您输入的账号格式错误！')
        transferMoney()


# 查询
def query():
    account = input('请输入您的账号：\n')
    if account.isdigit():
        account = int(account)
        pwd = input('请输入您的密码：\n')
        pwd = int(pwd)
        bank_query(account, pwd)
    else:
        print('账号格式输入错误！')
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
            print('您选择的业务不存在，请重新输入！')
    else:
        print('请输入数字！')
