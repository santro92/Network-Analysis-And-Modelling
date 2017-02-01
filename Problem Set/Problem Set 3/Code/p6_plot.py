import matplotlib.pyplot as plt
import pandas as pd

csv_file = "/home/santa/Dropbox/NAM/Problem Set 3/Code/prob6_2.csv"
df = pd.read_csv(csv_file)
y = df['size'].tolist()
x = df['p1'].tolist()

plt.plot( x, y)
plt.xlabel(r'$p_1$')
plt.ylabel('Mean fractional size of largest component')
plt.savefig("/home/santa/Dropbox/NAM/Problem Set 3/Latex/images/p6.png")
plt.clf()
