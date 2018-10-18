import tensorflow as tf 
import numpy as np
import read_img as rm
import cv2


class Prediction:

  def __init__(self, path):
    self.path = path
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    self.loaded_model = tf.keras.models.model_from_json(loaded_model_json)
    # load weights into new model
    self.loaded_model.load_weights("model.h5")
    print("Loaded model from disk")

    self.loaded_model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])



    self.clothes = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
            'Sandal/heels', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


  def testset():
    (x_train, y_train),(x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    dimensions = x_test.shape
    #x_test = x_test[1:101,:,:]
    #y_test = y_test[1:101]
    x_test = np.reshape(x_test, (dimensions + (1,)))


    prediction = loaded_model.predict(x_test)
    prediction = np.argmax(np.asarray(prediction), 1)
    #print(y_test)
    faults = 0
    false_shirt = np.zeros(10)
    for i in range(0,len(y_test)):
      if y_test[i] != prediction[i]:
        print(str(y_test[i])+"  "+str(prediction[i]))
        faults += 1
        if y_test[i] == 6:
          false_shirt[prediction[i]] += 1
    print('Accuracy '+str(1-(faults/len(prediction))))
    print(false_shirt)

  def predict_img(self):
    # load json and create model
    
    pred = self.test_image('Server_nodejs/'+self.path)
    return self.clothes[pred]


  def test_image(self,path):
    x_test = rm.load_image(path, 28)
    x_test = 255 - x_test
    cv2.imshow('image',x_test)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    x_test_list = []
    y_test_list = []
    for row in images_test:
      x_test_list.append(row[1:,:])
      y_test_list.append(row[0][0])
    x_test = np.asarray(x_test_list)
    '''
    x_test = x_test/255
    dimensions = x_test.shape
    x_test = np.reshape(x_test, ((1,) + dimensions + (1,)))

    prediction = self.loaded_model.predict(x_test)
    prediction = np.argmax(np.asarray(prediction), 1)
    return prediction[0]



  