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

# 特征选择
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier(criterion="entropy")
# clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# 预剪枝处理
clf = DecisionTreeClassifier(criterion="gini",max_depth=3)  # 限制树的最大深度为3
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy with pruning:", accuracy)

# 交叉验证
scores = cross_val_score(clf, X_train, y_train, cv=20)  # 使用交叉验证
print("Cross-validation scores:", scores)
print("Average cross-validation score:", scores.mean())

#0.411666最大








