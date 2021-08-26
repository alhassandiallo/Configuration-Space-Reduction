import tensorflow.keras as keras
import tensorflow as tf 
import numpy as np
import json
from sklearn.model_selection import train_test_split
from Classifier_CNN import Classifier_CNN
import sklearn
import time


version = 'v2'  # v1, v2

total_samples = 16000 if version == 'v2' else 1000  
test_sizes = [0.9, 0.7, 0.5, 0.3]  


        
models = {
    'v1': {
        'packet_loss': {
            'model': Classifier_CNN(input_shape = (65, 1))
        },
        'latency': {
            'model': Classifier_CNN(input_shape = (65, 1))
        }
    },
    'v2': {
        'packet_loss': {
            'model': Classifier_CNN(input_shape = (162, 1))
        },
        'latency': {
            'model': Classifier_CNN(input_shape = (162, 1))
        }
    }
}

results = []

for dataset_name, dataset in [
    ('packet_loss', json.load(open('data/dataset/' + version + '/packet_loss.json'))),
    ('latency', json.load(open('data/dataset/' + version + '/latency.json'))),
]:
    start_time = time.time()
    accuracy = []
    training_samples = []
    features = np.asarray(list(dataset['features'][:total_samples]))
    labels = np.asarray(list(dataset['labels'][:total_samples]))


    model = models[version][dataset_name]['model']

    #nb_classes = len(np.unique(labels))

    enc = sklearn.preprocessing.OneHotEncoder(categories = 'auto')
    enc.fit(labels.reshape(-1, 1))
    labels = enc.transform(labels.reshape(-1, 1)).toarray()

    features = features.reshape((features.shape[0], features.shape[1], 1))

    for test_size in test_sizes:
        training_features, testing_features, training_labels, testing_labels = train_test_split(
            features,
            labels,
            test_size=test_size,
            random_state=1,
        )

        training_samples.append(len(training_labels))


        model.fit(training_features, training_labels, testing_features, testing_labels)
        score = model.score(testing_features, testing_labels)

        accuracy.append(score)

    model.save(version, dataset_name)

    end_time = time.time() - start_time

    print({
        'version': version,
        'dataset': dataset_name,
        'accuracy': accuracy,
        'training_samples': training_samples,
        'total_samples': total_samples,
        'execution_time_in_sec': end_time
    })

    results.append({
        'target': dataset_name,
        'accuracy': accuracy,
        'training_samples': training_samples,
        'total_samples': total_samples,
        'execution_time_in_sec': end_time
    })

with open('data/training_selection/#' + version + '_training_selection.json', 'w') as f:
    json.dump(results, f, indent=2)
        
        

    


    
        