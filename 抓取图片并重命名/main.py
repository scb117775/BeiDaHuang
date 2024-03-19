import requests
import time
#地址表
with open(r'C:\Users\Administrator\Desktop\文件\1\11.8\图片之前\网址.txt', 'r',encoding='utf-8') as f1:
    line2 = f1.readlines()
#读取名称表
with open(r'C:\Users\Administrator\Desktop\文件\1\11.8\图片之前\名称2.0.txt', 'r',encoding='utf-8') as f:
    line1 = f.readlines()

line1_stripped1 = [line.strip() for line in line1]
line2_stripped = [line.strip() for line in line2]
line1_stripped = [line.replace('/','') for line in line1_stripped1]

with open (r'C:\Users\Administrator\Desktop\文件\1\11.8\id.txt', 'r',encoding='utf-8') as f:
    line3 = f.readlines()
line3_stripped = [line.strip() for line in line3]

count = 0
count = len(line1_stripped)
false_li=[] #下载失败的商品列表
repeat_l=[] #一个商品多个图片
mid_l=[]
for i in line1_stripped:
    if i in mid_l:
        repeat_l.append(i)
    else:
        mid_l.append(i)

for i in range(0,count):
    try:
        print(i)
        s = requests.session()
        s.keep_alive = False
        req=requests.get(line2_stripped[i])
        if(req.status_code==200):
            with open(r"C:/Users/Administrator/Desktop/文件/1/11.8/图片/"+str(i+1)+'-'+str(line3_stripped[i])+'-'+line1_stripped[i]+'.jpg', "wb") as file:
                file.write(req.content)

        else:
            with open(r"C:/Users/Administrator/Desktop/文件/1/11.8/图片/"+str(i+1)+'-'+str(line3_stripped[i])+'-'+line1_stripped[i]+'.jpg', "wb") as file:
                file.write(req.content)
            false_li.appen(line1_stripped[i])
        req.close()  # 关闭，很重要,确保不要过多的链接
    except Exception as e:
        false_li.append(line1_stripped[i])

with open(r"C:/Users/Administrator/Desktop/文件/1/11.8/false.txt",'w') as f:
    for item in false_li:
        f.write((item+'\n'))










