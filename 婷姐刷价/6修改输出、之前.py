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
import math

# 连接到MySQL数据库
mydb = mysql.connector.connect(
  host="192.168.112.215",
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

#输入模版  1.1商品库
foreign_id_1_1 = []
sort1_1_1 = []
sort2_1_1 = []
name_1_1 = []
unit_1_1 = []
brand_1_1 = []

#输入模版 2.1四家平台同品商品价格 A类
foreign_id_2_1 = []
provider_2_1 = []
price_source_2_1 = []
price_2_1 = []
rate_return_2_1 = []

#输入模版 2.2教委指定供应商报价明细表 A类
foreign_id_2_2 = []
sort1_2_2 = []
sort2_2_2 = []
provider_2_2 = []
price_source_2_2 = []

#输入模版 2.3.0合作方报价商品-鲜诺达 C0
foreign_id_2_3_0 = []
price_2_3_0 = []

#输入模版 2.3.1合作方报价商品-锦绣大地 C1
foreign_id_2_3_1 = []
sort1_2_3_1 = []
sort2_2_3_1 = []
price_buy_2_3_1 = []

#输入模版 2.3.2合作方报价商品-恒盛众德 C2
foreign_id_2_3_2 = []
sort1_2_3_2 = []
sort2_2_3_2 = []
price_buy_2_3_2 = []

#输入模版 2.3.4合作方报价商品-利源百发 C4
foreign_id_2_3_4 = []
sort1_2_3_4 = []
sort2_2_3_4 = []
price_buy_2_3_4 = []

#输入模版 3.1平台商品加价率
rate_sort1 = []
rate_sort2 = []
rate_provider = []
rate = []

price_mid = 0
price_source_mid = 0
price_buy_mid = 0
rate_mid = 0
rate_return_mid = 0

foreign_id_yes = []

# #处理售价
# def handle_5(a):
#   stra = str(a)
#   if len(stra) > 4:
#     if stra[-1] == '5':
#       stra = stra + '6'
#       return float(stra)
#     else:
#       return float(stra)
#   else:
#     return float(stra)
################################################################################################################
print('1.上传模版刷价  2.导出商品信息  0.退出')
while True:
  index = input('请输入选项:')
  if index == '1':
    try:
      print('计算中......')
      df1_1 = pd.read_excel(open(file_path, 'rb'), sheet_name='1.1商品库', dtype=str)
      df1_1 = df1_1.astype(object).where(pd.notnull(df1_1), None)
      for index, row in df1_1.iterrows():
        foreign_id_1_1.append(row['商品ID'])
        sort1_1_1.append(row['一级分类'])
        sort2_1_1.append(row['二级分类'])
        name_1_1.append(row['商品名称'])
        unit_1_1.append(row['单位'])
        brand_1_1.append(row['品牌'])
        # print(row)


      df2_1 = pd.read_excel(open(file_path, 'rb'), sheet_name='2.1四家平台同品商品价格', dtype=str)
      df2_1 = df2_1.astype(object).where(pd.notnull(df2_1), None)
      for index, row in df2_1.iterrows():
        foreign_id_2_1.append(row['商品ID'])
        provider_2_1.append(row['指定供应商'])
        price_source_2_1.append(row['源头进货价'])
        price_2_1.append(row['平台售价'])
        rate_return_2_1.append(row['反算加价率'])
        # print(row)


      df2_2 = pd.read_excel(open(file_path, 'rb'), sheet_name='2.2教委指定供应商报价明细表', dtype=str)
      df2_2 = df2_2.astype(object).where(pd.notnull(df2_2), None)
      for index, row in df2_2.iterrows():
        foreign_id_2_2.append(row['商品ID'])
        sort1_2_2.append(row['一级分类'])
        sort2_2_2.append(row['二级分类'])
        provider_2_2.append(row['指定供应商'])
        price_source_2_2.append(row['采购价'])


      df2_3_0 = pd.read_excel(open(file_path, 'rb'), sheet_name='2.3.0合作方报价商品-鲜诺达', dtype=str)
      df2_3_0 = df2_3_0.astype(object).where(pd.notnull(df2_3_0), None)
      for index, row in df2_3_0.iterrows():
        foreign_id_2_3_0.append(row['商品ID'])
        price_2_3_0.append(row['价格'])
        # print(row)


      df2_3_1 = pd.read_excel(open(file_path, 'rb'), sheet_name='2.3.1合作方报价商品-锦绣大地', dtype=str)
      df2_3_1 = df2_3_1.astype(object).where(pd.notnull(df2_3_1), None)
      for index, row in df2_3_1.iterrows():
        foreign_id_2_3_1.append(row['商品ID'])
        sort1_2_3_1.append(row['一级分类'])
        sort2_2_3_1.append(row['二级分类'])
        price_buy_2_3_1.append(row['价格'])
        # print(row)


      df2_3_2 = pd.read_excel(open(file_path, 'rb'), sheet_name='2.3.2合作方报价商品-恒盛众德', dtype=str)
      df2_3_2 = df2_3_2.astype(object).where(pd.notnull(df2_3_2), None)
      for index, row in df2_3_2.iterrows():
        foreign_id_2_3_2.append(row['商品ID'])
        sort1_2_3_2.append(row['一级分类'])
        sort2_2_3_2.append(row['二级分类'])
        price_buy_2_3_2.append(row['价格'])
        # print(row)


      df2_3_4 = pd.read_excel(open(file_path, 'rb'), sheet_name='2.3.4合作方报价商品-利源百发', dtype=str)
      df2_3_4 = df2_3_4.astype(object).where(pd.notnull(df2_3_4), None)
      for index, row in df2_3_4.iterrows():
        foreign_id_2_3_4.append(row['商品ID'])
        sort1_2_3_4.append(row['一级分类'])
        sort2_2_3_4.append(row['二级分类'])
        price_buy_2_3_4.append(row['价格'])
        # print(row)


      df3_1 = pd.read_excel(open(file_path, 'rb'), sheet_name='3.1平台商品加价率', dtype=str)
      df3_1 = df3_1.astype(object).where(pd.notnull(df3_1), None)
      for index, row in df3_1.iterrows():
        rate_sort1.append(row['一级分类'])
        rate_sort2.append(row['二级分类'])
        rate_provider.append(row['教委指定供应商名称'])
        rate.append(row['销售加价率'])


      # 写入commodity
      sql = 'delete from commodity'
      my_cursor.execute(sql)
      mydb.commit()
      for i in range(len(foreign_id_1_1)):
        sql = 'insert into commodity ' \
              '(`foreign_id`,`商品名称`,`一级分类`,`二级分类`,`单位`) ' \
              'values (%s,%s,%s,%s,%s)'
        val = (foreign_id_1_1[i],name_1_1[i],sort1_1_1[i],sort2_1_1[i],unit_1_1[i])
        my_cursor.execute(sql,val)
        mydb.commit()


      # 写入commodity_price
      sql = 'delete from commodity_price'
      my_cursor.execute(sql)
      mydb.commit()
      for i in range(len(foreign_id_1_1)):
        sql = 'insert into commodity_price ' \
              '(`foreign_id`,`商品名称`) ' \
              'values (%s,%s)'
        val = (foreign_id_1_1[i],name_1_1[i])
        my_cursor.execute(sql,val)
        mydb.commit()


      #写入 commodity_rate
      sql = 'delete from commodity_rate'
      my_cursor.execute(sql)
      mydb.commit()
      for i in range(len(rate)):
        sql = 'insert into commodity_rate ' \
              '(`一级分类`,`二级分类`,`供应商`,`rate`) ' \
              'values (%s,%s,%s,%s)'
        val = (rate_sort1[i],rate_sort2[i],rate_provider[i],rate[i])
        my_cursor.execute(sql,val)
        mydb.commit()

      # 更新2.1 A
      for i in range(len(foreign_id_2_1)):
        sql = 'update commodity_price set `类型`=%s,`供应商`=%s,`源头采购价`=%s,`采购价（含费）`=%s,`平台进货价`=%s,`配送服务费`=%s,`售价`=%s,' \
              '`加价率`=%s,`反算加价率`=%s where `foreign_id`=%s'
        rate_return_2_1[i] = round(float(rate_return_2_1[i]),2)
        price_2_1[i] = round(float(price_2_1[i]),1)
        if rate_return_2_1[i] <=0.15:
          price_buy_mid = price_2_1[i]*0.98
          price_buy_mid = round(price_buy_mid,2)
        elif rate_return_2_1[i] <= 0.2:
          price_buy_mid = price_2_1[i] * 0.96
          price_buy_mid = round(price_buy_mid,2)
        elif rate_return_2_1[i] <= 0.25:
          price_buy_mid = price_2_1[i] * 0.95
          price_buy_mid = round(price_buy_mid,2)
        elif rate_return_2_1[i] <= 0.3:
          price_buy_mid = price_2_1[i] * 0.94
          price_buy_mid = round(price_buy_mid,2)
        elif rate_return_2_1[i] >0.3:
          price_buy_mid = price_2_1[i] * 0.93
          price_buy_mid = round(price_buy_mid,2)
        if price_buy_mid == 0:
            rate_return_mid =0
        else:
          rate_return_mid = price_2_1[i]/price_buy_mid-1
          rate_return_mid = (int(rate_return_mid*10**2))/10**2
        val = ('A',provider_2_1[i],price_source_2_1[i],price_buy_mid,round(price_buy_mid*0.95,2),round(price_buy_mid*0.05,2),price_2_1[i],rate_return_2_1[i],rate_return_mid,
               foreign_id_2_1[i])
        my_cursor.execute(sql,val)
        mydb.commit()
        foreign_id_yes.append(foreign_id_2_1[i])


      # 更新2.2 A
      for i in range(len(foreign_id_2_2)):
        if foreign_id_2_2[i] not in foreign_id_yes:
          sql = 'update commodity_price set `类型`=%s,`供应商`=%s,`源头采购价`=%s,`采购价（含费）`=%s,`平台进货价`=%s,`配送服务费`=%s,`售价`=%s,' \
                '`加价率`=%s,`反算加价率`=%s where `foreign_id`=%s'
          for j in range(len(rate)):
            # 供应商
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[j] is not None:
              if rate_sort1[j] == sort1_2_2[i] and rate_sort2[j] == sort2_2_2[i] and rate_provider[j] == provider_2_2[i]:
                rate_mid = float(rate[j])
                break
            # 二级分类
            if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[j] is None:
              if rate_sort1[j] == sort1_2_2[i] and rate_sort2[j] == sort2_2_2[i]:
                rate_mid = float(rate[j])
                break
            # 一级分类
            if rate_sort1[j] is not None and rate_sort2[j] is None and rate_provider[j] is None:
              if rate_sort1[j] == sort1_2_2[i]:
                rate_mid = float(rate[j])
                break

          price_mid = (float(price_source_2_2[i])*(rate_mid+1))
          price_mid = round(price_mid,1)
          if rate_mid <= 0.15:
            price_buy_mid = (price_mid * 0.98)
          elif rate_mid <= 0.2:
            price_buy_mid = (price_mid * 0.96)
          elif rate_mid <=0.25:
            price_buy_mid = (price_mid * 0.95)
          elif rate_mid <= 0.3:
            price_buy_mid = (price_mid * 0.94)
          elif rate_mid > 0.3:
            price_buy_mid = (price_mid * 0.93)
          if price_source_2_2[i] == '0':
            rate_mid = round(rate_mid, 2)
            rate_return_mid = 0
            price_mid = 0
            price_buy_mid = 0
          else:
            rate_mid = round(rate_mid,2)
            rate_return_mid = price_mid / float(price_buy_mid)-1
            rate_return_mid = round(rate_return_mid,2)
            price_buy_mid = round(price_buy_mid, 2)
          val = ('A',provider_2_2[i],price_source_2_2[i],price_buy_mid,round(price_buy_mid*0.95,2),round(price_buy_mid*0.05,2),price_mid,rate_mid,rate_return_mid,foreign_id_2_2[i])
          my_cursor.execute(sql,val)
          mydb.commit()
          foreign_id_yes.append(foreign_id_2_2[i])


      # 更新2.3.0 C0-鲜诺达
      for i in range(len(foreign_id_2_3_0)):
        if foreign_id_2_3_0[i] not in foreign_id_yes:
          if price_2_3_0[i] != '0':
            price_2_3_0[i] = round(float(price_2_3_0[i]),1)
            sql = 'update commodity_price set `类型`=%s,`源头采购价`=%s,`采购价（含费）`=%s,`平台进货价`=%s,`配送服务费`=%s,`售价`=%s,' \
                  '`加价率`=%s,`反算加价率`=%s where `foreign_id`=%s'
            price_buy_mid = float(price_2_3_0[i]) * 0.95
            rate_return_mid = float(price_2_3_0[i]) / price_buy_mid -1
            price_buy_mid = round(price_buy_mid,2)
            rate_return_mid = round(rate_return_mid,2)
            val = ('C0','0',price_buy_mid,round(price_buy_mid*0.95,2),round(price_buy_mid*0.05,2),price_2_3_0[i],rate_return_mid,rate_return_mid,foreign_id_2_3_0[i])
            my_cursor.execute(sql,val)
            mydb.commit()
            foreign_id_yes.append(foreign_id_2_3_0[i])


      # 更新2.3.4 C4-利源百发
      for i in range(len(foreign_id_2_3_4)):
        if foreign_id_2_3_4[i] not in foreign_id_yes:
          if price_buy_2_3_4[i] != '0':
            sql = 'update commodity_price set `类型`=%s,`源头采购价`=%s,`采购价（含费）`=%s,`平台进货价`=%s,`配送服务费`=%s,`售价`=%s,' \
                  '`加价率`=%s,`反算加价率`=%s where `foreign_id`=%s'
            # for j in range(len(rate)):
            #   # 二级分类
            #   if rate_sort1[j] is not None and rate_sort2[j] is not None and rate_provider[j] is None:
            #     if rate_sort1[j] == sort1_2_3_4[i] and rate_sort2[j] == sort2_2_3_4[i]:
            #       rate_mid = float(rate[j])
            #       break
            #   # 一级分类
            #   if rate_sort1[j] is not None and rate_sort2[j] is None and rate_provider[j] is None:
            #     if rate_sort1[j] == sort1_2_3_4[i]:
            #       rate_mid = float(rate[j])
            #       break

            price_mid = (10**2 * float(price_buy_2_3_4[i]) * 1.05 ) / 10**2
            price_mid = round(price_mid,1)
            rate_return_mid = price_mid / float(price_buy_2_3_4[i]) - 1
            rate_return_mid = (int(rate_return_mid) * 10 ** 2) / 10 ** 2
            price_buy_2_3_4[i] = round(float(price_buy_2_3_4[i]),2)
            val = ('C4','0',price_buy_2_3_4[i],round(price_buy_2_3_4[i]*0.95,2),round(price_buy_2_3_4[i]*0.05,2),price_mid,'0',rate_return_mid,foreign_id_2_3_4[i])
            my_cursor.execute(sql,val)
            mydb.commit()
            foreign_id_yes.append(foreign_id_2_3_4[i])


      # 更新2.3.1 C1-锦绣大地
      for i in range(len(foreign_id_2_3_1)):
        if foreign_id_2_3_1[i] not in foreign_id_yes:
          if price_buy_2_3_1[i] != '0':
            sql = 'update commodity_price set `类型`=%s,`源头采购价`=%s,`采购价（含费）`=%s,`平台进货价`=%s,`配送服务费`=%s,`售价`=%s,' \
                  '`加价率`=%s,`反算加价率`=%s where `foreign_id`=%s'
            price_mid = (10**2 * float(price_buy_2_3_1[i]) * 1.05) / 10**2
            price_mid = round(price_mid,1)
            rate_return_mid = price_mid / float(price_buy_2_3_1[i]) - 1
            rate_return_mid = (int(rate_return_mid) * 10 ** 2) / 10 ** 2
            price_buy_2_3_1[i] = round(float(price_buy_2_3_1[i]),2)
            val = ('C1','0',price_buy_2_3_1[i],round(price_buy_2_3_1[i]*0.95,2),round(price_buy_2_3_1[i]*0.05,2),price_mid,'0',rate_return_mid,foreign_id_2_3_1[i])
            my_cursor.execute(sql,val)
            mydb.commit()
            foreign_id_yes.append(foreign_id_2_3_1[i])


      # 更新2.3.2 C2-恒盛众德
      for i in range(len(foreign_id_2_3_2)):
        if foreign_id_2_3_2[i] not in foreign_id_yes:
          if price_buy_2_3_2[i] != '0':
            sql = 'update commodity_price set `类型`=%s,`源头采购价`=%s,`采购价（含费）`=%s,`平台进货价`=%s,`配送服务费`=%s,`售价`=%s,' \
                  '`加价率`=%s,`反算加价率`=%s where `foreign_id`=%s'
            price_mid = (10**2 * float(price_buy_2_3_2[i]) * 1.05) / 10**2
            price_mid = round(price_mid,1)
            rate_return_mid = price_mid / float(price_buy_2_3_2[i]) - 1
            rate_return_mid = (int(rate_return_mid * 10 ** 2)) / 10 ** 2
            price_buy_2_3_2[i] = round(float(price_buy_2_3_2[i]),2)
            val = ('C2','0',price_buy_2_3_2[i],round(price_buy_2_3_2[i]*0.95,2),round(price_buy_2_3_2[i]*0.05,2),price_mid,'0',rate_return_mid,foreign_id_2_3_2[i])
            my_cursor.execute(sql,val)
            mydb.commit()
            foreign_id_yes.append(foreign_id_2_3_2[i])


      #处理没有售价的
      for i in range(len(foreign_id_1_1)):
        if foreign_id_1_1[i] not in foreign_id_yes:
          sql = 'update commodity_price set `源头采购价`=%s,`采购价（含费）`=%s,`平台进货价`=%s,`配送服务费`=%s,`售价`=%s,' \
                '`加价率`=%s,`反算加价率`=%s where `foreign_id`=%s'
          val = ('0','0','0','0','0','0','0',foreign_id_1_1[i])
          my_cursor.execute(sql,val)
          mydb.commit()
      #处理commodity_info_all
      sql = 'INSERT into commodity_info_all (commodity_info_all.foreign_id,commodity_info_all.`商品名称`,commodity_info_all.`一级分类`' \
            ',commodity_info_all.`二级分类`,commodity_info_all.`单位`,commodity_info_all.`供应商`,commodity_info_all.`类型`,' \
            'commodity_info_all.`品类`,commodity_info_all.`源头采购价`,commodity_info_all.`采购价（含费）`,commodity_info_all.`平台进货价`,commodity_info_all.`配送服务费`,commodity_info_all.`商品售价`)' \
            ' SELECT commodity.foreign_id,commodity.`商品名称`,commodity.`一级分类`,commodity.`二级分类`,commodity.`单位`,' \
            'commodity_price.`供应商`,commodity_price.`类型`,commodity.`品类`,commodity_price.`源头采购价`,commodity_price.`采购价（含费）`,commodity_price.`平台进货价`,commodity_price.`配送服务费`, ' \
            'commodity_price.`售价` from commodity INNER JOIN commodity_price ON commodity.foreign_id=commodity_price.foreign_id'
      my_cursor.execute(sql)
      mydb.commit()
      
      print('刷价已完成，请选择功能2！')
    except FileNotFoundError:
      print('没有选择文件！重新运行!')
    # except KeyError:
    #   print('表中列名请与模板中的列名一致！重新运行！')
    # except mysql.connector.errors.ProgrammingError:
    #   print('数据库中的名称与表中的名称不一致！')
    # except:
    #   print('运行出错！')
  elif index == '2':
    print('1、 4.1报价表 2、 4.0源头采购价 3、 4.3平台进货价&服务费 4、 4.2平台销售价 0、 退出')
    index1 = input('请输入导出商品信息选项:')
    if index1 == '1':
      sql = "SELECT commodity.foreign_id 商品ID,commodity.`一级分类`,commodity.`二级分类`,commodity.`商品名称`,commodity.`单位`,commodity_price.`类型` 类别, " \
            "commodity_price.`源头采购价`,commodity_price.`采购价（含费）`,commodity_price.`平台进货价`,commodity_price.`配送服务费`,commodity_price.`售价` FROM commodity " \
            "INNER JOIN commodity_price ON commodity.foreign_id = commodity_price.foreign_id"
      my_cursor.execute(sql)
      result = my_cursor.fetchall()
      # 将数据转换为pandas DataFrame
      df = pd.DataFrame(result, columns=[i[0] for i in my_cursor.description])
      try:
        print('请输入保存路径(. 保存到程序同级路径)')
        file_out_path = input()
        df.to_excel(file_out_path + "/4.1报价表.xlsx", index=False)
      except OSError:
        print('文件路径错误')
    elif index1 == '2':
      sql = "SELECT commodity.foreign_id 商品ID,commodity.`一级分类`,commodity.`二级分类`,commodity.`商品名称`,commodity.`单位`,commodity_price.`类型` 类别, " \
            "commodity_price.`源头采购价` FROM commodity " \
            "INNER JOIN commodity_price ON commodity.foreign_id = commodity_price.foreign_id"
      my_cursor.execute(sql)
      result = my_cursor.fetchall()
      # 将数据转换为pandas DataFrame
      df = pd.DataFrame(result, columns=[i[0] for i in my_cursor.description])
      try:
        print('请输入保存路径(. 保存到程序同级路径)')
        file_out_path = input()
        df.to_excel(file_out_path + "/4.0源头采购价.xlsx", index=False)
      except OSError:
        print('文件路径错误')
    elif index1 == '3':
      sql = "SELECT commodity.foreign_id 商品ID,commodity.`一级分类`,commodity.`二级分类`,commodity.`商品名称`,commodity.`单位`,commodity_price.`类型` 类别, " \
            "commodity_price.`平台进货价`,commodity_price.`配送服务费` FROM commodity " \
            "INNER JOIN commodity_price ON commodity.foreign_id = commodity_price.foreign_id"
      my_cursor.execute(sql)
      result = my_cursor.fetchall()
      # 将数据转换为pandas DataFrame
      df = pd.DataFrame(result, columns=[i[0] for i in my_cursor.description])
      try:
        print('请输入保存路径(. 保存到程序同级路径)')
        file_out_path = input()
        df.to_excel(file_out_path + "/4.3平台进货价&服务费.xlsx", index=False)
      except OSError:
        print('文件路径错误')
    elif index1 == '4':
      sql = "SELECT commodity.foreign_id 商品ID,commodity.`一级分类`,commodity.`二级分类`,commodity.`商品名称`,commodity.`单位`,commodity_price.`类型` 类别, " \
            "commodity_price.`售价` FROM commodity " \
            "INNER JOIN commodity_price ON commodity.foreign_id = commodity_price.foreign_id"
      my_cursor.execute(sql)
      result = my_cursor.fetchall()
      # 将数据转换为pandas DataFrame
      df = pd.DataFrame(result, columns=[i[0] for i in my_cursor.description])
      try:
        print('请输入保存路径(. 保存到程序同级路径)')
        file_out_path = input()
        df.to_excel(file_out_path + "/4.2平台销售价.xlsx", index=False)
      except OSError:
        print('文件路径错误')
    elif index1 == '0':continue
    else:print('输入选项错误!')

  elif index == '3':
    print('1.商品表 2.商品价格表 3.商品加价率')
    index2 = input('输入选项:')
    if index2 == '1':
      sql = "SELECT * from commodity"
      my_cursor.execute(sql)
      result = my_cursor.fetchall()
      # 将数据转换为pandas DataFrame
      df = pd.DataFrame(result, columns=[i[0] for i in my_cursor.description])
      try:
        print('请输入保存路径(. 保存到程序同级路径)')
        file_out_path = input()
        df.to_excel(file_out_path + "/商品信息表.xlsx", index=False)
      except OSError:
        print('文件路径错误')
    elif index2 == '2':
      sql = "SELECT * from commodity_price"
      my_cursor.execute(sql)
      result = my_cursor.fetchall()
      # 将数据转换为pandas DataFrame
      df = pd.DataFrame(result, columns=[i[0] for i in my_cursor.description])
      try:
        print('请输入保存路径(. 保存到程序同级路径)')
        file_out_path = input()
        df.to_excel(file_out_path + "/商品价格表.xlsx", index=False)
      except OSError:
        print('文件路径错误')
    elif index2 == '3':
      sql = "SELECT * from commodity_rate"
      my_cursor.execute(sql)
      result = my_cursor.fetchall()
      # 将数据转换为pandas DataFrame
      df = pd.DataFrame(result, columns=[i[0] for i in my_cursor.description])
      try:
        print('请输入保存路径(. 保存到程序同级路径)')
        file_out_path = input()
        df.to_excel(file_out_path + "/商品加价率.xlsx", index=False)
      except OSError:
        print('文件路径错误')
    elif index2 == '0':continue
    else:print('输入选项错误!')
  elif index == '0':
    exit()
  else:
    print('输入选项错误，请重新输入!')




