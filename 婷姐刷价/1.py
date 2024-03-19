from tkinter import Tk, Button, Label, filedialog
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import mysql.connector
import os

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

#变量定义
name_all=['foreign_id','name_ping','name_new','type','sort1','sort2','brand','specifications',
          'is_base','price_source','price_AB','price_C0','price_C4','in_price_C1','in_price_C2','in_price_C3',
          'rate_sort1','rate_sort2','rate_provider','rate_commodity','rate']
foreign_id = [] #foreign_id
name_ping = [] #商品名称_平台
name_new = [] #商品名称_新
type = [] #类型
sort1 = []  #一级分类
sort2 = []  #二级分类
brand = []  #品牌
specifications = [] #规格
is_base = []  #是否基础单位
price_source = [] #源头采购价
price_AB =[] #AB类售价
price_C0 = [] #C0售价
price_C4 = [] #C4售价
in_price_C1 = [] #C1进货
in_price_C2 = [] #C2进货
in_price_C3 = [] #C3进货
rate_sort1 = [] #rate_一级分类
rate_sort2 = [] #rate_二级分类
rate_provider = [] #供应商
rate_commodity = [] #特殊商品
rate = [] #rate
################################################################################################################
#选择文件的上传路径
file_path = filedialog.askopenfilename()
print('1.上传文件并更新价格  2.显示数据  0.退出')
while True:
  index = input('请输入选项：')
  if index == '1':
    try:
      df = pd.read_excel(open(file_path, 'rb'),dtype = str)
      df = df.astype(object).where(pd.notnull(df), None)
      for index, row in df.iterrows():  # 遍历输入表的每一行数据
        foreign_id.append(row['商品id'])
        name_ping.append(row['商品名称_平台'])
        name_new.append(row['商品名称_新'])
        type.append(row['类型'])
        sort1.append(row['一级分类'])
        sort2.append(row['二级分类'])
        brand.append(row['品牌'])
        specifications.append(row['规格'])
        is_base.append(row['是否基础单位'])
        price_source.append(row['源头采购价'])
        price_AB.append(row['AB类售价'])
        price_C0.append(row['C0售价'])
        price_C4.append(row['C4售价'])
        in_price_C1.append(row['C1进货价'])
        in_price_C2.append(row['C2进货价'])
        in_price_C3.append(row['C3进货价'])
        rate_sort1.append(row['rate_一级分类'])
        rate_sort2.append(row['rate_二级分类'])
        rate_provider.append(row['供应商'])
        rate_commodity.append(row['特殊商品'])
        rate.append(row['rate'])
        #删除数据库中
        sql = 'delete from input_commodity'
        mycursor.execute(sql)
        mydb.commit()
        #将数据写入输入表
        for i in range(len(foreign_id)):
          sql = 'insert  into input_commodity_all (`foreign_id`,`商品名称`,`商品名称_新`,`类型`,`一级分类`,`二级分类`,`品牌`,`规格`,' \
                '`是否基础单位`,`源头采购价`,`AB类售价`,`C0售价`,`C4售价`,`C1进货价`,`C2进货价`,`C3进货价`,' \
                '`一级分类_rate`,`二级分类_rate`,`供应商`,`特殊商品`,`rate`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
          val = (foreign_id[i],name_ping[i], name_new[i], type[i], sort1[i], sort2[i],brand[i], specifications[i],
                 is_base[i],price_source[i], price_AB[i], price_C0[i], price_C4[i], in_price_C1[i],in_price_C2[i],in_price_C3[i],
                 rate_sort1[i],rate_sort2[i],rate_provider[i],rate_commodity[i],rate[i])
          mycursor.execute(sql, val)
        mydb.commit()
        #将数据中商品基本更新商品表
        for i in range(len(foreign_id)):
          sql = 'UPDATE commodity SET `商品名称`=%s,`商品名称_新`=%s,`一级分类`=%s,`二级分类`=%s,`类型`=%s,' \
                '`品牌`=%s,`规格`=%s,`是否基础单位`=%s where `foreign_id` = %s'
          val = (name_ping[i], name_new[i], sort1[i], sort2[i], type[i], brand[i], specifications[i], is_base[i], foreign_id[i])
          mycursor.execute(sql, val)
        mydb.commit()
        #更新加价率
        num1 = 0
        if rate_commodity != None:
          sql = 'insert into commodity_rate_all (`特殊商品`,`供应商`,`二级分类`,`一级分类`,`rate`) values(%s,%s,%s,%s,%s)'
          val = (rate_commodity[i],rate_provider[i],rate_sort2[i],rate_sort1[i],rate[i])
          mycursor.execute(sql, val)
          mydb.commit()
        elif rate_provider != None:
          sql = 'insert into commodity_rate_all (`供应商`,`二级分类`,`一级分类`,`rate`) values(%s,%s,%s,%s)'
          val = (rate_provider[i], rate_sort2[i], rate_sort1[i], rate[i])
          mycursor.execute(sql, val)
          mydb.commit()
        elif rate_sort2 != None:
          sql = 'insert into commodity_rate_all (`二级分类`,`一级分类`,`rate`) values(%s,%s,%s)'
          val = (rate_sort2[i], rate_sort1[i], rate[i])
          mycursor.execute(sql,val)
          mydb.commit()
        elif rate_sort1 != None:
          sql = 'insert into commodity_rate_all (`一级分类`,`rate`) values(%s,%s)'
          val = (rate_sort1[i],rate[i])
          mycursor.execute(sql,val)
          mydb.commit()
        else :
          num1 += 1
          print('加价率刷新错误！')
        if num1 == 0:
          sql = ''
        #更新AB类
        for i in range(len(foreign_id)):
          sql = 'UPDATE commodity_price SET `销售价`=%s,`源头采购价`=%s where foreign_id = %s'
          val = (price_AB[i],price_source[i],foreign_id[i])
          mycursor.execute(sql,val)
          mydb.commit()
        for i in range(len(foreign_id)):
          sql = ''

    except KeyError:
      print('表中列名请与模板中的列名一致！')
  elif index == '2':
    print(2)
  elif index == '0':
    exit()
  else:
    print('输入选项错误,请重新输入!')


