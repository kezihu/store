# -*- coding: utf-8 -*-
# @Time    : 2021/8/17 15:41
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : operationLogic.py
import time


class operationLogic:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        # 手机号
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/gle').send_keys('15227067110')
        # 密码
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/gim').send_keys('k885213.')
        # 同意条款
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/h49').click()
        # 登录
        time.sleep(2)
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/bua').click()

    def get_success(self):
        return self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/iwj').text

    def get_failure(self):
        return self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/cdw').text
