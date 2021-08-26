import json
import operator
import time
import numpy as np
import keras
import sklearn

from keras.wrappers.scikit_learn import KerasClassifier


from sklearn.model_selection import ParameterGrid, train_test_split, GridSearchCV



version = 'v2'  # change version here -> v1, v2


def create_model(input_shape, nb_classes, filters=6, kernel_size=7, pool_size=3, activation='sigmoid'):
    padding = 'valid'
    input_layer = keras.layers.Input(input_shape)

    conv1 = keras.layers.Conv1D(filters=filters,kernel_size=kernel_size,padding=padding,activation=activation)(input_layer)
    conv1 = keras.layers.AveragePooling1D(pool_size=pool_size)(conv1)

    conv2 = keras.layers.Conv1D(filters=filters,kernel_size=kernel_size,padding=padding,activation=activation)(conv1)
    conv2 = keras.layers.AveragePooling1D(pool_size=pool_size)(conv2)

    flatten_layer = keras.layers.Flatten()(conv2)

    output_layer = keras.layers.Dense(units=nb_classes,activation=activation)(flatten_layer)

    model = keras.models.Model(inputs=input_layer, outputs=output_layer)

    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    return model


testing_samples = 1000  



for dataset_name, dataset in [
    ('packet_loss', json.load(open('data/dataset/' + version + '/packet_loss.json'))),
    ('latency', json.load(open('data/dataset/' + version + '/latency.json'))),
]:
    start_time = time.time()

    result = []
    features = np.asarray(list(dataset['features'][:testing_samples]))
    labels = np.asarray(list(dataset['labels'][:testing_samples]))
    dataset = None  # save runtime memory

   
    nb_classes = len(np.unique(labels))

    enc = sklearn.preprocessing.OneHotEncoder(categories = 'auto')
    enc.fit(labels.reshape(-1, 1))
    labels = enc.transform(labels.reshape(-1, 1)).toarray()
    features = features.reshape((features.shape[0], features.shape[1], 1))

    input_shape = features.shape[1:]
        
    model = KerasClassifier(build_fn=create_model, nb_classes=nb_classes, input_shape=input_shape, verbose=0)

    filters=[6, 12, 64]
    kernel_size=[3, 5, 7]
    batch_size=[12, 16]
    pool_size=[2, 3]
    epochs=[10, 15, 20]
    activation=['sigmoid', 'relu', 'softmax']

    param_grid = dict(
        filters=filters,
        kernel_size=kernel_size,
        batch_size=batch_size,
        pool_size=pool_size,
        epochs=epochs,
        activation=activation
    )
    grid = GridSearchCV(estimator = model, param_grid=param_grid, n_jobs = -1, cv=5)
    grid_result = grid.fit(features, labels)

    print(dataset_name+" "+version+"Best: %f using %s" %(grid_result.best_score_, grid_result.best_params_))


    end_time = time.time() - start_time

    
