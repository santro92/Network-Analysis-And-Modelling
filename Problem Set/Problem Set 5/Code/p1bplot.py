import matplotlib.pyplot as plt
import pandas as pd

files = ['temp_net1m']
title = {}
title['temp_net1m'] = 'Norwegian Boards of Directors network'
title['HVR'] = 'Malaria var DBLa HVR network'
for filename in files:
    csv_file = "/home/santa/Dropbox/NAM/Problem Set 5/Code/prob1b_"+filename+".csv"
    df = pd.read_csv(csv_file)
    x = df['f'].tolist()
    # plt.plot(x, df['d'].tolist(), label='degree')
    plt.plot(x, df['n'].tolist(), label='neighbors')
    # plt.plot(x, df['p'].tolist(), label='shortest path')
    plt.xlabel('f')
    plt.ylim([0.5,1])
    plt.ylabel('accuracy')
    plt.title(title[filename])
    plt.legend(loc='center right', fancybox=True, shadow=True)
    plt.tight_layout()
    plt.savefig("/home/santa/Dropbox/NAM/Problem Set 5/Latex/images/1b_"+filename+".png")
    plt.clf()