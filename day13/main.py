# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 11:26
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : main.py
import time

from HTMLTestRunner import HTMLTestRunner  # 运行器
import unittest
from mail import send_email

# 1.加载所有用例

tests = unittest.defaultTestLoader.discover(r"D:\PycharmProjects\day13", pattern="testC*.py")

# 2.使用运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="这是一份计算器的测试报告",
    description="这只是运算的测试报告",
    verbosity=1,
    stream=open("calca.html", mode="w+", encoding="utf-8")
)

# 3.运行所有用例
runner.run(tests)
time.sleep(2)
# 4.实现邮件发送
send_email()
