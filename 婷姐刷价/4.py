from tkinter import Tk, Button, Label, filedialog
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import mysql.connector
import os
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
import time
from sqlalchemy import create_engine

# 连接到MySQL数据库
mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="123456",
  database="list"
)

my_cursor = mydb.cursor()

# 创建主窗口
root = Tk()
root.withdraw()
#选择文件的上传路径
file_path = filedialog.askopenfilename()

foreign_id = [] #foreign_id
name_ping = [] #商品名称_平台
sort1 = []  #一级分类
sort2 = []  #二级分类
types = [] #类型
unit = [] #单位
provider = [] #供应商
clas = [] #品类
price_source = [] #源头采购价
price_buy = []#平台进货价
price_special = []#特殊商品价格
price_AB =[] #AB类售价
price_C0 = [] #C0售价
in_price_C4 = [] #C4进货价
in_price_C1 = [] #C1进货价
in_price_C2 = [] #C2进货价
in_price_C3 = [] #C3进货价

rate_sort1 = [] #rate_一级分类
rate_sort2 = [] #rate_二级分类
rate_provider = [] #供应商
rate_class = [] #品类
rate = [] #rate

add_foreign_id = [] #新增商品id
add_name_ping = [] #新增商品平台名称
add_sort1 = []#新增商品一级分类
add_sort2 = []#新增商品二级分类
add_types = []#新增商品类型
add_unit = []#新增商品单位
add_provider = []#新增商品供应商
add_clas = []#新增商品品类
add_price_source = []#新增商品源头采购价
add_price_buy = []#新增商品平台进货价
add_price = []#新增商品售价

name_same = [] #校验 商品名称
name_same_mid = [] #校验 商品名称中间列
price_same = []#校验 商品价格
price_same_mid = []#校验 商品价格
price_common_mid = 0 #校验 普通品质的商品的价格
price_high_mid = 0 #校验 优质品质的商品的价格
price_Boutique_mid = 0 #校验 精品品质的商品的价格

