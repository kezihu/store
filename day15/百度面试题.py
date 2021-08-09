# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 17:08
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : 百度面试题.py
file = (open('baidu_x_system.log', 'r+', encoding='utf-8')).readlines()
rows = len((open('baidu_x_system.log', 'r+', encoding='utf-8')).readlines())

list = {}
count = 1
for i in range(rows):
    part = file[i].split(' ', 1)
    if part[0] in list:
        list[part[0]]['count'] = list[part[0]]['count'] + 1
        list[part[0]] = {
            'count': list[part[0]]['count']
        }

    else:
        list[part[0]] = {
            'count': count
        }
print(list)

