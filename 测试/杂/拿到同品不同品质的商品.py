name = ['草莓','草莓(精品)','草莓(优质)','西瓜','水蜜桃','蓝莓','蓝莓(精品)','苹果','梨','香蕉','香蕉进口','小白菜(水洗)(优质)','小白菜(水洗)(精品)','小白菜(水洗)']
price = ['1','1.2','1.5','2','3','4','4.2','5','6']
name_same = []
for i in range(len(name)):
    name_same.append(name[i])
    index1 = 0 # 标志有没有name[i]重复
    num_len = len(name[i])
    for j in range(len(name)):
        if i != j: # 不能是他自己
            if len(name[j]) > num_len:# 精品肯定比普通名字长
                index2 = 0  # 标志是不是两个名字相同
                index3 = 0  # 标志有没有括号
                for g in range(num_len):
                    if name[i][g] == name[j][g]:
                        index2 += 1
                if name[j][len(name[j])-1] == ')' or name[j][num_len] == '(' or name[j][len(name[j])-1] == '）' or name[j][num_len] == '（':
                    index3 += 1
                if index2 == num_len and index3 != 0:
                    index1 += 1
                    name_same.append(name[j])
    if index1 == 0:
        name_same.pop()
print(name_same)

