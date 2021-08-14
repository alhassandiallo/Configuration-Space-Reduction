import numpy as np
import sklearn
import sklearn.preprocessing
import tensorflow as tf
from ExplainableModule.attributions import attributions

# v1, v2

directory = 'model'


def v1_training(dataset):
    version = 'v1'

    model1 = tf.keras.models.load_model(directory + '/' + version + '_packet_loss.hdf5')
    model2 = tf.keras.models.load_model(directory + '/' + version + '_latency.hdf5')

    features = np.asarray(dataset['features'])
    transformed_features = features.reshape((features.shape[0], features.shape[1], 1))

    for model, target, name in [
        (model1, dataset['packet_loss'], 'packet_loss'),
        (model2, dataset['latency'], 'latency'),
    ]:
        target = np.asarray(dataset[name])
        enc = sklearn.preprocessing.OneHotEncoder(categories='auto')
        enc.fit(target.reshape(-1, 1))
        target = enc.transform(target.reshape(-1, 1)).toarray()

        model.fit(transformed_features, target)

        model.save(version, name)
    return {'message': 'training successful'}


def v1_testing(dataset):
    version = 'v1'

    threshold = 90

    model1 = tf.keras.models.load_model(directory + '/' + version + '_packet_loss.hdf5')
    model2 = tf.keras.models.load_model(directory + '/' + version + '_latency.hdf5')
    features = np.asarray(dataset['features'])
    features = features.reshape((features.shape[0], features.shape[1], 1))
    indexes = [i for i in range(0, len(features))]

    for model, name in [
        (model1, 'packet_loss'),
        (model2, 'latency'),
    ]:
        relevant_features = []
        relevant_indexes = []

        predictions = model.predict(features)

        for index, prediction in enumerate(np.argmax(predictions, axis=1)):
            if prediction == 1:
                relevant_features.append(features[index])
                relevant_indexes.append(indexes[index])

        if len(relevant_features) > 0:
            features = np.array(relevant_features)
            indexes = relevant_indexes
        model.save(version, name)
    
    
    return features, indexes, threshold


def v2_training(dataset):
    version = 'v2'

    model1 = tf.keras.models.load_model(directory + '/' + version + '_packet_loss.hdf5')
    model2 = tf.keras.models.load_model(directory + '/' + version + '_latency.hdf5')

    features = np.asarray(dataset['features'])
    transformed_features = features.reshape((features.shape[0], features.shape[1], 1))

    for model, target, name in [
        (model1, dataset['packet_loss'], 'packet_loss'),
        (model2, dataset['latency'], 'latency'),
    ]:
        target = np.asarray(dataset[name])
        enc = sklearn.preprocessing.OneHotEncoder(categories='auto')
        enc.fit(target.reshape(-1, 1))
        target = enc.transform(target.reshape(-1, 1)).toarray()

        model.fit(transformed_features, target)

        model.save(version, name)
    return {'message': 'training successful'}


def v2_testing(dataset):
    version = 'v2'
    threshold = 90

    model1 = tf.keras.models.load_model(directory + '/' + version + '_packet_loss.hdf5')
    model2 = tf.keras.models.load_model(directory + '/' + version + '_latency.hdf5')
    features = np.asarray(dataset['features'])
    features = features.reshape((features.shape[0], features.shape[1], 1))
    indexes = [i for i in range(0, len(features))]

    for model, name in [
        (model1, 'packet_loss'),
        (model2, 'latency'),
    ]:
        relevant_features = []
        relevant_indexes = []

        predictions = model.predict(features)

        for index, prediction in enumerate(np.argmax(predictions, axis=1)):
            if prediction == 1:
                relevant_features.append(features[index])
                relevant_indexes.append(indexes[index])

        if len(relevant_features) > 0:
            features = np.array(relevant_features)
            indexes = relevant_indexes

        model.save(version, name)
    
    return features, indexes, threshold
