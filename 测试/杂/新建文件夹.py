import os

with open(r'品牌.txt', 'r',encoding='utf-8') as f:
    pin = f.readlines()
pin_stripped = [line.strip() for line in pin]
brand=[]#品牌名
for i in pin_stripped:
    brand.append(i)
for i in brand:
    if i not in brand:
        brand.append(i)
for i in range(len(brand)):
    os.mkdir('F:/工作台/python工作台-pycharm/prodect1/venv/src/测试/杂/'+brand[i])


