# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 11:41
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : useCaseData.py
class useCaseData:
    # 成功登录的数据
    success_data = [
        {'username': 'qiaoyueyang', 'password': 'admin', 'desiredResult': 'Teacher manager'},
        {'username': 'caoshiming', 'password': 'admin', 'desiredResult': 'Teacher manager'},
        {'username': 'jason', 'password': 'admin', 'desiredResult': 'Teacher manager'},
        {'username': 'chenyongjie', 'password': 'root', 'desiredResult': 'Teacher manager'}
    ]
    # 失败登录的数据
    failure_data = [
        {'username': 'qiaoyueyang', 'password': 'admin1', 'desiredResult': '账户名错误或密码错误!别瞎弄!'},
        {'username': '', 'password': 'admin1', 'desiredResult': '登录名或手机不能为空!别瞎弄!'},
        {'username': 'jason', 'password': '', 'desiredResult': '√'},
        {'username': 'chenyongjie1', 'password': 'root1', 'desiredResult': '账户名错误或密码错误!别瞎弄!'}
    ]
