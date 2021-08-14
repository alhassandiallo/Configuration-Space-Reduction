import os
import shutil
import tensorflow as tf
import tensorflow.keras as keras
from Classifier_CNN import Classifier_CNN

dir_name = 'model'

models = {
    'v1_packet_loss': Classifier_FCN(input_shape = (65, 1)),
    'v1_latency': Classifier_FCN(input_shape = (65, 1)),

    'v2_packet_loss': Classifier_FCN(input_shape = (162, 1)),
    'v2_latency': Classifier_FCN(input_shape = (162, 1))
}


def get_models(version):
    if version == 'v1':
        return {
            'packet_loss': get_model(version + '_packet_loss'),
            'latency': get_model(version + '_latency'),
        }
    else:
        return {
            'packet_loss': get_model(version + '_packet_loss'),
            'latency': get_model(version + '_latency'),
        }


def save_models(models, version):
    for model_name in models:
        save_model(version + '_' + model_name, models[model_name])


def get_model(model_name):
    
    return models[model_name]


def save_model(model_name, model):
    try:
        tf.keras.models.save_model(model, dir_name + '/' + model_name + '.hdf5')
    except Exception as e:
        print('unable to save model: ' + model_name)

'''
def initialize():
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)

    os.makedirs(dir_name)'''
