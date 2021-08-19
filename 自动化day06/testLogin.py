# -*- coding: utf-8 -*-
# @Time    : 2021/8/17 17:16
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : testLogin.py
import time
from unittest import TestCase
from appium import webdriver
from ddt import ddt
from ddt import data
from app.operationLogic import operationLogic
from caseData import useCaseData


@ddt
class TestLogin(TestCase):
    # 用例执行之前
    @data(*useCaseData.app_param)
    def setUp(self) -> None:
        server = "http://localhost:4723/wd/hub"  # Appium Server, 端口默认为4723
        platformName = data('platformName')  # 平台
        platformVersion = data('platformVersion')  # 平台版本，比如Android版本
        appPackage = data('appPackage')  # APP包名
        appActivity = data('appActivity')  # APP启动名，即Activity
        deviceName = data('deviceName')  # 设备名称或地址
        unicodeKeyboard = data('unicodeKeyboard')  # 这句和下面那句是避免中文问题的
        resetKeyboard = data('resetKeyboard')

        driver = webdriver.Remote(server)  # 连接手机和APP

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.close()
        self.driver.quit()

    # 执行成功用例
    @data(*useCaseData.login_success_data)
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
        actualResult = login.get_success()

        # 断言
        self.assertEqual(desiredResult, actualResult)

    # 执行失败用例
    @data(*useCaseData.login_failure_data)
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
        actualResult = login.get_failure()
        now = time.strftime('%M/%S')
        self.driver.save_screenshot('登录失败' + now + '.jpg')
        # 断言
        self.assertEqual(desiredResult, actualResult)
