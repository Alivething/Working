import cv2
from keras.saving.save import load_model
from tensorflow.keras import datasets, layers, models
import numpy as np

(X_train, y_train), (X_test,y_test) = datasets.cifar10.load_data()

classes = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

def showImage(X, y, index):
    cv2.namedWindow("window", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("window", cv2.resize(X_test[index], [800, 400]))
    print(classes[y[index]])
    cv2.waitKey(0)

y_train = np.squeeze(y_train)
y_test = np.squeeze(y_test)

showImage(X_train, y_train, 12)

# from keras.utils import to_categorical
# y_train = to_categorical(y_train) 
# y_test = to_categorical(y_test)

X_train = X_train/255.0
X_test = X_test/255.0

print(X_train[0].shape)

# model = models.Sequential()
# model.add(layers.Conv2D(32, kernel_size=3, activation='relu', input_shape=(32,32,3)))
# model.add(layers.MaxPooling2D((2,2)))
# model.add(layers.Conv2D(64, kernel_size=3, activation='relu'))
# model.add(layers.MaxPooling2D((2,2)))
# model.add(layers.Flatten())

# model.add(layers.Dense(10, activation='softmax'))

# model.summary()

# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])

# model.fit(X_train, y_train, epochs = 10)

# model.evaluate(X_test, y_test)

model = load_model("imageprocessing/cifar10.h5")

y_pred = model.predict(X_test[20:23])
y_classes = [np.argmax(element) for element in y_pred]
showImage(X_test, y_test, 20)
showImage(X_test, y_test, 21)
showImage(X_test, y_test, 22)
print(y_classes)

# model.save("cifar101.h5")