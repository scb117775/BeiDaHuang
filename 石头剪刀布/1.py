# -*- codeing = utf-8 -*-
# @Project :prodect
# @File    :1.py
# @IDE     :PyCharm
# @Author  :孙崇博
# @Date    :2024/2/22 9:45

import random
dic = {}
dic['1'] = '石头'
dic['2'] = '剪刀'
dic['3'] = '布'
print('1-石头 2-剪刀 3-布')
participant = int(input('请输入'))
if participant == 1 or participant == 2 or participant == 3:
    pass
else:
    print("输入错误")
    exit()
machine = random.randint(1,3)
if machine == 1:
    print('系统出', dic['1'])
    if participant == 1:
        print('平局')
    elif participant == 2:
        print('你输了')
    elif participant == 3:
        print('你赢了')
elif machine == 2:
    print('系统出', dic['2'])
    if participant == 2:
        print('平局')
    elif participant == 1:
        print('你赢了')
    elif participant == 3:
        print('你输了')
elif machine == 3:
    print('系统出', dic['3'])
    if participant == 3:
        print('平局')
    elif participant == 1:
        print('你输了')
    elif participant == 2:
        print('你赢了')



