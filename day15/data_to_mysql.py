# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:10
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : data_to_mysql.py
import pymysql

host = 'localhost'
user = 'root'
password = '123456'
database = '用户数据'

con = pymysql.connect(host=host, user=user, password=password, database=database)
cur = con.cursor()

file = (open('用户数据.txt', 'r+', encoding='utf-8')).readlines()
rows = len((open('用户数据.txt', 'r+', encoding='utf-8')).readlines())  # 获取行数
sum = 0
for i in range(rows):
    sql = 'INSERT INTO user VALUES (%s,%s,%s)'
    part = file[i].split(",", 2)  # 按，分割
    data = [part[0], part[1], part[2]]
    cur.execute(sql, data)
    count = int(part[2])
    sum += count
print(sum)
print('录入完成！')
con.commit()
cur.close()
con.close()
