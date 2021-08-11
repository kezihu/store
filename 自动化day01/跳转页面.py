# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 13:37
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : 跳转页面.py
from selenium import webdriver
import time

# 创建谷歌驱动
driver = webdriver.Chrome()
# 网页地址
driver.get(r'D:\PycharmProjects\automate\day01\pop.html')
# 窗口最大化
driver.maximize_window()
# 定位输入框
driver.find_element_by_id('goo').click()
time.sleep(3)
# 关闭浏览器
driver.close()
driver.quit()
