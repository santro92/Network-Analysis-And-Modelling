import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

csv_file = "/home/santa/Dropbox/NAM/Problem Set 4/Code/1c.csv"
df = pd.read_csv(csv_file)
lst = ['len', 'size']
for item in lst:
    x = df['p'].tolist()
    y = df[item].tolist()
    z = df['e'].tolist()
    i = 51
    for p in range(2):
    	plt.plot(z[p*i:(p+1)*i], y[p*i:(p+1)*i], label= 'p = ' + str(x[(p*i)+1]))
    plt.xlabel('Epsilon')
    plt.ylabel('average ' + item)
    plt.legend(loc='lower left', fancybox=True, shadow=True)
    plt.tight_layout()
    plt.savefig("/home/santa/Dropbox/NAM/Problem Set 4/Latex/images/1c_"+ item + ".png")
    plt.clf()