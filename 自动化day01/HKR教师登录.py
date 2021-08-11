# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 10:22
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : HKR教师登录.py
from selenium import webdriver
import time

# 创建谷歌驱动
driver = webdriver.Chrome()
# 网页地址
driver.get('http://localhost:8080/HKR')
# 窗口最大化
driver.maximize_window()
# 点击教师登录
time.sleep(2)
driver.find_element_by_link_text('教师登录').click()
# 教师登录名/手机
driver.find_element_by_id('loginname').send_keys('jason')
# 请输入密码
driver.find_element_by_id('password').send_keys('admin')
# 登录
driver.find_element_by_id('submit').click()
# 左侧教师管理
driver.find_element_by_id('_easyui_tree_11').click()
# 搜索框
time.sleep(2)
driver.find_element_by_id('sear_teaname').send_keys('曹士明')
# 点击搜索
time.sleep(2)
driver.find_element_by_xpath("//*[@id='search_user']/span/span[1]").click()
# 左侧学生管理
time.sleep(3)
driver.find_element_by_xpath("//*[@id='_easyui_tree_12']/span[4]/a").click()
# 关闭浏览器
driver.close()
driver.quit()
