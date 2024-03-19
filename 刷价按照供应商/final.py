# coding: utf-8
# @Project :project
# @File    :final.py
# @IDE     :PyCharm
# @Author  :孙崇博
# @Date    :2024/2/27 16:17

import openpyxl
import time
import pandas as pd

#截止时间
final_time = '2024/6/30'
# 获取当前日期
current_date = time.strftime("%Y-%m-%d", time.localtime())
#每次修改目录
read_file = 'F:/工作文件/4=刷价&采购协议价/24-3-18/采购协议价.xlsx'
#公司名称_AB
company_name_AB = []
#公司名称_C
company_name_C = [
'北京鸿基天翔发都商贸有限公司',
'北京鸿泽润华商贸有限公司',
'北京如骏领航商贸有限公司',
'北京益飞商贸有限公司',
'食速来（北京）供应链管理有限公司'
]
excel_file = pd.read_excel(read_file, sheet_name='商品数据')
for index, row in excel_file.iterrows():
    if row['*供应商/采购员名称'] != '杨烨昭':
        if row['*供应商/采购员名称'] not in company_name_C and row['*供应商/采购员名称'] not in company_name_AB:
            company_name_AB.append(row['*供应商/采购员名称'])

for i in range(len(company_name_AB)):
    workbook = openpyxl.load_workbook('F:/工作文件/4=刷价&采购协议价/程序处理/模版.xlsx')
    sheet = workbook['商品数据']
    sheet['B2'] = company_name_AB[i]
    sheet['B3'] = current_date
    sheet['D3'] = final_time  # 终止时间
    name = []
    unit = []
    price = []
    excel_file = pd.read_excel(read_file, sheet_name='商品数据')
    for index, row in excel_file.iterrows():
        if row['*供应商/采购员名称'] == company_name_AB[i] and row['最近一次进价'] != '下架' and row['最近一次进价'] != 0:
            name.append(row['*商品名称'])
            unit.append(row['*单位'])
            price.append(row['最近一次进价'])
    num = 5
    for j in range(len(name)):
        sheet['A'+str(num)] = name[j]
        sheet['D'+str(num)] = unit[j]
        sheet['G'+str(num)] = price[j]
        num += 1
    workbook.save('F:/工作文件/4=刷价&采购协议价/24-3-18/协议价/AB/' + company_name_AB[i] +'.xlsx')
print('AB类商品添加完成')

for i in range(len(company_name_C)):
    workbook = openpyxl.load_workbook('F:/工作文件/4=刷价&采购协议价/程序处理/模版.xlsx')
    sheet = workbook['商品数据']
    sheet['B2'] = company_name_C[i]
    sheet['B3'] = current_date
    sheet['D3'] = final_time
    name = []
    unit = []
    price = []
    excel_file = pd.read_excel(read_file, sheet_name='商品数据')
    for index, row in excel_file.iterrows():
        if row['*供应商/采购员名称'] == company_name_C[i] and row['最近一次进价'] != '下架' and row['最近一次进价'] != 0:
            name.append(row['*商品名称'])
            unit.append(row['*单位'])
            price.append(row['最近一次进价'])
    num = 5
    for j in range(len(name)):
        sheet['A' + str(num)] = name[j]
        sheet['D' + str(num)] = unit[j]
        sheet['G' + str(num)] = price[j]
        num += 1
    workbook.save('F:/工作文件/4=刷价&采购协议价/24-3-18/协议价/C/' + company_name_C[i] + '.xlsx')
print('C类商品添加完成')

# 杨烨昭 会被删掉；C类公司有5个；维护 C类公司名称、截止时间、文件目录