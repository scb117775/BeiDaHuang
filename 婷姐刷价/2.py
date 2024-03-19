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

mycursor = mydb.cursor()

# 创建主窗口
root = Tk()
root.withdraw()
#选择文件的上传路径
file_path = filedialog.askopenfilename()
#变量定义
name_all=['foreign_id','name_ping','name_new','type','sort1','sort2','brand','specifications','provider',
          'is_base','is_base','price_source','price_buy','price_AB','price_C0','price_C4','in_price_C1','in_price_C2','in_price_C3',
          'rate_sort1','rate_sort2','rate_provider','rate_commodity','rate']
foreign_id = [] #foreign_id
name_ping = [] #商品名称_平台
name_new = [] #商品名称_新
type = [] #类型
sort1 = []  #一级分类
sort2 = []  #二级分类
brand = []  #品牌
unit = [] #单位
specifications = [] #规格
provider = [] #供应商
is_sell = []#是否上架
is_base = []  #是否基础单位
price_source = [] #源头采购价
price_buy = []#平台进货价
price_AB =[] #AB类售价
price_C0 = [] #C0售价
# price_C4 = [] #C4售价
in_price_C4 = [] #C4进货价
in_price_C1 = [] #C1进货
in_price_C2 = [] #C2进货
in_price_C3 = [] #C3进货

rate_sort1 = [] #rate_一级分类
rate_sort2 = [] #rate_二级分类
rate_provider = [] #供应商
rate_commodity = [] #特殊商品
rate = [] #rate

add_foreign_id = [] #新增商品id
add_name_ping = [] #新增商品平台名称
add_name_new = []#新增商品名称新
add_type = []#新增商品类型
add_sort1 = []#新增商品一级分类
add_sort2 = []#新增商品二级分类
add_brand = []#新增商品品牌
add_unit = []#新增商品单位
add_specifications = []#新增商品规格
add_provider = []#新增商品供应商
add_is_sell = []#新增商品是否上架
add_is_base = []#新增商品是否基本单位
add_price_source = []#新增商品源头采购价
add_price_buy = []#新增商品平台进货价
add_price = []#新增商品售价

