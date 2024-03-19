# -*- codeing = utf-8 -*-
# @Project :prodect
# @File    :B2006 地球人口承载力估计.py
# @IDE     :PyCharm
# @Author  :孙崇博
# @Date    :2024/2/22 14:12

num = input().split()
x = float(num[0])
a = float(num[1])
y = float(num[2])
b = float(num[3])
out = float((b*y-a*x)/(b-a))
print("{:.2f}".format(out))
