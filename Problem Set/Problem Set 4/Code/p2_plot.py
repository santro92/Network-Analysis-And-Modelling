import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

csv_file = "/home/santa/Dropbox/NAM/Problem Set 4/Code/prob2.csv"
df = pd.read_csv(csv_file)
lst = ['len','size']
for item in lst:
    x = df['p'].tolist()
    y = df[item].tolist()
    plt.plot( x, y )
    plt.xlabel('Probability, p')
    if item == 'len':
        plt.axhline( y=np.log(1000),  color='r')
    plt.ylabel('average ' + item)
    plt.savefig("/home/santa/Dropbox/NAM/Problem Set 4/Latex/images/"+ item+".png")
    plt.clf()
