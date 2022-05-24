# Carregando os dados e juntando os arquivos

import pandas as pd
targets = ['red', 'white']
df_list = []
df = pd.DataFrame()
for target in targets:
    df_temp = pd.read_csv(f"D:/Dropbox/IFAL-SI/8_Periodo/Sistemas Inteligentes/intelligent-systems/aprendizagem_de_maquina/classificacao/winequality-{target}.csv", sep=';')
    df_temp['target'] = target
    df_list.append(df_temp)
    print(df_temp.shape)
df = pd.concat([df_list[0], df_list[1]])

print(df)

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

# Puts 0 or 1 for each category
def transform_categorical(data):
    categories = (data.dtypes =="object")
    cat_cols = list(categories[categories].index)
    label_encoder = LabelEncoder()
    for col in cat_cols:
        data[col] = label_encoder.fit_transform(data[col])

# This estimator scales and translates each feature individually such that 
# it is in the given range on the training set, e.g. between zero and one.
def scale_numerical(data):
    scaler = MinMaxScaler()
    data[data.columns] = scaler.fit_transform(data[data.columns])

# Classification: Red or White wine

from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from matplotlib import pyplot as plt

X = df.drop("target", axis = 1)
y = df["target"]

transform_categorical(X)
scale_numerical(X)

print(X)

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

print(X_train)

# Entendendo as métricas
# https://medium.com/@mateuspdua/machine-learning-métricas-de-avaliação-acurácia-precisão-e-recall-d44c72307959

def run_experiment(model):
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    #plot_confusion_matrix(model, X_test, y_test, cmap='GnBu')
    #plt.show()
    print('Precision: %.3f' % precision_score(y_test, y_pred))
    print('Recall: %.3f' % recall_score(y_test, y_pred))
    print('F1: %.3f' % f1_score(y_test, y_pred))
    print('Accuracy: %.3f' % accuracy_score(y_test, y_pred))

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
run_experiment(model)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
run_experiment(model)
