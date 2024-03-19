# -*- codeing = utf-8 -*-
# @Project :prodect
# @File    :B2004 对齐输出.py
# @IDE     :PyCharm
# @Author  :孙崇博
# @Date    :2024/2/22 13:49


num = input().split()
a = int(num[0])
b = int(num[1])
c = int(num[2])

print("{:>8} {:>8} {:>8}".format(a, b, c))
