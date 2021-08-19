# -*- coding: utf-8 -*-
# @Time    : 2021/8/17 15:32
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : caseData.py
class useCaseData:
    # 五大参数
    app_param = [
        {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
            "deviceName": "127.0.0.1∶62001",
            "noReset": "True",
            "unicodeKeyboard": "True",
            "resetKeyboard": "True"
        }
    ]
    # 登录数据
    login_success_data = [
        {
            "username": "15227067110", "password": "k885213.", "desiredResult": ""
        }
    ]
    login_failure_data = [
        {
            "username": "15227067110", "password": "123456", "desiredResult": ""
        }
    ]
