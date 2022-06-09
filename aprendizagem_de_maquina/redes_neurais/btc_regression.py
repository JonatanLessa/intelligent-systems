import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('D:/Dropbox/IFAL-SI/8_Periodo/Sistemas Inteligentes/intelligent-systems/aprendizagem_de_maquina/redes_neurais/BTC-USD.csv', date_parser = True)
data.tail()
#print(data)

# Separando o dataset de treinamento e teste
data_training = data[data['Date']< '2021-06-31'].copy()
data_training
print(data_training)

data_test = data[data['Date']>= '2021-06-31'].copy()
data_test
print(data_test)

# Removendo algumas colunas
training_data = data_training.drop(['Date', 'Adj Close'], axis = 1)
training_data.head()

# Normalizando os dados
# #MinMaxScaler is used to normalize the data
scaler = MinMaxScaler()
training_data = scaler.fit_transform(training_data)
training_data

# Criando, compilando, treinando e normalizando o modelo
X_train = [] 
Y_train = []

#len(training_data)
#len(data_test)

for i in range(60, training_data.shape[0]):
  X_train.append(training_data[i-60:i])
  Y_train.append(training_data[i,0])
  
X_train, Y_train = np.array(X_train), np.array(Y_train)
#X_train.shape

#print(len(X_train))  
#print(len(Y_train))

#print(len(training_data[0:60]))
#print(training_data[60,0])

print(len(X_train))
print(len(Y_train))

print(X_train[0])

# Criando o
#from tensorflow.keras import Sequential
#from tensorflow.keras.layers import Dense, LSTM, Dropout
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

#Initialize the RNN
model = Sequential() 
model.add(LSTM(units = 50, activation = 'relu', return_sequences = True, input_shape = (X_train.shape[1], 5)))
model.add(Dropout(0.2)) 
model.add(LSTM(units = 60, activation = 'relu', return_sequences = True))
model.add(Dropout(0.3)) 
model.add(LSTM(units = 80, activation = 'relu', return_sequences = True))
model.add(Dropout(0.4)) 
model.add(LSTM(units = 120, activation = 'relu'))
model.add(Dropout(0.5)) 
model.add(Dense(units =1))
#model.summary()

model.compile(optimizer = 'adam', loss = 'mean_squared_error')
history= model.fit(X_train, Y_train, epochs = 20, batch_size =50, validation_split=0.1)

# Analizando as perdas
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(loss))
plt.figure()
plt.plot(epochs, loss, 'b', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title("Training and Validation Loss")
plt.legend()
plt.show()

# Organizando o dataset de teste
part_60_days = data_training.tail(60)
df= part_60_days.append(data_test, ignore_index = True)
df = df.drop(['Date', 'Adj Close'], axis = 1)
df.head()

inputs = scaler.transform(df)  

X_test = []
Y_test = []
for i in range (60, inputs.shape[0]):
  X_test.append(inputs[i-60:i]) 
  Y_test.append(inputs[i, 0])
  
X_test, Y_test = np.array(X_test), np.array(Y_test) 

#X_test.shape
#Y_test.shape

Y_pred = model.predict(X_test) 

#Y_pred, 
#Y_test
#scaler.scale_

# Voltando resultado para escala normal

#print(Y_test[0] * 19298.903787912797)
#print(Y_pred[0] * 19298.903787912797)

scale = 1/5.18164146e-05
#print(scale)
Y_test = Y_test*scale 
Y_pred = Y_pred*scale
#Y_pred
#Y_test

#print(Y_test)
#print(Y_pred)

formatted_test = Y_test.copy()
#formatted_test = list(map(lambda x:e(x), formatted_test))

formatted_pred = Y_pred.copy()
formatted_pred = list(map(lambda x:(x[0]/10), formatted_pred))

#for i in range(400, 600):
  #print(f'{temp[i]} | {Y_pred[i]}')

formatted_pred = np.array(formatted_pred)

#print(formatted_pred)

#print(formatted_test)

# Plotando as curvas


plt.figure(figsize=(14,5))
plt.plot(formatted_test, color = 'red', label = 'Real Bitcoin Price')   
plt.plot(formatted_pred, color = 'green', label = 'Predicted Bitcoin Price')
plt.ticklabel_format(useOffset=False, style='plain')
plt.title('Bitcoin Price Prediction using RNN-LSTM')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()