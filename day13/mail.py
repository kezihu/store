# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 11:45
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : mail.py
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr


def send_email():
    sender = '87281094@qq.com'  # 发件人邮箱账号
    my_pass = 'ynmxmovzjljebgei'  # 发件人邮箱授权码
    user = '87281094@qq.com'  # 收件人邮箱账号

    msg = MIMEMultipart()  # 创建一个邮件
    msg['From'] = formataddr(["", sender])  # 括号里对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(["", user])  # 括号里对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = "发送邮件测试"  # 邮件的主题，也可以说是标题

    server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，SMTP端口是25
    server.login(sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码

    att = MIMEApplication(open('计算器.html', 'rb').read(), 'base64')  # 构造附件，三个参数：第一个为附件路径，第二个附件格式，第三个附件设置编码utf-8
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = "attachment; filename='test.html'"  # filename为文件名字
    msg.attach(att)
    try:
        server.sendmail(sender, user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("邮件发送失败")
