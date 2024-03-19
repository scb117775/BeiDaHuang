from tkinter import Tk, Button, Label, filedialog
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import mysql.connector
import os
import openpyxl
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
                val = (add_foreign_id[i],add_name_ping[i],add_sort1[i],add_sort2[i],add_types[i],add_unit[i],add_provider[i],
                       add_clas[i],add_price_source[i],add_price_buy[i],add_price[i])
                my_cursor.execute(sql,val)
                mydb.commit()
            # 新增的商品写入commodity
            for i in range(len(add_foreign_id)):
                sql = 'insert into commodity ' \
                      '(`foreign_id`,`商品名称`,`一级分类`,`二级分类`,`类型`,`单位`,`供应商`,`品类`) ' \
                      'values (%s,%s,%s,%s,%s,%s,%s,%s)'
                val = (add_foreign_id[i],add_name_ping[i],add_sort1[i],add_sort2[i],add_types[i],
                       add_unit[i],add_provider[i],add_clas[i])
                my_cursor.execute(sql,val)
                mydb.commit()
            # 新增的商品写入commodity_price
            for i in range(len(add_foreign_id)):
                sql = 'insert into commodity_price ' \
                      '(`foreign_id`,`商品名称`,`类型`,`源头采购价`,`平台进货价`,`售价`) ' \
                      'values (%s,%s,%s,%s,%s,%s)'
            # 删除commodity_rate
            sql = 'delete from commodity_rate'
            my_cursor.execute(sql)
            mydb.commit()
            # 写入commodity_rate
            for i in range(len(rate)):
                sql = 'insert into commodity_rate ' \
                      '(`一级分类`,`二级分类`,`供应商_rate`,`品类`,`rate`) ' \
                      'values (%s,%s,%s,%s,%s)'
                val = (rate_sort1[i],rate_sort2[i],rate_provider[i],rate_class[i],rate[i])
                my_cursor.execute(sql,val)
                mydb.commit()
            # 写入commodity
            for i in range(len(foreign_id)):
                sql = 'UPDATE commodity SET `商品名称`=%s,`一级分类`=%s,`二级分类`=%s,`类型`=%s,`单位`=%s,`供应商`=%s,`品类`=%s ' \
                      'where `foreign_id`=%s'
                val = (name_ping[i],sort1[i],sort2[i],types[i],unit[i],provider[i],clas[i],foreign_id[i])
                my_cursor.execute(sql,val)
                mydb.commit()
            # 写入commodity_price
            # 特殊商品
            for i in range(len(foreign_id)):
                if price_special[i] is not None:
                    sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s ' \
                          'where `foreign_id`=%s'
                    val = (name_ping[i],types[i],price_source[i],price_buy[i],price_special[i],foreign_id[i])
                    my_cursor.execute(sql,val)
                    mydb.commit()
            # A类商品
            for i in range(len(foreign_id)):
                if price_special[i] is None:
                    if types[i] == 'A':
                        sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s ' \
                              'where `foreign_id`=%s'
                        val = (name_ping[i], types[i], price_source[i], price_buy[i], price_AB[i],foreign_id[i])
                        my_cursor.execute(sql, val)
                        mydb.commit()
            # B类商品
            for i in range(len(foreign_id)):
                if price_special[i] is None:
                    if types[i] == 'B':
                        sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s ' \
                              'where `foreign_id`=%s'
                        val = (name_ping[i], types[i], price_source[i], price_buy[i], price_AB[i],foreign_id[i])
                        my_cursor.execute(sql, val)
                        mydb.commit()
            # C0
            for i in range(len(foreign_id)):
                if price_special[i] is None:
                    if types[i] == 'C' and price_C0[i] is not None:
                        sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s ' \
                              'where `foreign_id`=%s'
                        val = (name_ping[i], 'C0', price_source[i], price_buy[i], price_C0[i],foreign_id[i])
                        my_cursor.execute(sql, val)
                        mydb.commit()
            # C4
            for i in range(len(foreign_id)):
                if price_special[i] is None:
                    if types[i] == 'C' and in_price_C4[i] is not None and price_C0[i] is None:
                        sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s,`加价率`=%s ' \
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
                        val = (name_ping[i], 'C4', price_source[i], in_price_C4[i], price_mid,rate_mid,foreign_id[i])
                        my_cursor.execute(sql, val)
                        mydb.commit()
            # C1
            for i in range(len(foreign_id)):
                if price_special[i] is None:
                    if types[i] == 'C' and in_price_C1[i] is not None and price_C0[i] is None and in_price_C4[i] is None:
                        sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s,`加价率`=%s ' \
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
                        val = (name_ping[i], 'C1', price_source[i], in_price_C1[i], price_mid,rate_mid, foreign_id[i])
                        my_cursor.execute(sql, val)
                        mydb.commit()
            # C2
            for i in range(len(foreign_id)):
                if price_special[i] is None:
                    if types[i] == 'C' and in_price_C2[i] is not None and price_C0[i] is None and in_price_C4[i] is None and in_price_C1[i] is None:
                        sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s,`加价率`=%s ' \
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
                        val = (name_ping[i], 'C2', price_source[i], in_price_C2[i], price_mid,rate_mid, foreign_id[i])
                        my_cursor.execute(sql, val)
                        mydb.commit()
            # C3
            for i in range(len(foreign_id)):
                if price_special[i] is None:
                    if types[i] == 'C' and in_price_C3[i] is not None and price_C0[i] is None and in_price_C4[i] is None and in_price_C1[i] is None and in_price_C2[i] is None:
                        sql = 'UPDATE commodity_price SET `商品名称`=%s,`类型`=%s,`源头采购价`=%s,`平台进货价`=%s,`售价`=%s,`加价率`=%s ' \
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
                        val = (name_ping[i], 'C3', price_source[i], in_price_C3[i], price_mid,rate_mid, foreign_id[i])
                        my_cursor.execute(sql, val)
                        mydb.commit()
        except FileNotFoundError:
            print('没有选择文件！重新运行!')
        except KeyError:
            print('表中列名请与模板中的列名一致！重新运行！')
        except mysql.connector.errors.ProgrammingError:
            print('数据库中的名称与表中的名称不一致！')
        except Exception as e:
            print('有错误！重新运行！')
            print("发生错误:", str(e))
            time.sleep(3)
            exit()
    elif index == '2':
        pass
    elif index == '0':
        exit()
    else:
        print('输入选项有误，请重新输入！')