################################################################################################################
print('1.上传模版刷价加品  2.导出商品及价格  0.退出')
while True:
  index = input('请输入选项：')
  if index == '1':
    try:
      df1 = pd.read_excel(open(file_path, 'rb'), sheet_name='商品价格', dtype=str)
      df1 = df1.astype(object).where(pd.notnull(df1), None)
      df2 = pd.read_excel(open(file_path, 'rb'), sheet_name='加价率', dtype=str)
      df2 = df2.astype(object).where(pd.notnull(df2), None)
      df3 = pd.read_excel(open(file_path, 'rb'), sheet_name='新增商品', dtype=str)
      df3 = df3.astype(object).where(pd.notnull(df3), None)
      # 遍历商品价格的每一行数据
      for index, row in df1.iterrows():
        foreign_id.append(row['商品id'])
        name_ping.append(row['商品名称_平台'])
        sort1.append(row['一级分类'])
        sort2.append(row['二级分类'])
        types.append(row['类型'])
        unit.append(row['单位'])
        provider.append(row['供应商'])
        clas.append(row['品类'])
        price_source.append(row['源头采购价'])
        price_buy.append(row['平台进货价'])
        price_special.append(row['商品售价'])
        price_AB.append(row['AB类售价'])
        price_C0.append(row['C0售价'])
        in_price_C4.append(row['C4进货价'])
        in_price_C1.append(row['C1进货价'])
        in_price_C2.append(row['C2进货价'])
        in_price_C3.append(row['C3进货价'])
      # 遍历加价率的每一行数据
      for index, row in df2.iterrows():
        rate_sort1.append(row['rate_一级分类'])
        rate_sort2.append(row['rate_二级分类'])
        rate_provider.append(row['供应商_rate'])
        rate_class.append(row['品类'])
        rate.append(row['rate'])
      # 遍历新增商品的每一行数据
      for index, row in df3.iterrows():
        add_foreign_id.append(row['商品id'])
        add_name_ping.append(row['商品名称_平台'])
        add_sort1.append(row['一级分类'])
        add_sort2.append(row['二级分类'])
        add_types.append(row['类型'])
        add_unit.append(row['单位'])
        add_provider.append(row['供应商'])
        add_clas.append(row['品类'])
        add_price_source.append(row['源头采购价'])
        add_price_buy.append(row['平台进货价'])
        add_price.append(row['售价'])
      # 写入input_commodity_all
      for i in range(len(foreign_id)):
        sql = 'insert into input_commodity_all ' \
              '(`foreign_id`,`商品名称`,`一级分类`,`二级分类`,`类型`,`单位`,`供应商`,`品类`,`源头采购价`,`平台进货价`,`商品售价`,`AB类售价`,' \
              '`C0售价`,`C4进货价`,`C1进货价`,`C2进货价`,`C3进货价`) ' \
              'values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (foreign_id[i], name_ping[i], sort1[i], sort2[i], types[i], unit[i], provider[i], clas[i],
               price_source[i], price_buy[i],
               price_special[i], price_AB[i], price_C0[i], in_price_C4[i], in_price_C1[i], in_price_C2[i],
               in_price_C3[i])
        my_cursor.execute(sql, val)
        mydb.commit()
      # 写入input_rate_all
      for i in range(len(rate)):
        sql = 'insert into input_rate_all ' \
              '(`一级分类`,`二级分类`,`供应商_rate`,`品类`,`rate`) ' \
              'values (%s,%s,%s,%s,%s)'
        val = (rate_sort1[i], rate_sort2[i], rate_provider[i], rate_class[i], rate[i])
        my_cursor.execute(sql, val)
        mydb.commit()
      # 写入input_add_commodity_all
      for i in range(len(add_foreign_id)):
        sql = 'insert into input_add_commodity_all ' \
              '(`foreign_id`,`商品名称`,`一级分类`,`二级分类`,`类型`,`单位`,`供应商`,`品类`,`源头采购价`,`平台进货价`,`售价`) ' \
              'values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (add_foreign_id[i], add_name_ping[i], add_sort1[i], add_sort2[i], add_types[i], add_unit[i], add_provider[i],
        add_clas[i], add_price_source[i], add_price_buy[i], add_price[i])
        my_cursor.execute(sql, val)
        mydb.commit()
      # 新增的商品写入commodity
      for i in range(len(add_foreign_id)):
        sql = 'insert into commodity ' \
              '(`foreign_id`,`商品名称`,`一级分类`,`二级分类`,`类型`,`单位`,`供应商`,`品类`) ' \
              'values (%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (add_foreign_id[i],add_name_ping[i],add_sort1[i],add_sort2[i],add_types[i],
                       add_unit[i],add_provider[i],add_clas[i])
        my_cursor.execute(sql, val)
        mydb.commit()
      # 新增的商品写入commodity_price
      for i in range(len(add_foreign_id)):
        sql = 'insert into commodity_price ' \
              '(`foreign_id`,`商品名称`,`类型`,`源头采购价`,`平台进货价`,`售价`) ' \
              'values (%s,%s,%s,%s,%s,%s)'
        val = (add_foreign_id[i],add_name_ping[i],add_types[i],add_price_source[i],
               add_price_buy[i],add_price[i])
        my_cursor.execute(sql,val)
        mydb.commit()
      # 删除commodity_rate
      sql = 'delete from commodity_rate'
      my_cursor.execute(sql)
      mydb.commit()
      # 写入commodity_rate
      for i in range(len(rate)):
        sql = 'insert into commodity_rate ' \
              '(`一级分类`,`二级分类`,`供应商_rate`,`品类`,`rate`) ' \
              'values (%s,%s,%s,%s,%s)'
        val = (rate_sort1[i], rate_sort2[i], rate_provider[i], rate_class[i], rate[i])
        my_cursor.execute(sql, val)
        mydb.commit()
      # 写入commodity
      # 更新商品信息commodity
      for i in range(len(foreign_id)):
        sql = 'UPDATE commodity SET `商品名称`=%s,`一级分类`=%s,`二级分类`=%s,`类型`=%s,`单位`=%s,`供应商`=%s,`品类`=%s ' \
              'where `foreign_id`=%s'
        val = (name_ping[i], sort1[i], sort2[i], types[i], unit[i], provider[i], clas[i], foreign_id[i])
        my_cursor.execute(sql, val)
        mydb.commit()
      # 写入commodity_price
      # 特殊商品
      for i in range(len(foreign_id)):
        if price_special[i] is not None:
          sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s ' \
                'where `foreign_id`=%s'
          val = (name_ping[i], types[i], price_source[i], price_buy[i], price_special[i], foreign_id[i])
          my_cursor.execute(sql, val)
          mydb.commit()
      # 更新A类中有售价、B类
      for i in range(len(foreign_id)):
        if price_special[i] is None and price_source[i] is not None and price_AB[i] is not None:
          sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s,' \
                '`加价率`=%s,`反算加价率`=%s where `foreign_id`=%s'
          rate_mid = (float(price_AB[i])/float(price_source[i]))-1
          rate_mid = round(rate_mid,2)
          if rate_mid <= 0.15:
            price_buy_mid = float(price_AB[i])*0.98
            price_buy_mid = round(price_buy_mid,2)
          elif rate_mid <= 0.2:
            price_buy_mid = float(price_AB[i])*0.96
            price_buy_mid = round(price_buy_mid, 2)
          elif rate_mid <= 0.25:
            price_buy_mid = float(price_AB[i])*0.95
            price_buy_mid = round(price_buy_mid, 2)
          elif rate_mid <= 0.3:
            price_buy_mid = float(price_AB[i])*0.94
            price_buy_mid = round(price_buy_mid, 2)
          elif rate_mid > 0.3:
            price_buy_mid = float(price_AB[i])*0.93
            price_buy_mid = round(price_buy_mid, 2)
          else:
            rate_return = '有误'
            price_buy_mid = '有误'
          price_AB[i] = round(float(price_AB[i]),1)
          rate_return = (price_AB[i]/price_buy_mid)-1
          rate_return = round(rate_return,2)
          val = (name_ping[i], types[i], price_source[i], price_buy_mid, price_AB[i],rate_mid,rate_return,foreign_id[i])
          my_cursor.execute(sql, val)
          mydb.commit()
      # 更新A类中无售价
      for i in range(len(foreign_id)):
        if price_special[i] is None and price_source[i] is not None and price_AB[i] is None:
          sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s,' \
                '`加价率`=%s,`反算加价率`=%s where `foreign_id`=%s'
          rate_mid = 0
          for j in range(len(rate)):
            # 品类
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is not None and rate_class[j] is not None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i] and rate_provider[j] == \
                      provider[i] and rate_class[j] == clas[i]:
                rate_mid = rate[j]
            # 供应商
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is not None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i] and rate_provider[j] == \
                      provider[i]:
                rate_mid = rate[j]
            # 二级分类
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i]:
                rate_mid = rate[j]
            # 一级分类
            if rate_sort1[j] is not None and rate_sort2[j] is None and rate_provider[
              j] is None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i]:
                rate_mid = rate[j]

          price_mid = float(price_source[i])*(float(rate_mid)+1)
          rate_mid = float(rate_mid)
          if rate_mid <= 0.15:
            price_buy_mid = price_mid*0.98
            price_buy_mid = round(price_buy_mid,2)
          elif rate_mid <= 0.2:
            price_buy_mid = price_mid*0.96
            price_buy_mid = round(price_buy_mid, 2)
          elif rate_mid <= 0.25:
            price_buy_mid = price_mid*0.95
            price_buy_mid = round(price_buy_mid, 2)
          elif rate_mid <= 0.3:
            price_buy_mid = price_mid*0.94
            price_buy_mid = round(price_buy_mid, 2)
          elif rate_mid > 0.3:
            price_buy_mid = price_mid*0.93
            price_buy_mid = round(price_buy_mid, 2)
          else:
            rate_return = '有误'
            price_buy_mid = '有误'
          price_mid = round(price_mid,2)
          rate_return = (price_mid/price_buy_mid)-1
          rate_return = round(rate_return,2)
          val = (name_ping[i], types[i], price_source[i], price_buy_mid, price_mid,rate_mid,rate_return,foreign_id[i])
          my_cursor.execute(sql, val)
          mydb.commit()
      # C0
      for i in range(len(foreign_id)):
        if price_special[i] is None and price_C0[i] is not None:
          sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s,`反算加价率`=%s ' \
                'where `foreign_id`=%s'
          price_buy_mid = float(price_C0[i])*0.95
          price_buy_mid = round(price_buy_mid,2)
          price_C0[i] = round(float(price_C0[i]),1)
          rate_return = float(price_C0[i])/price_buy_mid-1
          rate_return = round(rate_return,2)
          val = (name_ping[i], 'C0', '0', price_buy_mid, price_C0[i],rate_return, foreign_id[i])
          my_cursor.execute(sql, val)
          mydb.commit()
      # C4
      for i in range(len(foreign_id)):
        if price_special[i] is None and in_price_C4[i] is not None and price_C0[i] is None:
          sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s,`加价率`=%s,`反算加价率`=%s ' \
                'where `foreign_id`=%s'
          rate_mid = 0
          for j in range(len(rate)):
            # 品类
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is not None and rate_class[j] is not None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i] and rate_provider[j] == \
                      provider[i] and rate_class[j] == clas[i]:
                rate_mid = rate[j]
            # 供应商
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is not None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i] and rate_provider[j] == \
                      provider[i]:
                rate_mid = rate[j]
            # 二级分类
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i]:
                rate_mid = rate[j]
            # 一级分类
            if rate_sort1[j] is not None and rate_sort2[j] is None and rate_provider[
              j] is None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i]:
                rate_mid = rate[j]
          price_mid = float(in_price_C4[i]) * 1.05 * (float(rate_mid) + 1)
          price_mid = round(price_mid,1)
          in_price_C4[i] = round(float(in_price_C4[i]),2)
          rate_return = price_mid/in_price_C4[i]-1
          rate_return = round(rate_return,2)
          val = (name_ping[i], 'C4', '0', in_price_C4[i], price_mid, rate_mid,rate_return, foreign_id[i])
          my_cursor.execute(sql, val)
          mydb.commit()
      # C1
      for i in range(len(foreign_id)):
        if price_special[i] is None and in_price_C1[i] is not None and price_C0[i] is None and in_price_C4[i] is None:
          sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s,`加价率`=%s,`反算加价率`=%s ' \
                'where `foreign_id`=%s'
          rate_mid = 0
          for j in range(len(rate)):
            # 品类
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is not None and rate_class[j] is not None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i] and rate_provider[j] == \
                      provider[i] and rate_class[j] == clas[i]:
                rate_mid = rate[j]
            # 供应商
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is not None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i] and rate_provider[j] == \
                      provider[i]:
                rate_mid = rate[j]
            # 二级分类
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i]:
                rate_mid = rate[j]
            # 一级分类
            if rate_sort1[j] is not None and rate_sort2[j] is None and rate_provider[
              j] is None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i]:
                rate_mid = rate[j]
          price_mid = float(in_price_C1[i]) * 1.05 * (float(rate_mid) + 1)
          price_mid = round(price_mid,1)
          in_price_C1[i] = round(float(in_price_C1[i]),2)
          rate_return = price_mid/in_price_C1[i]-1
          rate_return = round(rate_return,2)
          val = (name_ping[i], 'C1', '0', in_price_C1[i], price_mid, rate_mid,rate_return, foreign_id[i])
          my_cursor.execute(sql, val)
          mydb.commit()
      # C2
      for i in range(len(foreign_id)):
        if price_special[i] is None and in_price_C2[i] is not None and price_C0[i] is None and in_price_C4[i] is None and in_price_C1[i] is None:
          sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s,`加价率`=%s,`反算加价率`=%s ' \
                'where `foreign_id`=%s'
          rate_mid = 0
          for j in range(len(rate)):
            # 品类
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is not None and rate_class[j] is not None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i] and rate_provider[j] == \
                      provider[i] and rate_class[j] == clas[i]:
                rate_mid = rate[j]
            # 供应商
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is not None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i] and rate_provider[j] == \
                      provider[i]:
                rate_mid = rate[j]
            # 二级分类
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i]:
                rate_mid = rate[j]
            # 一级分类
            if rate_sort1[j] is not None and rate_sort2[j] is None and rate_provider[
              j] is None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i]:
                rate_mid = rate[j]
          price_mid = float(in_price_C2[i]) * 1.05 * (float(rate_mid) + 1)
          price_mid = round(price_mid,1)
          in_price_C2[i] = round(float(in_price_C2[i]),2)
          rate_return = price_mid/in_price_C2[i]-1
          rate_return = round(rate_return,2)
          val = (name_ping[i], 'C2', '0', in_price_C2[i], price_mid, rate_mid,rate_return, foreign_id[i])
          my_cursor.execute(sql, val)
          mydb.commit()
      # C3
      for i in range(len(foreign_id)):
        if price_special[i] is None and in_price_C3[i] is not None and price_C0[i] is None and in_price_C4[i] is None and in_price_C1[i] is None and in_price_C2[i] is None:
          sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s,`加价率`=%s,`反算加价率`=%s ' \
                'where `foreign_id`=%s'
          rate_mid = 0
          for j in range(len(rate)):
            # 品类
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is not None and rate_class[j] is not None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i] and rate_provider[j] == \
                      provider[i] and rate_class[j] == clas[i]:
                rate_mid = rate[j]

            # 供应商
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is not None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i] and rate_provider[j] == \
                      provider[i]:
                rate_mid = rate[j]

            # 二级分类
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[
              j] is None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i] and rate_sort2[j] == sort2[i]:
                rate_mid = rate[j]

            # 一级分类
            if rate_sort1[j] is not None and rate_sort2[j] is None and rate_provider[
              j] is None and rate_class[j] is None:
              if rate_sort1[j] == sort1[i]:
                rate_mid = rate[j]
          price_mid = float(in_price_C3[i]) * 1.05 * (float(rate_mid) + 1)
          price_mid = round(price_mid,1)
          in_price_C3[i] = round(float(in_price_C3[i]),2)
          rate_return = price_mid/in_price_C3[i]-1
          rate_return = round(rate_return,2)
          val = (name_ping[i], 'C3', '0', in_price_C3[i], price_mid, rate_mid,rate_return, foreign_id[i])
          my_cursor.execute(sql, val)
          mydb.commit()
      #校验 蔬果类的品类
      sql = 'UPDATE commodity_price SET `校验`=""'
      my_cursor.execute(sql)
      mydb.commit()
      sql = 'select `商品名称`,`售价` from commodity_price'
      my_cursor.execute(sql)
      result = my_cursor.fetchall()
      for row in result:
        name_same_mid.append(row[0])
        price_same_mid.append(row[1])

      for i in range(len(name_same_mid)):
        name_same.append(name_same_mid[i])
        price_same.append(price_same_mid[i])
        index1 = 0  # 标志有没有name[i]重复
        num_len = len(name_same_mid[i])
        for j in range(len(name_same_mid)):
          if i != j:  # 不能是他自己
            if len(name_same_mid[j]) > num_len:
              index2 = 0  # 标志是不是两个名字相同
              index3 = 0# 标志有没有括号
              for g in range(num_len):
                if name_same_mid[i][g] == name_same_mid[j][g]:
                  index2 += 1
              if name_same_mid[j][len(name_same_mid[j]) - 1] == ')' or name_same_mid[j][num_len] == '(' or name_same_mid[j][len(name_same_mid[j]) - 1] == '）' or \
                      name_same_mid[j][num_len] == '（':
                index3 += 1
              if index2 == num_len and index3 != 0:
                index1 += 1
                name_same.append(name_same_mid[j])
                price_same.append(price_same_mid[j])
        if index1 == 0:
          name_same.pop()
          price_same.pop()
      for i in range(len(name_same)-2):
        index4 = 0 #标志优质商品是否有
        index5 = 0 #标志精品商品是否有
        #按照没有括号的商品为基准
        if '(精品)' not in name_same[i] and '（精品）' not in name_same[i] and '(优质)' not in name_same[i] and '（优质）' not in name_same[i]:
          price_common_mid = price_same[i]
          if '(优质)' in name_same[i+1] or '（优质）' in name_same[i+1]:
            price_high_mid = price_same[i+1]
            index4 += 1
          if '(优质)' in name_same[i+2] or '（优质）' in name_same[i+2]:
            price_high_mid = price_same[i+2]
            index4 += 2
          if '(精品)' in name_same[i+1] or '（精品）' in name_same[i+1]:
            price_Boutique_mid = price_same[i+1]
            index5 += 1
          if '(精品)' in name_same[i+2] or '（精品）' in name_same[i+2]:
            price_Boutique_mid = price_same[i+2]
            index5 += 2
        if index4 == 0 and index5 != 0:
          if price_common_mid >= price_Boutique_mid:
            sql = 'UPDATE commodity_price SET `校验`=%s where `商品名称`=%s'
            val = ('错误',name_same[i])
            my_cursor.execute(sql,val)
            mydb.commit()
            if index5 == 1:
              val = ('错误', name_same[i+1])
              my_cursor.execute(sql, val)
              mydb.commit()
            elif index5 == 2:
              val = ('错误', name_same[i + 2])
              my_cursor.execute(sql, val)
              mydb.commit()
        elif index4 != 0 and index5 == 0:
          if price_common_mid >= price_high_mid:
            sql = 'UPDATE commodity_price SET `校验`=%s where `商品名称`=%s'
            val = ('错误', name_same[i])
            my_cursor.execute(sql, val)
            mydb.commit()
            if index4 == 1:
              val = ('错误', name_same[i + 1])
              my_cursor.execute(sql, val)
              mydb.commit()
            elif index4 == 2:
              val = ('错误', name_same[i + 2])
              my_cursor.execute(sql, val)
              mydb.commit()
        elif index4 != 0 and index5 != 0:
          if price_common_mid >= price_high_mid:
            sql = 'UPDATE commodity_price SET `校验`=%s where `商品名称`=%s'
            val = ('错误', name_same[i])
            my_cursor.execute(sql, val)
            mydb.commit()
            if index4 == 1:
              sql = 'UPDATE commodity_price SET `校验`=%s where `商品名称`=%s'
              val = ('错误', name_same[i+1])
              my_cursor.execute(sql, val)
              mydb.commit()
            elif index4 == 2:
              sql = 'UPDATE commodity_price SET `校验`=%s where `商品名称`=%s'
              val = ('错误', name_same[i + 2])
              my_cursor.execute(sql, val)
              mydb.commit()
          if price_common_mid >= price_Boutique_mid:
            sql = 'UPDATE commodity_price SET `校验`=%s where `商品名称`=%s'
            val = ('错误', name_same[i])
            my_cursor.execute(sql, val)
            mydb.commit()
            if index5 == 1:
              sql = 'UPDATE commodity_price SET `校验`=%s where `商品名称`=%s'
              val = ('错误', name_same[i + 1])
              my_cursor.execute(sql, val)
              mydb.commit()
            elif index5 == 2:
              sql = 'UPDATE commodity_price SET `校验`=%s where `商品名称`=%s'
              val = ('错误', name_same[i + 2])
              my_cursor.execute(sql, val)
              mydb.commit()
          if price_high_mid >= price_Boutique_mid:
            sql = 'UPDATE commodity_price SET `校验`=%s where `商品名称`=%s'
            val = ('错误', name_same[i + 1])
            my_cursor.execute(sql, val)
            mydb.commit()
            sql = 'UPDATE commodity_price SET `校验`=%s where `商品名称`=%s'
            val = ('错误', name_same[i + 2])
            my_cursor.execute(sql, val)
            mydb.commit()
    except FileNotFoundError:
      print('没有选择文件！重新运行!')
    except KeyError:
      print('表中列名请与模板中的列名一致！重新运行！')
    # except mysql.connector.errors.ProgrammingError:
    #   print('数据库中的名称与表中的名称不一致！')
  elif index == '2':
    sql = 'SELECT commodity.foreign_id,commodity.`商品名称`,commodity.`类型`, commodity.`一级分类`,commodity.`二级分类`,' \
          'commodity.`单位`,commodity.`供应商`,commodity_price.`源头采购价`,commodity_price.`平台进货价`,commodity_price.`售价` ' \
          'FROM `commodity_price`,commodity where commodity.foreign_id = commodity_price.foreign_id'
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    # 将数据转换为pandas DataFrame
    df = pd.DataFrame(result, columns=[i[0] for i in my_cursor.description])

    # 将数据写入Excel文件
    try:
      print('请输入保存路径(. 保存到程序同级路径)')
      file_out_path = input()
      df.to_excel(file_out_path+"/数据库商品信息.xlsx", index=False)
    except OSError:
      print('文件路径错误')
      continue
  elif index == '3':
    print('1.商品表 2.商品价格表 3.加价率表')
    a = input('')
    if a == '1':
      sql = 'SELECT * FROM `commodity`'
      my_cursor.execute(sql)
      result = my_cursor.fetchall()
      # 将数据转换为pandas DataFrame
      df = pd.DataFrame(result, columns=[i[0] for i in my_cursor.description])

      # 将数据写入Excel文件
      try:
        print('请输入保存路径(. 保存到程序同级路径)')
        file_out_path = input()
        df.to_excel(file_out_path + "/数据库商品表.xlsx", index=False)
      except OSError:
        print('文件路径错误')
        continue

    elif a == '2':
      sql = 'SELECT * FROM `commodity_price`'
      my_cursor.execute(sql)
      result = my_cursor.fetchall()
      # 将数据转换为pandas DataFrame
      df = pd.DataFrame(result, columns=[i[0] for i in my_cursor.description])

      # 将数据写入Excel文件
      try:
        print('请输入保存路径(. 保存到程序同级路径)')
        file_out_path = input()
        df.to_excel(file_out_path + "/数据库商品价格表.xlsx", index=False)
      except OSError:
        print('文件路径错误')
        continue
    elif a == '3':
      sql = 'SELECT * FROM `commodity_rate`'
      my_cursor.execute(sql)
      result = my_cursor.fetchall()
      # 将数据转换为pandas DataFrame
      df = pd.DataFrame(result, columns=[i[0] for i in my_cursor.description])

      # 将数据写入Excel文件
      try:
        print('请输入保存路径(. 保存到程序同级路径)')
        file_out_path = input()
        df.to_excel(file_out_path + "/数据库加价率表.xlsx", index=False)
      except OSError:
        print('文件路径错误')
        continue
    elif a == '0':
      continue
  elif index == '0':
    exit()
  else:
    print('输入选项有误，请重新输入！')

