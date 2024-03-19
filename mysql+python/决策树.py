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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=30)
clf = DecisionTreeClassifier(criterion="gini",
                             max_depth=4,
                             # max_leaf_nodes=max_leaf_nodes,
                             # min_samples_split=min_samples_split,
                             # min_samples_leaf=min_samples_leaf
                             )  # 限制树的最大深度为3
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
scores = cross_val_score(clf, X_train, y_train,
                         cv=9
                         )  # 使用交叉验证
print(max(scores))

