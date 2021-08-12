# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 14:13
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : operationLogic.py
import time


class operationLogic:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        # 教师登录名/手机
        self.driver.find_element_by_id('loginname').send_keys(username)

        # 请输入密码
        self.driver.find_element_by_id('password').send_keys(password)

        # 登录
        time.sleep(1)
        self.driver.find_element_by_id('submit').click()

    def get_succes_data(self):
        return self.driver.title

    def get_failure_data(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text
