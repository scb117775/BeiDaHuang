import random
b=[]
dic = {'鸡腿' : 1,
      '鸡蛋炒面+腊八蒜+果汁' :1,
      '两瓣蒜' : 0,
      '合菜' : 1,
      '疙瘩汤' : 0,
      '自然肉片+红烧茄子米饭' : 0,
      '泡面' : 0,
       '飘香拌面':0,
      'NB麻辣拌' : 2}

for key in dic.keys():
    if dic[key] == 0:
        b.append(key)
print(b[random.randint(0, len(b))-1])
