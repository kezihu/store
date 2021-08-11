# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 9:53
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : HKR同学注册.py
from selenium import webdriver
import time

# 创建谷歌驱动
driver = webdriver.Chrome()
# 网页地址
driver.get('http://localhost:8080/HKR')
# 窗口最大化
driver.maximize_window()
# 点击新来的童鞋来这里注册一下哦
driver.find_element_by_link_text('新来的童鞋来这里注册一下哦').click()
# 系统登录名
driver.find_element_by_id('loginname').send_keys('Kevin')
# 真实姓名
driver.find_element_by_name('username').send_keys('克子')
# 密码
driver.find_element_by_id('pwd').send_keys('123456')
# 确认密码
driver.find_element_by_name('reloginpass').send_keys('123456')
# 下一步
driver.find_element_by_name('next').click()
# 年龄
driver.find_element_by_name('age').send_keys('22')
# 性别
driver.find_element_by_name('sex').send_keys('男')
# 学习内容
driver.find_element_by_id('classname').send_keys('Python自动化')
time.sleep(2)
# 上一步
# driver.find_element_by_xpath('//*[@id="msform"]/fieldset[2]/input[2]').click()
# driver.find_element_by_name('previous').click()
# 下一步
driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()
# driver.find_element_by_name('next').click()
# 邮箱
driver.find_element_by_id('reg_mail').send_keys('8728109@qq.com')
# 电话号码
driver.find_element_by_id('reg_phone').send_keys('15227067110')
# 居住地址
driver.find_element_by_name('address').send_keys('北京')
time.sleep(3)
# 上一步
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[3]/input[3]").click()
# driver.find_element_by_class_name('previous action-button').click()
# driver.find_element_by_name('previous').click()
# 注册
driver.find_element_by_id('btn_reg').click()
time.sleep(2)
# 注册失败点击弹窗确定
# driver.find_element_by_class_name('l-btn-text').click()
# driver.find_element_by_xpath('/html/body/div[2]/div[3]/a/span/span').click()
# 注册成功点击弹窗确定
driver.find_element_by_class_name('l-btn-text').click()
# driver.find_element_by_xpath('/html/body/div[2]/div[3]/a/span/span').click()
# 关闭浏览器
driver.close()
driver.quit()
