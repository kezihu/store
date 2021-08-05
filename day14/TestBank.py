# -*- coding: utf-8 -*-
# @Time    : 2021/8/5 14:34
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : TestBank.py
from unittest import TestCase
from ddt import ddt, data, unpack
from Bank_ICBC import Bank

# 测试开户的数据
add = [
    [4, 3, 123456, 3, 3, 3, 3, 1000, None]
    # account, username, password, country, province, street, gate, money, registdate
]

# 测试存钱的数据
save = [
    [4, 100]  # account, money
]

# 测试取钱的数据
get = [
    [3, 123456, 100]  # account, pwd, money
]

# 测试查询的数据
query = [
    [3, 123456]  # account, pwd
]

# 测试转账的数据
transfer = [
    [1, 2, 1, 100]  # account, account1, pwd, transferMon
]


@ddt
class TestBank(TestCase):
    # 测试开户
    @data(*add)
    @unpack
    def testaddUser(self, account, username, password, country, province, street, gate, money, registdate):
        bank = Bank()
        bank.bank_addUser(account, username, password, country, province, street, gate, money, registdate)

    # 测试存钱
    @data(*save)
    @unpack
    def testsaveMoney(self, account, money):
        bank = Bank()
        bank.bank_saveMoney(account, money)

    # 测试取钱
    @data(*get)
    @unpack
    def testgetMoney(self, account, pwd, money):
        bank = Bank()
        bank.bank_getMoney(account, pwd, money)

    # 测试查询
    @data(*query)
    @unpack
    def testquery(self, account, pwd):
        bank = Bank()
        bank.bank_query(account, pwd)

    @data(*transfer)
    @unpack
    def testtransferMoney(self, account, account1, pwd, transferMon):
        bank = Bank()
        bank.bank_transferMoney(account, account1, pwd, transferMon)
