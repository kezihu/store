# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 14:45
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : main.py
from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="TestLogin.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="HKR教师登录的测试报告",
    description="成功用例和失败用例",
    verbosity=1,
    stream=open(file="TestingReport.html", mode="w+", encoding="utf-8")
)

runner.run(tests)
