import numpy as np
import tensorflow.keras 
import tensorflow as tf

def calculate_outputs_and_gradients(inputs, model, target_label_idx):
    
    #x_tensor= tf.Variable(inputs, dtype = tf.float32)
    x_tensor = tf.convert_to_tensor(inputs, dtype = tf.float32)
    #x_tensor = inputs
    
    with tf.GradientTape() as tape:
        tape.watch(x_tensor)
        predictions = model(x_tensor)
    
    if target_label_idx is not None:
         predictions = predictions[:, target_label_idx]
    
    gradients = tape.gradient(predictions, x_tensor)

    return predictions, gradients

def top_label_id_and_score(inputs, model, calculate_outputs_and_gradients):

    preds, _ = calculate_outputs_and_gradients(inputs, model, 0)

    target_label_idx = np.argmax(preds[0])
    return target_label_idx, preds[0][target_label_idx]






