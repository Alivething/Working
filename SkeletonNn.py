
import keras
from keras.backend import argmax
from keras.models import Sequential

import pandas as pd
from pandas.core.construction import array

model = Sequential()
model.add(keras.layers.Dense(12, input_dim=3, activation='relu'))
model.add(keras.layers.Dense(3, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

dataset = pd.read_csv("red.csv")


X = dataset[['n1', 'n2', 'n3']]
Y = dataset[['colour']]

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical

ohe = OneHotEncoder(sparse=False)
le = LabelEncoder()


Y1 = le.fit_transform(Y)
Y1 = array(Y1)
Y2 = to_categorical(Y1)


print(Y1)
print(Y2[0])
print(Y2[1])

model.fit(X, Y2, epochs=3000, verbose=0)
y = model.predict([[50,45,70]])
print(y)
