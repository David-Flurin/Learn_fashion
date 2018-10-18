import tensorflow as tf 
import numpy as np
import cv2

classes=10

(x_train, y_train),(x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
dimensions = x_train.shape
x_train = np.reshape(x_train, (dimensions + (1,)))

model = tf.keras.models.Sequential([
	tf.keras.layers.Conv2D(input_shape=(28,28,1), activation='relu', filters=5, padding='same', kernel_size=(3,3)),
	tf.keras.layers.Conv2D(activation='relu', filters=5, padding='same', kernel_size=(3,3)),	
	tf.keras.layers.MaxPool2D(pool_size=(2)),
	tf.keras.layers.Conv2D(activation='relu',filters=5, padding='same', kernel_size=(3,3)),
	tf.keras.layers.Conv2D(activation='relu',filters=5, padding='same', kernel_size=(3,3)),
	tf.keras.layers.MaxPool2D(pool_size=(2)),
	tf.keras.layers.Flatten(),
	tf.keras.layers.Dense(245,activation='relu'),
	tf.keras.layers.Dropout(0.2),
	#tf.keras.layers.Dense(980,activation='relu'),
	#tf.keras.layers.Dense(1280,activation='relu'),	
	#tf.keras.layers.Dropout(0.5),
	tf.keras.layers.Dense(classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
#tensorboard = TensorBoard(log_dir='c:/temp/tensorboard/run1', histogram_freq=1, write_graph=True, write_images=False)
model.fit(x_train, y_train, epochs=50, batch_size=32)
model.summary()

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")