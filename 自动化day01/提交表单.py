# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 13:45
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : 提交表单.py
from selenium import webdriver
import time

# 创建谷歌驱动
driver = webdriver.Chrome()
# 网页地址
driver.get(r'D:\PycharmProjects\automate\day01\autotest.html')
# 窗口最大化
driver.maximize_window()
# 定位username
driver.find_element_by_id('accountID').send_keys('Kevin')
# 定位password
driver.find_element_by_id('passwordID').send_keys('123456')
# 定位地区
driver.find_element_by_id('areaID').send_keys('北京市')
# 定位性别
driver.find_element_by_id('sexID1').click()
# 定位四季
driver.find_element_by_xpath("//*[@name='u3' and @value='summer']").click()
driver.find_element_by_xpath("//*[@name='u3' and @value='winter']").click()
# 选择文件
driver.find_element_by_name('file').send_keys(r'C:\Users\20382\Pictures\Saved Pictures\虎头.png')
# 提交
driver.find_element_by_class_name('u16').click()
time.sleep(3)
# 关闭浏览器
driver.close()
driver.quit()
