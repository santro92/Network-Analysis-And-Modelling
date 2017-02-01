import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

csv_file = "/home/santa/Dropbox/NAM/Problem Set 4/Code/temp.csv"
df = pd.read_csv(csv_file)
lst = ['len', 'size']
for item in lst:
    x = df['p'].tolist()
    y = df[item].tolist()
    z = df['e'].tolist()
    for epsilon in range(17):
        plt.plot( x[epsilon::17], y[epsilon::17])
    plt.xlabel('Probability, p')
    plt.ylabel('average ' + item)
    plt.show()
