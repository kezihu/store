# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 9:47
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : HKR所有好友和退出系统.py
from selenium import webdriver
import time

# 创建谷歌驱动
driver = webdriver.Chrome()
# 网页地址
driver.get('http://localhost:8080/HKR')
# 窗口最大化
driver.maximize_window()
# 用户名
driver.find_element_by_id('loginname').send_keys('aaaaa')
# 密码
driver.find_element_by_id('password').send_keys('aaaaa')
time.sleep(1)
# 确定
driver.find_element_by_id('submit').click()
# 点击左侧所有好友
driver.find_element_by_xpath("//*[@id='_easyui_tree_10']/span[4]/a").click()
# 退出系统
time.sleep(2)
driver.find_element_by_xpath("//*[@id='top']/div/a[2]/img").click()
# 关闭浏览器
driver.close()
driver.quit()
