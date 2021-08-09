# -*- coding: utf-8 -*-
# @Time    : 2021/8/4 16:07
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : addUser.py
import random
from DBUtils import addUser
from citizenInt import *


# 注册公民信息
def add_citizen():
    cit = citizen()
    li = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w",
          "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
          "T",
          "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    cardID = ''
    for i in range(32):
        index = random.randint(0, len(li) - 1)
        cardID += li[index]
    cit.setcardID(cardID)

    name = input('请输入姓名：\n')
    cit.setname(name)

    sex = input('请输入性别：\n')
    cit.setsex(cit)

    age = input('请输入年龄：\n')
    while True:
        if age.isdigit():
            age = int(age)
            cit.setage(age)
            break
        else:
            print('请输入数字！')

    while True:
        password = input('请输入密码：\n')
        if 6 <= len(password) <= 12:
            cit.setpassword(password)
            break
        else:
            print('密码需要大于6位且小于12位！')

    status = True
    cit.setstatus(status)

    country = input('请输入国家：\n')
    cit.setcountry(country)

    while True:
        province = input('请输入省份：\n')
        sql = "SELECT pid FROM province WHERE pname LIKE '%%s%'"
        data = [province]
        model = 'one'
        num = select(sql, data, model, [])
        if num is None:
            print('您输入的省份不存在！')
        else:
            cit.setprovince(num)
            break

    street = input('请输入街道：\n')
    cit.setstreet(street)

    door = input('请输入门牌号：\n')
    cit.setdoor(door)

    registDate = time.strftime('%Y-%m-%d')
    cit.setregistDate(registDate)

    immiDate = None

    cit.setimmiDate(immiDate)

    credit = 2
    cit.setcredit(credit)

    education = 0
    cit.seteducation(education)

    studies = 0
    cit.setstudies(studies)

    print("注册！以下是您的个人注册信息：")
    info = '''\033[35;1m
        -----------------个人信息-----------------
            身份证号码：%s
            姓名：%s
            性别：%s
            年龄：%s
            密码：%s
            状态：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号: %s
            注册日期：%s
            申请移民日期：%s
            信誉程度：%s
            文化程度：%s
            学习次数：%s
        -----------------------------------------\033[35;0m
    '''
    print(info % (
    cardID, name, sex, age, password, status, country, province, street, door, registDate, immiDate, credit, education,
    studies))
    sql = 'insert into citizen values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    data = [cardID, name, sex, age, password, status, country, province, street, door, registDate, immiDate, credit,
            education, studies]
    addUser(sql, data)
