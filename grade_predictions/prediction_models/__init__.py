from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree

iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data,
                                                    iris.target,
                                                    test_size=0.3,
                                                    random_state=30)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))
print(clf.predict(x_test))

features = iris.data
iris_class = iris.target

features_train, features_test, iris_class_train, iris_class_test = train_test_split(features, iris_class,
                                                                                    test_size=0.33, random_state=42)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(features_train)
features_train_scale = scaler.transform(features_train)
features_test_scale = scaler.transform(features_test)

from sklearn.neural_network import MLPClassifier

iterations = 1000
hidden_layers = [10, 10, 10]

mlp = MLPClassifier(hidden_layer_sizes=(hidden_layers), max_iter=iterations)

mlp.fit(features_train_scale, iris_class_train)

predicted = mlp.predict(features_test_scale)
