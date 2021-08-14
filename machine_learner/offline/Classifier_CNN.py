# CNN model
# when tuning start with learning rate->mini_batch_size -> 
# momentum-> #hidden_units -> # learning_rate_decay -> #layers 
import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
from sklearn.metrics import accuracy_score
import time 

class Classifier_CNN:
    def __init__(self, input_shape, build = True):
        if build == True:
             self.model = self.build_model(input_shape)
        return


    def build_model(self, input_shape, nb_classes = 2):
        padding = 'valid'
        input_layer = tf.keras.Input(input_shape)

        conv1 = tf.keras.layers.Conv1D(filters=64,kernel_size=7,padding=padding,activation='sigmoid')(input_layer)
        conv1 = tf.keras.layers.AveragePooling1D(pool_size=2)(conv1)

        conv2 = tf.keras.layers.Conv1D(filters=64,kernel_size=7,padding=padding,activation='sigmoid')(conv1)
        conv2 = tf.keras.layers.AveragePooling1D(pool_size=2)(conv2)

        flatten_layer = tf.keras.layers.Flatten()(conv2)

        output_layer = tf.keras.layers.Dense(units=nb_classes,activation='softmax')(flatten_layer)

        model = tf.keras.Model(inputs=input_layer, outputs=output_layer)

        model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(), metrics=['accuracy'])

        return model 

    def fit(self, x_train, y_train, x_val, y_val):
        # x_val and y_val are only used to monitor the test loss and NOT for training  
        batch_size = 12
        nb_epochs = 15

        start_time = time.time()

        self.model.fit(x_train, y_train, batch_size=batch_size, epochs=nb_epochs, validation_data=(x_val,y_val))

        duration = time.time() - start_time

    def save(self, version, dataset_name):
        self.model.save('model/'+version+'_'+dataset_name+'.hdf5')

    def compile(self, loss, optimizer):
        return self.model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy']) 

    def prediction(self, x):
        return self.model.predict(x) 

        #return pred   

    def score(self, x_test, y_true):

        y_pred = self.model.predict(x_test)
        y_pred = np.argmax(y_pred, axis=1)
        y_true = np.argmax(y_true, axis=1)

        return accuracy_score(y_true, y_pred)
        



