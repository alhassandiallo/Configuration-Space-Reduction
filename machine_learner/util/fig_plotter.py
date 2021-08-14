import matplotlib.pyplot as plt
import pandas as pd
from ast import literal_eval
import json
import numpy as np
import matplotlib.patches as mpatches
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler


version = 'v1'  # v1, v2


def plot_learning_vs_no_learning():
    plt.figure()
    plt_index = 1

    for title in [
        'Packet Loss (%)',
        'Latency (%)',
        'Adaptation Space',
        'Analysis Time (sec)',
    ]:
        data = {
            'explainable_learning': [],
            'learning': []
        }

        for file_name in ['explainable_learning', 'learning']:
            path = 'data/results/' + version + '/'
            file_data = open(path + file_name + '.txt').readlines()
            file_data = [x.strip() for x in file_data]
            learning_size = 11
            no_learning_size = 11

            for line in file_data:
                content = line.split(';')

                if len(content) > 1 and int(content[0]) == 1:  # skip training cycle
                    continue

                if title == 'Packet Loss (%)':
                    if len(content) == no_learning_size:
                        data[file_name].append(float(content[7]))
                    elif len(content) == learning_size:
                        data[file_name].append(float(content[7]))

                elif title == 'Latency (%)':
                    if len(content) == no_learning_size:
                        data[file_name].append(float(content[8]))
                    elif len(content) == learning_size:
                        data[file_name].append(float(content[8]))

                elif title == 'Adaptation Space':
                    if len(content) == no_learning_size:
                        data[file_name].append(int(content[4]))
                    elif len(content) == learning_size:
                        data[file_name].append(int(content[4]))

                elif title == 'Analysis Time (sec)':
                    if len(content) == no_learning_size:
                        data[file_name].append(float(content[5]) / 1000)
                    elif len(content) == learning_size:
                        data[file_name].append(float(content[5]) / 1000)


        print({
            'title': title,
            'explainable_learning_avg': np.average(data['explainable_learning']),
            'learning_avg': np.average(data['learning'])
        })

        plt.subplot(2, 2, plt_index)

        boxplot = plt.boxplot(
            [data[x] for x in ['learning', 'explainable_learning']],
            positions=[1, 2],
            widths=.3,
            labels=['regular', 'explainable'],
            patch_artist=True,
            #showfliers=False,
            #notch=True,
            medianprops={'color': 'black', 'linewidth': 2}
        )

        for index, box in enumerate(boxplot['boxes']):
            box.set(facecolor=[ 'orange', 'green'][index])
            #box.set(facecolor=['orange', 'dodgerblue'][index])

        plt.ylabel(title, fontsize='20')
        plt.xticks(size = 20)
        plt.yticks(size = 15)
        #plt.figlegend(bbox_to_anchor=(1.1, 1.05), loc="upper left")
        plt_index += 1
    plt.show()


#plot_feature_scaling()
plot_learning_vs_no_learning()
#plot_learning_models_time()
#plot_uncertainties_profiles()
#plot_training_selection()
#plot_offline_activities_time()
#plot_offline_activities()
#for i in range(300, 0, -1):
#    plot_selected_adaptation_options(i)