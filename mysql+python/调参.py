import pymysql
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 建立数据库连接
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='graduate')

data = []
data_mid = []
y = []
# 创建游标
cur = conn.cursor()

# 执行查询语句
cur.execute('SELECT * FROM data')
# 提取查询结果
result = cur.fetchall()

# 关闭游标和数据库连接
cur.close()
conn.close()

# 遍历结果并处理
for row in result:
    # 处理每一行的数据
    data_mid = list(row)
    y.append(data_mid[-1])
    data_mid.pop(-1)
    data.append(data_mid)

X = data
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
score = []
number = 0
for test_size in range(10,40):#40
    test_size = test_size/100 #l1
    for random_state in range(1,35):#l2 50
        for max_depth in range(1,5):#l3
        #     # for max_leaf_nodes in range(2,10):#l4
        #     #     for min_samples_split in range(2,10):#l5
        #     #         for min_samples_leaf in range(1,10):#l6
            for cv in range(5,10):#l7
                try:
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
                    clf = DecisionTreeClassifier(criterion="gini",
                                                 max_depth=max_depth,
                                                 # max_leaf_nodes=max_leaf_nodes,
                                                 # min_samples_split=min_samples_split,
                                                 # min_samples_leaf=min_samples_leaf
                                                 )  # 限制树的最大深度为3
                    clf.fit(X_train, y_train)
                    y_pred = clf.predict(X_test)
                    accuracy = accuracy_score(y_test, y_pred)
                    scores = cross_val_score(clf, X_train, y_train,
                                             cv=cv
                                             # cv=5
                                             )  # 使用交叉验证
                    score.append(max(scores))
                    l1.append(test_size)
                    l2.append(random_state)
                    l3.append(max_depth)
                    l7.append(cv)
                    print(number)
                    number += 1
                except UserWarning:
                    continue
index = 0
score_mid = 0
print(score)
print(type(score))
for i in range(len(score)):
    if score_mid < score[i] :
        score_mid = score[i]
        index = i
print(l1[index])
print(l2[index])
print(l3[index])
print(l7[index])







