import numpy as np

# integrated gradients
def integrated_gradients(inputs, model, target_label_idx, calculate_outputs_and_gradients, baseline, steps=50):
    if baseline is None:
        baseline = 0 * inputs 
    # scale inputs and compute gradients
    scaled_inputs = [baseline + (float(i) / steps) * (inputs - baseline) for i in range(0, steps + 1)]
    predictions, grads = calculate_outputs_and_gradients(scaled_inputs, model, target_label_idx)

    grads = (grads[:-1] + grads[1:]) / 2.0
    avg_grads = np.average(grads[:-1], axis=0)
    integrated_grad = (inputs - baseline) * avg_grads
    return predictions, integrated_grad

def random_baseline_integrated_gradients(inputs, model, target_label_idx, calculate_outputs_and_gradients, steps, num_random_trials):
    all_intgrads = []
    for i in range(num_random_trials):
        integrated_grad = integrated_gradients(inputs, model, target_label_idx, calculate_outputs_and_gradients, \
                                                baseline=255.0 *np.random.random(inputs.shape), steps=steps)
        all_intgrads.append(integrated_grad)
        print('the trial number is: {}'.format(i))
    avg_intgrads = np.average(np.array(all_intgrads), axis=0)
    return avg_intgrads
