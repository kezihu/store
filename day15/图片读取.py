# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:47
# @Author  : Kevin_liu
# @Email   : 87281094@qq.com
# @File    : 图片读取.py
path = input('请输入图片的路径：\n')
picture = (open(file=path, mode="rb")).read()
photo = (open(file="picture.jpg", mode="wb")).write(picture)
