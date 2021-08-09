# -*- coding: utf-8 -*-
# @Time    : 2021/8/5 11:37
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : main.py
from immigration import pub_sec_per
from learn import ordinaryCitizen
from management import *


def welcome():
    print('\033[31;5m-----------------------------------------\033[31;0m')
    print('\033[31;5m-\t\t  公安局人员管理系统V1.2版本  \t\t-\033[31;0m')
    print('\033[31;5m-----------------------------------------\033[31;0m')


welcome()
while True:
    operation = input('请选择您的身份(1.国家安全总局人员  2.地区公安局人员  3.普通公民):\n')
    if operation.isdigit():
        operation = int(operation)
        if operation == 1:
            nationalStaff()
        elif operation == 2:
            pub_sec_per()
        elif operation == 3:
            ordinaryCitizen()
        else:
            print('\033[36;5m您选择的身份不存在！\033[36;0m')
    else:
        print('\033[36;5m输入非法！\033[36;5m')
