import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

csv_file = "/home/santa/Dropbox/NAM/Problem Set 3/Code/prob4.csv"
df = pd.read_csv(csv_file)
lst = ['Gender', 'Major', 'SF_status', 'Vertex']
for item in lst:
    x = df['Size'].tolist()
    y = df[item].tolist()
    print item +"," + str(np.mean(y))
    # plt.plot( x, y, 'ro')
    # plt.axhline( y=0,  color='r')
    # plt.xscale('log')
    # plt.xlabel('Network size, n')
    # plt.ylabel(item + ' modularity, Q')
    # plt.savefig("/home/santa/Dropbox/NAM/Problem Set 3/Latex/images/"+ item+".png")
    # plt.clf()
    # sns.kdeplot( np.array( y ) )
    # plt.axvline( x=0, color='r' )
    # plt.xlabel('Assortativity (' + item + ')')
    # plt.ylabel('Density')
    # plt.savefig("/home/santa/Dropbox/NAM/Problem Set 3/Latex/images/"+ item+"_density.png" )
    # plt.clf()
