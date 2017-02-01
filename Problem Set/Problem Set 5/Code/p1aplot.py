import matplotlib.pyplot as plt
import pandas as pd

files = ['net1m', 'HVR', 'flip_netm']
title = {}
title['net1m'] = 'Norwegian Boards of Directors network'
title['HVR'] = 'Malaria var DBLa HVR network'
title['flip_net1m'] = 'Norwegian Boards of Directors network - flipped'
for filename in files:
    csv_file = "/home/santa/Dropbox/NAM/Problem Set 5/Code/prob1a_"+filename+".csv"
    df = pd.read_csv(csv_file)
    x = df['f'].tolist()
    y = df['acc'].tolist()
    plt.plot(x, y)
    plt.xlabel('f')
    plt.ylim([0, 1])
    plt.ylabel('accuracy')
    plt.title(title[filename])
    plt.savefig("/home/santa/Dropbox/NAM/Problem Set 5/Latex/images/1a_"+filename+".png")
    plt.clf()