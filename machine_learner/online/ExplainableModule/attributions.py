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

version = 'v1'  # v1, v2
directory = 'model'

results = []

attribute = []

def attributions(dataset):

    features, indexes, threshold = classification.v1_testing(dataset)

    indexes = indexes

    model = tf.keras.models.load_model(directory + '/' + version + '_packet_loss.hdf5')
    
    if len(features) < threshold:
        for index in indexes:
            predictions, attributions  = integrated_gradients(features[index, :], model, None, calculate_outputs_and_gradients, steps = 50, baseline=None)
            
            if attributions[0] < 1.21077549e-11:
                attributions[0] = 1.21077549e-1
    
    return {'indexes': indexes}