################################################################################################################
print('1.上传模版刷价加品  2.导出商品及价格  0.退出')
while True:
    index = input('请输入选项:')
    if index == '1':
        try:
            df1 = pd.read_excel(open(file_path, 'rb'), sheet_name='商品价格',dtype=str)
            df1 = df1.astype(object).where(pd.notnull(df1), None)
            df2 = pd.read_excel(open(file_path, 'rb'), sheet_name='加价率',dtype=str)
            df2 = df2.astype(object).where(pd.notnull(df2), None)
            df3 = pd.read_excel(open(file_path, 'rb'), sheet_name='新增商品', dtype=str)
            df3 = df3.astype(object).where(pd.notnull(df3), None)
            # 遍历商品价格的每一行数据
            for index, row in df1.iterrows():
                foreign_id.append(row['商品id'])
                name_ping.append(row['商品名称_平台'])
                name_new.append(row['商品名称_新'])
                type.append(row['类型'])
                sort1.append(row['一级分类'])
                sort2.append(row['二级分类'])
                brand.append(row['品牌'])
                unit.append(row['单位'])
                specifications.append(row['规格'])
                provider.append(row['供应商'])
                is_sell.append(row['是否上架'])
                is_base.append(row['是否基础单位'])
                price_source.append(row['源头采购价'])
                price_buy.append(row['平台进货价'])
                price_AB.append(row['AB类售价'])
                price_C0.append(row['C0售价'])
                # price_C4.append(row['C4售价'])
                in_price_C4.append(row['C4进货价'])
                in_price_C1.append(row['C1进货价'])
                in_price_C2.append(row['C2进货价'])
                in_price_C3.append(row['C3进货价'])
            # 遍历加价率的每一行数据
            for index, row in df2.iterrows():
                rate_sort1.append(row['rate_一级分类'])
                rate_sort2.append(row['rate_二级分类'])
                rate_provider.append(row['供应商_rate'])
                rate_commodity.append(row['特殊商品'])
                rate.append(row['rate'])
            # 遍历新增商品的每一行数据
            for index, row in df3.iterrows():
                add_foreign_id.append(row['商品id'])
                add_name_ping.append(row['商品名称_平台'])
                add_name_new.append(row['商品名称_新'])
                add_type.append(row['类型'])
                add_sort1.append(row['一级分类'])
                add_sort2.append(row['二级分类'])
                add_brand.append(row['品牌'])
                add_unit.append(row['单位'])
                add_specifications.append(row['规格'])
                add_provider.append(row['供应商'])
                add_is_sell.append(row['是否上架'])
                add_is_base.append(row['是否基础单位'])
                add_price_source.append(row['源头采购价'])
                add_price_buy.append(row['平台进货价'])
                add_price.append(row['售价'])
            #新增加商品
            if len(add_foreign_id) != 0:
                for i in range(len(add_foreign_id)):
                    sql = 'insert into commodity (`foreign_id`,`商品名称`,`商品名称_新`,`一级分类`,`二级分类`,`类型`,`供应商`,`单位`,`品牌`,`规格`,' \
                          '`是否上架`,`是否基础单位`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    val = (add_foreign_id[i],add_name_ping[i],add_name_new[i],add_sort1[i],add_sort2[i],add_type[i],add_provider[i],
                           add_unit[i],add_brand[i],add_specifications[i],add_is_sell[i],add_is_base[i])
                    mycursor.execute(sql,val)
                    mydb.commit()
                    sql = 'insert into commodity_price (`foreign_id`,`类型`,`商品名称`,`商品名称_新`,`源头采购价`,`平台进货价`,`销售价`) ' \
                          'values (%s,%s,%s,%s,%s,%s,%s)'
                    val  = (add_foreign_id[i],add_type[i],add_name_ping[i],add_name_new[i],add_price_source[i],add_price_buy[i],add_price[i])
                    mycursor.execute(sql, val)
                    mydb.commit()
            # 将数据写入输入表
            for i in range(len(foreign_id)):#写商品信息
                sql = 'insert  into input_commodity_all (`foreign_id`,`商品名称`,`商品名称_新`,`类型`,`一级分类`,`二级分类`,`品牌`,`单位`,`规格`,' \
                      '`供应商`,`是否上架`,`是否基础单位`,`源头采购价`,`平台进货价`,`AB类售价`,`C0售价`,`C4进货价`,`C1进货价`,`C2进货价`,`C3进货价`) ' \
                      'values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                val = (
                foreign_id[i], name_ping[i], name_new[i], type[i], sort1[i], sort2[i], brand[i],unit[i] ,specifications[i],
                provider[i],is_sell[i],is_base[i], price_source[i], price_buy[i] ,price_AB[i], price_C0[i], in_price_C4[i], in_price_C1[i], in_price_C2[i],in_price_C3[i])
                mycursor.execute(sql, val)
                mydb.commit()
            # 写加价率
            for i in range(len(rate)):
                sql = 'insert into input_rate_all (`一级分类_rate`,`二级分类_rate`,`供应商_rate`,`特殊商品`,`rate`) values (%s,%s,%s,%s,%s)'
                val = (rate_sort1[i],rate_sort2[i],rate_provider[i],rate_commodity[i],rate[i])
                mycursor.execute(sql,val)
                mydb.commit()
            # 将数据中商品基本更新商品表
            for i in range(len(foreign_id)):
                sql = 'UPDATE commodity SET `商品名称`=%s,`商品名称_新`=%s,`一级分类`=%s,`二级分类`=%s,`类型`=%s,' \
                      '`供应商`=%s,`品牌`=%s,`单位`=%s,`规格`=%s,`是否上架`=%s,`是否基础单位`=%s where `foreign_id` = %s'
                val = (name_ping[i], name_new[i], sort1[i], sort2[i], type[i],
                       provider[i],brand[i], unit[i],specifications[i], is_sell[i],is_base[i],foreign_id[i])
                mycursor.execute(sql, val)
                mydb.commit()
            # 更新加价率 先更新加价率防止刷价错误
            num1 = 0
            for i in range(len(rate)):
                if rate_commodity[i] is not None:
                    sql = 'insert into commodity_rate_all (`特殊商品`,`供应商_rate`,`二级分类`,`一级分类`,`rate`) values(%s,%s,%s,%s,%s)'
                    val = (rate_commodity[i], rate_provider[i], rate_sort2[i], rate_sort1[i], rate[i])
                    mycursor.execute(sql, val)
                    mydb.commit()
                elif rate_provider[i] is not None:
                    sql = 'insert into commodity_rate_all (`供应商_rate`,`二级分类`,`一级分类`,`rate`) values(%s,%s,%s,%s)'
                    val = (rate_provider[i], rate_sort2[i], rate_sort1[i], rate[i])
                    mycursor.execute(sql, val)
                    mydb.commit()
                elif rate_sort2[i] is not None:
                    sql = 'insert into commodity_rate_all (`二级分类`,`一级分类`,`rate`) values(%s,%s,%s)'
                    val = (rate_sort2[i], rate_sort1[i], rate[i])
                    mycursor.execute(sql, val)
                    mydb.commit()
                elif rate_sort1[i] is not None:
                    sql = 'insert into commodity_rate_all (`一级分类`,`rate`) values(%s,%s)'
                    val = (rate_sort1[i], rate[i])
                    mycursor.execute(sql, val)
                    mydb.commit()
                else:
                    num1 += 1
                    print('加价率刷新失败！')
            # 能取成功加价率
            if num1 == 0:
                sql = 'DELETE from commodity_rate' #先删除表中所有数据
                mycursor.execute(sql)
                mydb.commit()
                for i in range(len(rate)):
                    if rate_commodity[i] is not None:
                        sql = 'insert into commodity_rate (`特殊商品`,`供应商_rate`,`二级分类`,`一级分类`,`rate`) values(%s,%s,%s,%s,%s)'
                        val = (rate_commodity[i], rate_provider[i], rate_sort2[i], rate_sort1[i], rate[i])
                        mycursor.execute(sql, val)
                        mydb.commit()
                    elif rate_provider[i] is not None:
                        sql = 'insert into commodity_rate (`供应商_rate`,`二级分类`,`一级分类`,`rate`) values(%s,%s,%s,%s)'
                        val = (rate_provider[i], rate_sort2[i], rate_sort1[i], rate[i])
                        mycursor.execute(sql, val)
                        mydb.commit()
                    elif rate_sort2[i] is not None:
                        sql = 'insert into commodity_rate (`二级分类`,`一级分类`,`rate`) values(%s,%s,%s)'
                        val = (rate_sort2[i], rate_sort1[i], rate[i])
                        mycursor.execute(sql, val)
                        mydb.commit()
                    elif rate_sort1[i] is not None:
                        sql = 'insert into commodity_rate (`一级分类`,`rate`) values(%s,%s)'
                        val = (rate_sort1[i], rate[i])
                        mycursor.execute(sql, val)
                        mydb.commit()
            else:
                print('加价率刷新失败！')
            # 更新AB类
            for i in range(len(foreign_id)):
                sql = 'UPDATE commodity_price SET `销售价`=%s,`源头采购价`=%s ,`平台进货价`=%s where foreign_id = %s'
                if price_AB[i] is not None: #处理AB类商品有售价的
                    if type[i] == "A" or type[i] == "B":
                        val = (price_AB[i], price_source[i], price_buy[i],foreign_id[i])
                        mycursor.execute(sql, val)
                        mydb.commit()

            #更新C类
            for i in range(len(foreign_id)):
                if type[i] == "C":
                    sql = 'UPDATE commodity_price SET `销售价`=%s,`平台进货价`=%s,`源头采购价`=%s where foreign_id = %s'
                    if price_C0[i] is not None: #处理C0
                        val = (price_C0[i],price_buy[i],price_source[i],foreign_id[i])
                        mycursor.execute(sql,val)
                        mydb.commit()
                    elif in_price_C4[i] is not None:#处理C4
                        rate_mid = 0
                        for j in range(len(rate)):
                            if rate_commodity[j] is not None:
                                if rate_commodity[j] == name_ping[i] and name_ping[i] is not None:
                                    rate_mid = rate[j]
                            elif rate_provider[j] is not None:
                                if rate_provider[j] == provider[i] and provider[i] is not None:
                                    rate_mid = rate[j]
                            elif rate_sort2[j] is not None:
                                if rate_sort2[j] == sort2[i] and sort2[i] is not None:
                                    rate_mid = rate[j]
                            elif rate_sort1[j] is not None:
                                if rate_sort1[j] == sort1[i] and sort1[i] is not None:
                                    rate_mid = rate[j]
                        if rate_mid == 0:
                            print(name_ping[i], '该商品无加价率！')
                        else:
                            val = (float(in_price_C4[i]) * (float(rate_mid) + 1) * 1.05, price_buy[i],price_source[i], foreign_id[i])
                            mycursor.execute(sql, val)
                            mydb.commit()
                    elif in_price_C1[i] is not None:#处理C1
                        rate_mid = 0
                        for j in range(len(rate)):
                            if rate_commodity[j] is not None:
                                if rate_commodity[j] == name_ping[i] and name_ping[i] is not None:
                                    rate_mid = rate[j]
                            elif rate_provider[j] is not None:
                                if rate_provider[j] == provider[i] and provider[i] is not None:
                                    rate_mid = rate[j]
                            elif rate_sort2[j] is not None:
                                if rate_sort2[j] == sort2[i] and sort2[i] is not None:
                                    rate_mid = rate[j]
                            elif rate_sort1[j] is not None:
                                if rate_sort1[j] == sort1[i] and sort1[i] is not None:
                                    rate_mid = rate[j]
                        if rate_mid == 0:
                            print(name_ping[i], '该商品无加价率！')
                        else:
                            val = (float(in_price_C1[i]) * (float(rate_mid) + 1) * 1.05, price_buy[i],price_source[i], foreign_id[i])
                            mycursor.execute(sql, val)
                            mydb.commit()
                    elif in_price_C2[i] is not None:#处理C2
                        rate_mid = 0
                        for j in range(len(rate)):
                            if rate_commodity[j] is not None:
                                if rate_commodity[j] == name_ping[i] and name_ping[i] is not None:
                                    rate_mid = rate[j]
                            elif rate_provider[j] is not None:
                                if rate_provider[j] == provider[i] and provider[i] is not None:
                                    rate_mid = rate[j]
                            elif rate_sort2[j] is not None:
                                if rate_sort2[j] == sort2[i] and sort2[i] is not None:
                                    rate_mid = rate[j]
                            elif rate_sort1[j] is not None:
                                if rate_sort1[j] == sort1[i] and sort1[i] is not None:
                                    rate_mid = rate[j]
                        if rate_mid == 0:
                            print(name_ping[i], '该商品无加价率！')
                        else:
                            val = (float(in_price_C2[i]) * (float(rate_mid) + 1) * 1.05, price_buy[i],price_source[i], foreign_id[i])
                            mycursor.execute(sql, val)
                            mydb.commit()
                    elif in_price_C3[i] is not None:#处理C3
                        rate_mid = 0
                        for j in range(len(rate)):
                            if rate_commodity[j] is not None:
                                if rate_commodity[j] == name_ping[i] and name_ping[i] is not None:
                                    rate_mid = rate[j]
                            elif rate_provider[j] is not None:
                                if rate_provider[j] == provider[i] and provider[i] is not None:
                                    rate_mid = rate[j]
                            elif rate_sort2[j] is not None:
                                if rate_sort2[j] == sort2[i] and sort2[i] is not None:
                                    rate_mid = rate[j]
                            elif rate_sort1[j] is not None:
                                if rate_sort1[j] == sort1[i] and sort1[i] is not None:
                                    rate_mid = rate[j]
                        if rate_mid == 0:
                            print(name_ping[i], '该商品无加价率！')
                        else:
                            val = (float(in_price_C3[i]) * (float(rate_mid) + 1) * 1.05, price_buy[i],price_source[i], foreign_id[i])
                            mycursor.execute(sql, val)
                            mydb.commit()
                    else:
                        print(name_ping[i],'该商品刷新价格失败！')
        except KeyError:
            print('表中列名请与模板中的列名一致！重新运行！')
        except FileNotFoundError:
            print('没有选择文件！重新运行!')
        except:
            print('有错误！重新运行！')
            time.sleep(3)
            exit()

    elif index == '2':
        foreign_id_out = []
        sort1_out = []
        sort2_out = []
        name_ping_out = []
        unit_out = []
        type_out = []
        price_source_out = []
        price_buy_out = []
        price_out = []
        sql = 'SELECT commodity.`foreign_id`,commodity.`一级分类`,commodity.`二级分类`,commodity.`商品名称`,commodity.`单位`,commodity.`类型`,' \
              'commodity_price.`源头采购价`,commodity_price.`平台进货价`,commodity_price.`销售价` FROM `commodity` INNER JOIN commodity_price ON commodity.foreign_id = commodity_price.foreign_id'
        mycursor.execute(sql)
        data = mycursor.fetchall()
        for i in range(len(data)):
            foreign_id_out.append(data[i][0])
            sort1_out.append(data[i][1])
            sort2_out.append(data[i][2])
            name_ping_out.append(data[i][3])
            unit_out.append(data[i][4])
            type_out.append(data[i][5])
            price_source_out.append(data[i][6])
            price_buy_out.append(data[i][7])
            price_out.append(data[i][8])
        print('请输入保存的路径 (. 保存该文件路径下)')
        file_out = input('')
        if file_out is None:
            print('路径未输入！')
        else:
            workbook = openpyxl.Workbook()
            worksheet = workbook.active
            workbook.save(file_out+"/商品信息.xlsx")
            workbook = openpyxl.load_workbook(file_out+"/商品信息.xlsx")
            sheet = workbook['Sheet']
            sheet['A1'] = '商品id'
            sheet['B1'] = '一级分类'
            sheet['C1'] = '二级分类'
            sheet['D1'] = '商品名称'
            sheet['E1'] = '单位'
            sheet['F1'] = '类别'
            sheet['G1'] = '源头采购价'
            sheet['H1'] = '平台进货价'
            sheet['I1'] = '售价'
            num = 2
            for i in range(len(foreign_id_out)):
                sheet['A' + str(num)] = foreign_id_out[i]
                sheet['B' + str(num)] = sort1_out[i]
                sheet['C' + str(num)] = sort2_out[i]
                sheet['D' + str(num)] = name_ping_out[i]
                sheet['E' + str(num)] = unit_out[i]
                sheet['F' + str(num)] = type_out[i]
                sheet['G' + str(num)] = price_source_out[i]
                sheet['H' + str(num)] = price_buy_out[i]
                sheet['I' + str(num)] = price_out[i]
                num += 1
            workbook.save(file_out+"/商品信息.xlsx")
    elif index == '3':
        #sum1 = 0
        sum1 = input('1.商品表 2.加价率表 3.价格表')
        if sum1 == '1':
            sql = 'select * from commodity'
            # 创建数据库引擎
            engine = create_engine("mysql+pymysql://root:123456@localhost/list")

            # 从数据库中获取数据
            dataframe = pd.read_sql_query(sql, engine)

            file_out = input('请输入保存路径')
            # 保存为Excel文件
            dataframe.to_excel(file_out+'/商品表.xlsx', index=False)
        elif sum1 == '2':
            sql = 'select * from commodity_rate'
            # 创建数据库引擎
            engine = create_engine("mysql+pymysql://root:123456@localhost/list")

            # 从数据库中获取数据
            dataframe = pd.read_sql_query(sql, engine)

            file_out = input('请输入保存路径')
            # 保存为Excel文件
            dataframe.to_excel(file_out + '/加价率表.xlsx', index=False)
        elif sum1 == '3':
            sql = 'select * from commodity_price'
            # 创建数据库引擎
            engine = create_engine("mysql+pymysql://root:123456@localhost/list")

            # 从数据库中获取数据
            dataframe = pd.read_sql_query(sql, engine)

            file_out = input('请输入保存路径')
            # 保存为Excel文件
            dataframe.to_excel(file_out + '/商品价格表.xlsx', index=False)

    elif index == '0':
        exit()
    else:
        print('输入的选项错误！重新输入！')

























