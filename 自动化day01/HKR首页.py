# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 17:38
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : HKR首页.py
from selenium import webdriver
import time

# 创建谷歌驱动
driver = webdriver.Chrome()
# 网页地址
driver.get('http://localhost:8080/HKR')
# 窗口最大化
driver.maximize_window()
# 用户名
driver.find_element_by_id('loginname').send_keys('root')
# 密码
driver.find_element_by_id('password').send_keys('root')
# time.sleep(1)
# 确定
driver.find_element_by_id('submit').click()
time.sleep(1)
# 培训时间
driver.find_element_by_class_name('show_tea').send_keys('9（上晚自习）')
# 授课讲师
driver.find_element_by_xpath('//*[@id="tea_td"]/select').send_keys('贾生')
# 本次学习都理解了么？
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[5]/td[3]/div/label[2]/div').click()
# 对工作帮助大么？
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[6]/td[2]/div/label[2]/div").click()
# 符合实际企业需要
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[7]/td[3]/div/label[3]/div").click()
# 语言、思路清晰明确
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[8]/td[2]/div/label[1]/div").click()
# 针对性、系统性强
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[9]/td[2]/div/label[2]/div").click()
# 以后有机会还愿意来学么？
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[10]/td[3]/div/label[4]/div").click()
# 本次学习还满意吗？
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[11]/td[2]/div/label[2]/div").click()
# 达到学习目的了么？
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[12]/td[2]/div/label[2]/div").click()
# 您宝贵的建议是我们进步的阶梯！
driver.find_element_by_id('textarea').send_keys('hello world!')
# 提交今日评价
driver.find_element_by_id('subtn').click()
time.sleep(1)
# 重复提交的确定
driver.find_element_by_class_name('l-btn-text').click()
time.sleep(3)
# 关闭浏览器
driver.close()
driver.quit()
