
import keras
from keras.backend import argmax, dropout
from keras.models import Sequential
from sklearn.model_selection import train_test_split


import pandas as pd
from pandas.core.construction import array

model = Sequential()
model.add(keras.layers.Dense(12, input_dim=12, activation='relu'))
model.add(keras.layers.Dropout(0.1))
model.add(keras.layers.Dense(64, activation='linear'))
model.add(keras.layers.Dropout(0.1))
model.add(keras.layers.Dense(6, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

print(model.summary())

datasetX = pd.read_csv("wines.csv")
datasetY = pd.read_csv("regions.csv")

X = datasetX[['Body','Sweetness','Smoky','Medicinal','Tobacco','Honey','Spicy','Winey','Nutty','Malty','Fruity','Floral']]
Y = datasetY[['Regions']]


from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical

ohe = OneHotEncoder(sparse=False)
le = LabelEncoder()

Y1 = le.fit_transform(Y)
Y1 = array(Y1)
Y2 = to_categorical(Y1)

print(Y1)

trainX, testX, trainY, testY = train_test_split(X, Y2, test_size=0.2, random_state=1)

history = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=500, verbose=0)

model.save("winemodel.h5")

from matplotlib import pyplot
pyplot.title('Loss / Mean Squared Error')
pyplot.plot(history.history['accuracy'], label='train')
pyplot.plot(history.history['val_accuracy'], label='test')
pyplot.legend()
pyplot.show()

y = model.predict([[2,2,2,0,0,2,1,2,2,2,2,2]])
print(y)
