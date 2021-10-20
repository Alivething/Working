import keras
from numpy import array
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers.core import Activation, Dropout, Dense
from keras.layers import Flatten, LSTM
from keras.layers import GlobalMaxPooling1D
from keras.models import Model
from keras.layers.embeddings import Embedding
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.layers import Input
from keras.layers.merge import Concatenate
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

data = pd.read_csv("MissonEd.csv")
labels = data[['SoftwareWeb', 'Data Science', 'Human Resource', 'SocMeMarketing']]

print(data.shape)

# fig_size = plt.rcParams["figure.figsize"]
# fig_size[0] = 10
# fig_size[1] = 8
# plt.rcParams["figure.figsize"] = fig_size

# labels.sum(axis=0).plot.bar()
# plt.show()

X = []
sentences = list(data["Content"])
for sen in sentences:
    X.append(sen)
print(X)
y = labels.values
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=4)
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(X_train)

# X_train = tokenizer.texts_to_sequences(X_train)
# X_test = tokenizer.texts_to_sequences(X_test)

vocab_size = len(tokenizer.word_index) + 1

maxlen = 200

# X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
# X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)

from numpy import array
from numpy import asarray
from numpy import zeros

embeddings_dictionary = dict()

glove_file = open('glove.6B.100d.txt', encoding="utf8")

for line in glove_file:
    records = line.split()
    word = records[0]
    vector_dimensions = asarray(records[1:], dtype='float32')
    embeddings_dictionary[word] = vector_dimensions
glove_file.close()

embedding_matrix = zeros((vocab_size, 100))
for word, index in tokenizer.word_index.items():
    embedding_vector = embeddings_dictionary.get(word)
    if embedding_vector is not None:
        embedding_matrix[index] = embedding_vector

# deep_inputs = Input(shape=(maxlen,))
# embedding_layer = Embedding(vocab_size, 100, weights=[embedding_matrix], trainable=False)(deep_inputs)
# LSTM_Layer_1 = LSTM(128)(embedding_layer)
# dense_layer_1 = Dense(4, activation='sigmoid')(LSTM_Layer_1)
# model = Model(inputs=deep_inputs, outputs=dense_layer_1)

# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
# print(model.summary())

# history = model.fit(X_train, y_train, batch_size=128, epochs=5, verbose=1, validation_split=0.2)
# score = model.evaluate(X_test, y_test, verbose=1)

# print("Test Score:", score[0])
# print("Test Accuracy:", score[1])

model = keras.models.load_model('missoned1.h5')
 
X = ['Certified data scientist with 12 years of experience for a diverse clientele Achievements include updating data streaming processes for an reduction in redundancy as well as improving the accuracy of predicted prices by 18 Highly skilled in data visualization machine learning leadership']

# maxlen = 200
# tokenizer = Tokenizer(num_words=5000)
# tokenizer.fit_on_texts(X)

X = tokenizer.texts_to_sequences(X)
print(X)
X = pad_sequences(X, padding='post', maxlen=maxlen)
X = array(X)
y =[[1,0,0,0]]

score = model.predict(X)
print(score, y)
