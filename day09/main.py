# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 12:41
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : main.py
from creatTable import creat_mysql_table
from db_to_excel import mysql_to_excel
from excel_to_db import excel_to_mysql

creat_mysql_table()
excel_to_mysql()
mysql_to_excel()
