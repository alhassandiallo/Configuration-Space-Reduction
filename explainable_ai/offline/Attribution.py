#import tensorflow.keras as keras
import tensorflow as tf
import numpy as np
import json

from integrated_gradients import integrated_gradients, random_baseline_integrated_gradients
from predictions_and_gradients import calculate_outputs_and_gradients, top_label_id_and_score
from visualize import visualize_token_attrs
import sklearn.preprocessing
import sklearn

version = 'v2'  # v1, v2

total_samples = 1000 if version == 'v2' else 100  # any desired value

target_label_idx = None

directory = 'model'

results = []

for dataset_name, dataset in [
    ('packet_loss', json.load(open('data/dataset/' + version + '/packet_loss.json'))),
    ('latency', json.load(open('data/dataset/' + version + '/latency.json'))),
]:
    features = np.asarray(list(dataset['features'][:total_samples]))
    labels = np.asarray(list(dataset['labels'][:total_samples]))


    model = tf.keras.models.load_model(directory+'/'+version+'_'+dataset_name+'.hdf5')

    
    enc = sklearn.preprocessing.OneHotEncoder(categories = 'auto')
    enc.fit(labels.reshape(-1, 1))
    labels = enc.transform(labels.reshape(-1, 1)).toarray()

    features = features.reshape((features.shape[0], features.shape[1], 1))
    
    indexes = [i for i in range(0, 50)]
    
    for index in indexes:
        predictions, attributions  = integrated_gradients(features[index, :], model, target_label_idx, calculate_outputs_and_gradients, steps = 50, baseline=None)
        '''
        print(predictions)
        print('****************')
        print('****************')
        print('****************')
        #print(attributions[0:31].min())
        #print(attributions)
        print('****************')
        print('****************')
        print('****************')
        #print(features[index])
        print('****************')
        print('****************')
        print('****************')'''
        
        visualize_token_attrs(features[index], attributions)
        
        results.append({
        'index': index,
        'features': features[index].tolist(),
        'predictions': predictions.tolist(),
        'attributions': attributions.tolist()
        })
with open('data/' + version + '_attributions.json', 'w') as f:
    json.dump(results, f, indent=2)

    