import pandas as pd
import mysql.connector #mysql 库
import numpy as np

# 连接到MySQL数据库
mydb = mysql.connector.connect(
  host="192.168.112.78",
  port="3306",
  user="root",
  password="123456",
  database="list"
)
my_cursor = mydb.cursor(buffered=True)

sql = "SELECT commodity.foreign_id 商品ID,commodity.`一级分类`,commodity.`二级分类`,commodity.`商品名称`,commodity.`单位`,commodity_price.`类型` 类别, " \
      "commodity_price.`源头采购价`,commodity_price.`平台进货价`,commodity_price.`售价` FROM commodity " \
      "INNER JOIN commodity_price ON commodity.foreign_id = commodity_price.foreign_id"
my_cursor.execute(sql)
result = my_cursor.fetchall()
# 将数据转换为pandas DataFrame
df = pd.DataFrame(result, columns=[i[0] for i in my_cursor.description])
try:
  print('请输入保存路径(. 保存到程序同级路径)')
  file_out_path = input()
  df.to_excel(file_out_path + "/数据库商品表.xlsx", index=False)
except OSError:
  print('文件路径错误')

my_cursor.close()

