# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 12:48
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : 苏宁易购.py
from selenium import webdriver
import time

# 创建谷歌浏览器对象
chromeDriver = webdriver.Chrome()

# 打开网址
chromeDriver.get("https://www.suning.com/")

# 窗口最大化
chromeDriver.maximize_window()
time.sleep(2)

# # 点击登录按钮
# chromeDriver.find_element_by_link_text('登录').click()
#
# # 点击账户登录
# chromeDriver.find_element_by_link_text('账户登录').click()
#
# # 用户名
# chromeDriver.find_element_by_id('userName').send_keys('Kevin_ke')
#
# # 密码
# chromeDriver.find_element_by_id('password').send_keys('k885213.')
# # 点击按钮进行验证
# time.sleep(3)
# chromeDriver.find_element_by_id('iar1_sncaptcha_button').click()
# # 点击登录
# chromeDriver.find_element_by_id('submit').click()

# 寻找搜索输入框
chromeDriver.find_element_by_id("searchKeywords").send_keys("iPhone12")
# 点击搜索
chromeDriver.find_element_by_id("searchSubmit").click()

# 选择一个商品
time.sleep(3)
# chromeDriver.find_element_by_name('ssdsn_search_pro_name02-1_0_0_12156210854_0070094634').click()
chromeDriver.find_element_by_xpath("//*[@id='0070094634-12156210854']/div/div/div[2]/div[2]/a").click()

# 切换窗口
data = chromeDriver.window_handles
chromeDriver.switch_to.window(data[1])

# 添加购物车
chromeDriver.find_element_by_id("addCart").click()
time.sleep(3)
# 去购物车结算
chromeDriver.find_element_by_name('cart1_go').click()
# chromeDriver.find_element_by_xpath("/html/body/div[38]/div/div[2]/div/div[1]/a").click()
# 去结算
chromeDriver.find_element_by_name('icart1_ope_buy01').click()
time.sleep(3)
# 关闭服务
chromeDriver.close()

# 退出浏览器
chromeDriver.quit()
