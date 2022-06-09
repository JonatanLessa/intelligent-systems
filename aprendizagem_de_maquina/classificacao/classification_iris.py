from matplotlib import cm
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
#print(iris)
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
#print(iris_df)
iris_df['target'] = iris.target
#print(iris_df.head())
iris_df['target names'] = pd.Categorical.from_codes(iris.target, iris.target_names)
print(iris_df.head())
#print(iris_df)
#iris.target[[10, 25, 50]] 

#list(iris.target_names)
#print(iris.target_names)
#%matplotlib inline flag para plotagem no notebook
iris_df.plot.scatter('sepal length (cm)', 'sepal width (cm)', c='target', cmap = cm.Set1)
plt.show()

#iris.data # features, características do dado
#iris.target # rótulo, coluna que se quer prever para os dados de teste
X,y = load_iris(return_X_y=True)
#print(X) # features, características do dado
#print(y) # rótulo, coluna que se quer prever para os dados de teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(X_train.shape)
print(X_test.shape)