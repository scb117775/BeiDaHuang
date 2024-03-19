# -*- codeing = utf-8 -*-
# @Project :prodect
# @File    :B2015 计算并联电阻的阻值.py
# @IDE     :PyCharm
# @Author  :孙崇博
# @Date    :2024/2/22 15:33


num = input().split()
a = int(num[0])
b = int(num[1])
c = a*b/(a+b)
print("{:.2f}".format(c))