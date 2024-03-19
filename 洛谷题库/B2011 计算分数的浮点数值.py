# -*- codeing = utf-8 -*-
# @Project :prodect
# @File    :B2011 计算分数的浮点数值.py
# @IDE     :PyCharm
# @Author  :孙崇博
# @Date    :2024/2/22 14:48


num = input().split()
a = int(num[0])
b = int(num[1])
c = a/b
print("{:.9f}".format(c))