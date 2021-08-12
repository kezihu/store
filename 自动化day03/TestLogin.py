# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 14:18
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : TestLogin.py
from selenium import webdriver
from unittest import TestCase
from ddt import ddt
from ddt import data
import time
from operationLogic import operationLogic
from useCaseData import *


@ddt
class TestLogin(TestCase):
    # 用例执行之前
    def setUp(self) -> None:
        # 创建谷歌驱动
        self.driver = webdriver.Chrome()

        # 网页地址
        self.driver.get('http://localhost:8080/HKR/admin_jsps/login.jsp')

        # 窗口最大化
        self.driver.maximize_window()
        time.sleep(2)

    # 用例执行完之后，关闭浏览器
    def tearDown(self) -> None:
        time.sleep(1)

        # 关闭服务
        self.driver.close()

        # 关闭浏览器
        self.driver.quit()

    # 执行成功用例
    @data(*useCaseData.success_data)
    def testLoginsuccess(self, testdata):
        # 提取用户名
        username = testdata["username"]
        # 提取密码
        password = testdata["password"]
        # 提取期望结果
        desiredResult = testdata["desiredResult"]

        login = operationLogic(self.driver)
        login.login(username, password)

        # 获取实际结果
        actualResult = login.get_succes_data()

        # 断言
        self.assertEqual(desiredResult, actualResult)

    # 执行失败用例
    @data(*useCaseData.failure_data)
    def testLoginfailure(self, testdata):
        # 提取用户名
        username = testdata["username"]
        # 提取密码
        password = testdata["password"]
        # 提取期望结果
        desiredResult = testdata["desiredResult"]

        login = operationLogic(self.driver)
        login.login(username, password)
        # 获取实际结果
        actualResult = login.get_failure_data()
        now = time.strftime('%M/%S')
        self.driver.save_screenshot('登录失败'+now+'.png')
        # 断言
        self.assertEqual(desiredResult, actualResult)
