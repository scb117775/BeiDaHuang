import requests
import time
import os

current_directory = os.getcwd()
current_directory1=current_directory+'/图片/'
current_directory2=current_directory+'/'
os.makedirs(current_directory1, exist_ok=True)
#地址表
with open(r'网址.txt', 'r',encoding='utf-8') as f1:
    line2 = f1.readlines()
#读取名称表
with open(r'名称.txt', 'r',encoding='utf-8') as f:
    line1 = f.readlines()
#读取品牌表
with open(r'品牌.txt', 'r',encoding='utf-8') as f:
    pin = f.readlines()

line1_stripped1 = [line.strip() for line in line1]
line2_stripped = [line.strip() for line in line2]
pin_stripped = [line.strip() for line in pin]
line1_stripped2 = [line.replace('/','') for line in line1_stripped1]
line1_stripped3 = [line.replace('*','') for line in line1_stripped2]
line1_stripped4 = [line.replace('|','') for line in line1_stripped3]
line1_stripped = [line.replace(':','') for line in line1_stripped4]

with open (r'id.txt', 'r',encoding='utf-8') as f:
    line3 = f.readlines()
line3_stripped = [line.strip() for line in line3]
brand=[]#品牌名
brand1=[]
count = 0
count = len(line1_stripped)
false_li=[] #下载失败的商品列表
repeat_l=[] #一个商品多个图片
mid_l=[]
for i in pin_stripped:
    brand1.append(i)
for i in brand1:
    if i not in brand:
        brand.append(i)

for i in range(len(brand)):
    os.mkdir(current_directory1+brand[i])

for i in line1_stripped:
    if i in mid_l:
        repeat_l.append(i)
    else:
        mid_l.append(i)

for i in range(0,count):
    try:
        # print(i)
        s = requests.session()
        s.keep_alive = False
        req=requests.get(line2_stripped[i])
        if(req.status_code==200):
            print(str(i+1)+'-'+str(line3_stripped[i])+'-'+line1_stripped[i]+'  已完成!')
            with open(current_directory1+str(pin_stripped[i])+'/'+str(i+1)+'-'+str(line3_stripped[i])+'-'+line1_stripped[i]+'.jpg', "wb") as file:
                file.write(req.content)

        else:
            if (req.status_code == 200):
                print(str(i + 1) + '-' + str(line3_stripped[i]) + '-' + line1_stripped[i] + '  已完成!')
                with open(current_directory1+str(pin_stripped[i])+'/'+str(i + 1) + '-' + str(line3_stripped[i]) + '-' + line1_stripped[i] + '.jpg', "wb") as file:
                    file.write(req.content)
            else:
                print(str(i + 1) + '-' + str(line3_stripped[i]) + '-' + line1_stripped[i] + '  失败!！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
                false_li.appen(line1_stripped[i])
        req.close()  # 关闭，很重要,确保不要过多的链接
    except Exception as e:
        print(str(i + 1) + '-' + str(line3_stripped[i]) + '-' + line1_stripped[i] + '  失败!！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
        false_li.append(str(i + 1) + '-' + str(line3_stripped[i]) + '-' + line1_stripped[i])

with open(current_directory2+'false.txt','w') as f:
    for item in false_li:
        f.write((item+'\n'))










