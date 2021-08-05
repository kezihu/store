# -*- coding: utf-8 -*-
# @Time    : 2021/8/5 15:18
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : main.py
from HTMLTestRunner import HTMLTestRunner
import unittest

# 加载所有用例
tests = unittest.defaultTestLoader.discover(r"D:\PycharmProjects\day14", pattern="TestBank.py")

# 使用运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="这是一份银行系统的测试报告",
    description="这是银行开户、存钱、取钱、查询、转账的测试报告",
    verbosity=1,
    stream=open("bank.html", mode="w+", encoding="utf-8")
)

# 运行所有用例
runner.run(tests)
