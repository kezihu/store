# -*- coding: utf-8 -*-
# @Time    : 2021/8/5 15:30
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : Bank_ICBC.py
import pymysql

con = pymysql.connect(host='localhost', user='root', password='123456', database='bank')
cur = con.cursor()
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称


class Bank:
    # 银行开户
    def bank_addUser(self, account, username, password, country, province, street, gate, money, registdate):
        # 1.判断数据库是否已满
        cur.execute("SELECT * from user")
        record = cur.fetchall()
        if len(record) >= 100:
            return 3
        else:
            # 2.判断用户是否存在
            cur.execute("SELECT * from user where account = %s" % account)
            record1 = cur.fetchone()
            if record1 is not None:
                return 2
            else:
                # 3.正常开户
                sql = "insert into  user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                a = [account, username, password, country, province, street, gate, money, bank_name, registdate]
                cur.execute(sql, a)
                con.commit()
                return 1

    # 银行的存钱逻辑
    def bank_saveMoney(self, account, saveMon):
        cur.execute("SELECT account FROM `user` where account = %s " % account)
        record = cur.fetchone()
        if record is None:
            return False
        else:
            sql = 'UPDATE `user` SET money = money + %s WHERE account = %s'
            a = [saveMon, account]
            cur.execute(sql, a)
            con.commit()

    # 银行的取钱逻辑
    def bank_getMoney(self, account, pwd, getMon):
        cur.execute("SELECT * FROM `user` where account = %s" % account)
        record = cur.fetchone()
        if record is None:
            return 1
        if record[2] != pwd:
            return 2
        if record[7] < getMon:
            return 3

    # 银行的转账逻辑
    def bank_transferMoney(self, account, account1, pwd, transferMon):
        cur.execute("SELECT * FROM `user` where account = %s" % account)
        record = cur.fetchone()
        if record is None:
            return 1
        cur.execute("SELECT * FROM `user` where account = %s" % account1)
        record = cur.fetchone()
        if record is None:
            return 1
        if record[2] != pwd:
            return 2
        if record[7] < transferMon:
            return 3

    # 银行的查询逻辑
    def bank_query(self, account, pwd):
        cur.execute("SELECT * FROM `user` where account = %s" % account)
        record = cur.fetchone()
        if record is None:
            print('\033[33;1m您输入的账号不存在！\033[0m')
        else:
            if record[2] != pwd:
                print('\033[33;1m您输入的密码不正确！\033[0m')
            else:
                print('查询成功，您的个人信息如下:')
                info = '''\033[35;1m
                            ----------个人信息----------
                            用户名：%s
                            密码：%s
                            账号：%s
                            地址信息
                                国家：%s
                                省份：%s
                                街道：%s
                                门牌号: %s
                            余额：%s
                            开户行地址：%s
                            注册日期：%s
                            ---------------------------\033[35;0m
                        '''
                print(info % (
                    record[1], record[2], record[0], record[3], record[4], record[5], record[6], record[7], record[8],
                    record[9]))

