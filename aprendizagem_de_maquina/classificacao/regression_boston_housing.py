from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# Loading the dataset

data=load_boston()
#print(data.DESCR)

# Separating independent and dependent variables

boston=pd.DataFrame(data["data"],columns=data["feature_names"])
boston.head()
prices=pd.DataFrame(data["target"],columns=["price"])
prices.head()

print(prices.head(1))
#print(boston.head(1))

# Splitting the training and test datasets

X_train,X_test,y_train,y_test=train_test_split(boston,prices)
print("Train Data Size:",X_train.size)
print("Test Data Size:",X_test.size)

# Creating the model

model=LinearRegression()
model.fit(X_train,y_train)
print(model)

# Predicting a house price

data = {'CRIM': [0.00632], 'ZN': [18.0], 'INDUS': [2.31], 'CHAS': [0.0], 'NOX': [0.538],
        'RM': [6.575], 'AGE': [65.2], 'DIS': [4.0900], 'RAD': [1.0], 'TAX': [296.0],
        'PTRATIO': [15.3], 'B': [396.90], 'LSTAT': [4.98]}

df = pd.DataFrame(data)
result = model.predict(df)
print(result)

result = model.predict(X_test)
print(result)

# Validação do modelo

from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error
import numpy as np

print("R^2 : ", r2_score(y_test, result))
print("MAE :", mean_absolute_error(y_test,result))
print("RMSE:",np.sqrt(mean_squared_error(y_test, result)))