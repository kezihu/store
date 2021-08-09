# -*- coding: utf-8 -*-
# @Time    : 2021/8/4 15:08
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : DBUtils.py
import pymysql

host = 'localhost'
user = 'root'
password = '123456'
database = 'psb'


# 添加公民
def addUser(sql, data):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, data)
    con.commit()
    cur.close()
    con.close()


# 删除信息
def delete(sql, data):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, data)
    con.commit()
    cur.close()
    con.close()


# 修改信息
def update(sql, data):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, data)
    con.commit()
    cur.close()
    con.close()


# 查询公民信息
def select(sql, data, model, size):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, data)
    if model == "all":
        return cur.fetchall()
    elif model == "one":
        return cur.fetchone()
    elif model == "many":
        return cur.fetchmany(size)
    con.commit()
    cur.close()
    con.close()
