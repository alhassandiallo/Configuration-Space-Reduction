import tensorflow.keras as keras
import tensorflow as tf
import numpy as np
import json

from ExplainableModule.integrated_gradients import integrated_gradients, random_baseline_integrated_gradients
from ExplainableModule.predictions_and_gradients import calculate_outputs_and_gradients, top_label_id_and_score
from LearningModule import classification
import sklearn.preprocessing
import sklearn
import time

#version = 'v1'  # v1, v2
directory = 'model'


def attribute1(dataset, version):

    indexes = classification.v1_predicting(dataset, version)

    features = np.asarray(dataset['features'])
    features = features.reshape((features.shape[0], features.shape[1], 1))

    model = tf.keras.models.load_model(directory + '/' + version + '_packet_loss.hdf5')
    
    
    for index in indexes:
        attributions  = integrated_gradients(features[index, :], 
            model, None, calculate_outputs_and_gradients, steps = 50, baseline=None)
        
        if attributions[0:31].max() < 0.0:
           indexes.remove(index)
    
    return {'indexes': indexes}

def attribute2(dataset, version):

    indexes = classification.v2_predicting(dataset, version)

    features = np.asarray(dataset['features'])
    features = features.reshape((features.shape[0], features.shape[1], 1))

    model = tf.keras.models.load_model(directory + '/' + version + '_packet_loss.hdf5')
    
    
    for index in indexes:
        attributions  = integrated_gradients(features[index, :], model, None, calculate_outputs_and_gradients, steps = 50, baseline=None)
        
        if attributions[0:79].max() < 0.0:
          indexes.remove(index)
    
    return {'indexes': indexes}

