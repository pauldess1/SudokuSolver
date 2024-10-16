import cv2 
import numpy as np
import matplotlib.pyplot as plt
import os
import tensorflow as tf
import PIL
from utils import show

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics =['accuracy'])

model.fit(x_train, y_train, epochs = 10)
model.save('handwritten_model.keras')



model = tf.keras.models.load_model("handwritten_model.keras")
loss, accuracy = model.evaluate(x_test, y_test)
image = cv2.imread("images/8.PNG")
image = cv2.resize(image,(28,28))
show(image)
image = image[:,:,0]
img = np.invert(np.array([image]))
prediction = np.argmax(model.predict(img))
print(prediction)