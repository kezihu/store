# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 12:48
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : 京东.py
from selenium import webdriver
import time

# 打开谷歌浏览器
chromeDriver = webdriver.Chrome()

# 打开京东网址
chromeDriver.get("https://www.jd.com/")

# 窗口最大化
chromeDriver.maximize_window()

# 点击登录按钮
chromeDriver.find_element_by_link_text("登录").click()

# 进行登录
chromeDriver.find_element_by_link_text("账户登录").click()
chromeDriver.find_element_by_id("loginname").send_keys("Kevin__ke")
chromeDriver.find_element_by_id("nloginpwd").send_keys("k885213.")
chromeDriver.find_element_by_id("loginsubmit").click()
time.sleep(5)

# 搜索iPhone12
chromeDriver.find_element_by_id("key").send_keys("iPhone12")
chromeDriver.find_element_by_class_name("button").click()

# 滑动验证
# ac = ActionChains(chromeDriver)
# ac.click_and_hold(chromeDriver.find_element_by_class_name("JDJRV-slide-inner JDJRV-slide-btn")).move_by_offset().perform()

# 选择一个商品
time.sleep(5)
chromeDriver.find_element_by_class_name("p-img").click()

# 切换窗口
data = chromeDriver.window_handles
chromeDriver.switch_to.window(data[1])

# 加入购物车
chromeDriver.find_element_by_id("InitCartUrl").click()

# 查看我的购物车
chromeDriver.find_element_by_link_text('我的购物车').click()

# 切换窗口
data = chromeDriver.window_handles
chromeDriver.switch_to.window(data[2])

# 去结算
chromeDriver.find_element_by_link_text('去结算').click()
# 提交订单
time.sleep(5)
chromeDriver.find_element_by_id('order-submit').click()
# chromeDriver.find_element_by_link_text('提交订单').click()

# 关闭服务
chromeDriver.close()

# 关闭浏览器
time.sleep(3)
chromeDriver.quit()
