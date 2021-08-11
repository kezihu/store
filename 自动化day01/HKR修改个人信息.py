# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 9:18
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : HKR修改个人信息.py
from selenium import webdriver
import time

# 创建谷歌驱动
driver = webdriver.Chrome()
# 网页地址
driver.get('http://localhost:8080/HKR')
# 窗口最大化
driver.maximize_window()
# 用户名
driver.find_element_by_id('loginname').send_keys('admin4')
# 密码
driver.find_element_by_id('password').send_keys('root')
# time.sleep(1)
# 确定
driver.find_element_by_id('submit').click()
time.sleep(1)
# 修改个人信息界面
driver.find_element_by_xpath("//*[@id='_easyui_tree_8']/span[4]/a").click()
# 登录名
# driver.find_element_by_name('loginname').clear()
driver.find_element_by_name('loginname').send_keys('')
# 登录密码
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('123456')
# 年龄
driver.find_element_by_id('_easyui_textbox_input1').clear()
driver.find_element_by_id('_easyui_textbox_input1').send_keys('66')
# 性别
driver.find_element_by_name('sex').send_keys('女')
# 居住地址
driver.find_element_by_name('address').clear()
driver.find_element_by_name('address').send_keys('上海')
# 邮箱
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('87281094@qq.com')
# 个人名片
driver.find_element_by_name('carte').clear()
driver.find_element_by_name('carte').send_keys('你好啊!')
# 修改按钮
driver.find_element_by_id('btn_modify').click()
# 关闭浏览器
time.sleep(3)
driver.close()
driver.quit()
