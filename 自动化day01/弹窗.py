# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 14:21
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : 弹窗.py
from selenium import webdriver
import time

# 创建谷歌驱动
driver = webdriver.Chrome()
# 网页地址
driver.get(r'D:\PycharmProjects\automate\day01\dialogs.html')
# 窗口最大化
driver.maximize_window()
# 定位输入框
# driver.find_element_by_id('alert').click()
driver.find_element_by_id('confirm').click()

time.sleep(2)
# 点击确定，关闭弹窗
driver.switch_to.alert.accept()  # 确定
# driver.switch_to.alert.dismiss()  # 取消
time.sleep(3)
# 关闭浏览器
driver.close()
driver.quit()
