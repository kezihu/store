# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 13:21
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : 淘宝.py
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver import ActionChains
import time

# 打开谷歌浏览器
chromeDriver = webdriver.Chrome()

# 打开京东网址
chromeDriver.get("https://www.taobao.com/")

# 窗口最大化
chromeDriver.maximize_window()

# 点击登录按钮
chromeDriver.find_element_by_link_text('登录').click()

# 切换窗口
data = chromeDriver.window_handles
chromeDriver.switch_to.window(data[1])

# 用户名
chromeDriver.find_element_by_id('fm-login-id').send_keys('帅气潇洒的孩子')

# 密码
chromeDriver.find_element_by_id('fm-login-password').send_keys('k885213.')

# 滑动验证
time.sleep(5)
ac = ActionChains(chromeDriver)
slider = chromeDriver.find_element_by_xpath("//*[@id='nc_2_n1z' and @class='nc_iconfont btn_slide']")  # 定位滑块
# slider = chromeDriver.find_element_by_id('nc_2_n1z')  # 定位滑块
ac.click_and_hold(slider).move_by_offset(300, 0).perform()
# for i in range(320):
#     try:
#         ac.drag_and_drop_by_offset(slider, 300, 0).perform()  # 平行移动鼠标，此处直接设一个超出范围的值，这样拉到头后会报错从而结束这个动作
#     except UnexpectedAlertPresentException:
#         break
#
#     time.sleep(11)  # 等待停顿时间
# 点击登录
# time.sleep(2)
chromeDriver.find_element_by_class_name('fm-button fm-submit password-login').click()

# 输入框搜索
chromeDriver.find_element_by_id('q').send_keys('iphone12')

# 点击搜索
chromeDriver.find_element_by_link_text('搜索').click()

# 关闭服务
chromeDriver.close()

# 关闭浏览器
chromeDriver.quit()
