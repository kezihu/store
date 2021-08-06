# -*- coding: utf-8 -*-
# @Time    : 2021/7/23 19:11
# @Author  : Kevin_liu
# @Email   : 87281094@xxx.com
# @File    : demo.py
"""
任务：
    每个月的销售总金额：
    全年的销售总额：
    每种衣服的销售总额：
    每个季度销售总额占比：
    全年每种销售数量占比：
"""
import xlrd

month_sales = []
clothes = {}
wb = xlrd.open_workbook("2020年每个月的销售情况.xlsx", encoding_override=True)  # 打开工作簿


def sales(month):
    st = wb.sheet_by_name(month)  # 打开您要操作的选项卡
    rows = st.nrows  # 获取行数
    sale = 0
    for i in range(1, rows):  # 遍历所有行数据
        data = st.row_values(i)
        sale = sale + (data[2] * data[4])
    month_sales.append(round(sale, 2))
    print(month, "销售总额为：", round(sale, 2))


# # 每种衣服的销售总额
# def quarter(month):
#     st = wd.sheet_by_name(month)  # 打开您要操作的选项卡
#     rows = st.nrows  # 获取行数
#     for i in range(1, rows):  # 遍历所有行数据
#         name = st.cell_value(i, 1)  # 服装名字
#         price = float(st.cell_value(i, 2))  # 服装价格
#         count = int(st.cell_value(i, 4))  # 服装数量
#         if name in clothes:
#             clothes[name]['count'] = clothes[name]['count'] + count
#         else:
#             clothes[name] = {
#                 'price': price,
#                 'count': count
#             }
#         data = sale_total(name, price , count)
#         total = clothes[name]['price'] * clothes[name]['count']
#         print(clothes[name], '的销售总额为：', total, '元。')

mon = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
for month in mon:
    sales(month)
    # quarter(month)
print("-".center(30, "-"))
print('全年的销售总额为：', round(sum(month_sales), 2))
print("-".center(30, "-"))
