from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# Loading the dataset

data=load_boston()
print(data.DESCR)

# Separating independent and dependent variables

boston=pd.DataFrame(data["data"],columns=data["feature_names"])
boston.head()
prices=pd.DataFrame(data["target"],columns=["price"])
prices.head()

# Decomentar essa linha apenas para geração dos gráficos
boston['MEDV'] = data["target"]

#print(prices.head(1))
print(boston.head(1))

# Distribution of the target variable

prices.hist()

# Verificando os tipos de dados das variáveis independentes

boston.info()

# Verificando os tipos de dados

boston.nunique()

# Plotting multiple bar charts at once for categorical variables
# Since there is no default function which can plot bar charts for multiple columns at once
# we are defining our own function for the same

def PlotBarCharts(inpData, colsToPlot):
    %matplotlib inline
    
    import matplotlib.pyplot as plt
    
    # Generating multiple subplots
    fig, subPlot=plt.subplots(nrows=1, ncols=len(colsToPlot), figsize=(20,5))
    fig.suptitle('Bar charts of: '+ str(colsToPlot))

    for colName, plotNumber in zip(colsToPlot, range(len(colsToPlot))):
        inpData.groupby(colName).size().plot(kind='bar',ax=subPlot[plotNumber])

# Calling the function
PlotBarCharts(inpData=boston, colsToPlot=['CHAS','RAD'])

# Plotting histograms of multiple columns together
boston.hist(['CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'TAX',
                 'PTRATIO', 'B', 'LSTAT'], figsize=(18,10))

                 # Relationship exploration: Continuous Vs Continuous -- Scatter Charts

ContinuousCols=['CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'TAX',
                 'PTRATIO', 'B', 'LSTAT']

# Plotting scatter chart for each predictor vs the target variable
for predictor in ContinuousCols:
    boston.plot.scatter(x=predictor, y='MEDV', figsize=(10,5), title=predictor+" VS "+ 'MEDV')

# Calculating correlation matrix
ContinuousCols=['MEDV','CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'TAX',
                 'PTRATIO', 'B', 'LSTAT']

# Creating the correlation matrix
CorrelationData=boston[ContinuousCols].corr()
CorrelationData

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
#print(result)
print(y_test.price)