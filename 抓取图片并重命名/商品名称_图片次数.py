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

line1_stripped1 = [line.strip() for line in line1]
line2_stripped = [line.strip() for line in line2]
line1_stripped2 = [line.replace('/','') for line in line1_stripped1]
line1_stripped3 = [line.replace('*','') for line in line1_stripped2]
line1_stripped4 = [line.replace('|','') for line in line1_stripped3]
line1_stripped = [line.replace(':','') for line in line1_stripped4]

# with open (r'id.txt', 'r',encoding='utf-8') as f:
#     line3 = f.readlines()
# line3_stripped = [line.strip() for line in line3]

count = len(line1_stripped)
false_l=[] #下载失败的商品列表
exist_l=[] #下载好的商品图片加入
name_mid = ''
for i in range(0,count):
    try:
        s = requests.session()
        s.keep_alive = False
        req=requests.get(line2_stripped[i])
        if req.status_code==200:
            name_mid = line1_stripped[i]+'_1'
            if name_mid not in exist_l: # 1不存在
                print(current_directory1 + name_mid+'  已完成!')
                with open(current_directory1+name_mid+'.jpg', "wb") as file:
                    file.write(req.content)
                exist_l.append(name_mid)
            else:#_1存在
                name_mid = line1_stripped[i]+'_2'
                if name_mid not in exist_l: #2不存在
                    print(current_directory1 + name_mid + '  已完成!')
                    with open(current_directory1 + name_mid + '.jpg', "wb") as file:
                        file.write(req.content)
                    exist_l.append(name_mid)
                else:# 2存在
                    name_mid = line1_stripped[i]+'_3'
                    if name_mid not in exist_l:#3不存在
                        print(current_directory1 + name_mid + '  已完成!')
                        with open(current_directory1 + name_mid + '.jpg', "wb") as file:
                            file.write(req.content)
                        exist_l.append(name_mid)
                    else:#3存在
                        name_mid = line1_stripped[i]+'_4'
                        if name_mid not in exist_l:#4不存在
                            print(current_directory1 + name_mid + '  已完成!')
                            with open(current_directory1 + name_mid + '.jpg', "wb") as file:
                                file.write(req.content)
                            exist_l.append(name_mid)
                        else:#4存在
                            name_mid = line1_stripped[i]+'_5'
                            if name_mid not in exist_l:#5不存在
                                print(current_directory1 + name_mid + '  已完成!')
                                with open(current_directory1 + name_mid + '.jpg', "wb") as file:
                                    file.write(req.content)
                                exist_l.append(name_mid)
                            else:#5存在
                                name_mid = line1_stripped[i]+'_6'
                                if name_mid not in exist_l:#6不存在
                                    print(current_directory1 + name_mid + '  已完成!')
                                    with open(current_directory1 + name_mid + '.jpg', "wb") as file:
                                        file.write(req.content)
                                    exist_l.append(name_mid)
                                else:#6存在
                                    name_mid = line1_stripped[i]+'_7'
                                    if name_mid not in exist_l:  # 7不存在
                                        print(current_directory1 + name_mid + '  已完成!')
                                        with open(current_directory1 + name_mid + '.jpg', "wb") as file:
                                            file.write(req.content)
                                        exist_l.append(name_mid)
                                    else:#7存在
                                        name_mid = line1_stripped[i]+'_8'
                                        if name_mid not in exist_l:  # 8不存在
                                            print(current_directory1 + name_mid + '  已完成!')
                                            with open(current_directory1 + name_mid + '.jpg', "wb") as file:
                                                file.write(req.content)
                                            exist_l.append(name_mid)
                                        else:#8存在
                                            name_mid = line1_stripped[i] + '_9'
                                            if name_mid not in exist_l:  # 9不存在
                                                print(current_directory1 + name_mid + '  已完成!')
                                                with open(current_directory1 + name_mid + '.jpg', "wb") as file:
                                                    file.write(req.content)
                                                exist_l.append(name_mid)
                                            else:#9存在
                                                name_mid = line1_stripped[i] + '_10'
                                                if name_mid not in exist_l:  # 10不存在
                                                    print(current_directory1 + name_mid + '  已完成!')
                                                    with open(current_directory1 + name_mid + '.jpg', "wb") as file:
                                                        file.write(req.content)
                                                    exist_l.append(name_mid)
                                                else:
                                                    false_l.append(1)
        else:
            false_l.append(line1_stripped[i])
        req.close()  # 关闭，很重要,确保不要过多的链接
    except Exception as e:
        print(name_mid + '  失败!！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
        false_l.append(name_mid)

with open(current_directory2+'false.txt','w') as f:
    for item in false_l:
        f.write((item+'\n'))










