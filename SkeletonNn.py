from keras import models
import keras
from keras.models import Sequential

model = Sequential()
model.add(keras.layers.Dense(12, input_dim=X, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# train_x, train_y, test_x, test_y = imported data
# imported dataset will be X coloumns of independent variables such as speed, terrain roughness, angle of elevation, torque etc
# last 1(Y) coloumn will be fuel efficieny/ whatever output is required calucalted manually, after fitting the model, the predicted output will give exact fuel efficiency 
# for any variation in the first X columns

model.fit(train_x, train_y, epochs=5)

tested_y = model.predict(test_x)

import matplotlib.pyplot as plt

plt.plot(tested_y, test_y)
plt.show()