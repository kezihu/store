# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 15:25
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : douyin.py
# 自动刷抖音
import time
from appium import webdriver

server = "http://localhost:4723/wd/hub"  # Appium Server, 端口默认为4723
param = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "deviceName": "127.0.0.1∶62001"
}

driver = webdriver.Remote(server, param)  # 连接手机和APP


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


x, y = get_size()
time.sleep(6)

while 1:
    if '没有更多' in driver.page_source:
        break
    else:
        driver.swipe(x * 0.5, y * 0.9, x * 0.5, y * 0.2)
        time.sleep(1)
