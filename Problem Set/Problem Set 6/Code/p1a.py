from __future__ import division
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

c = 3
n = 1000000
ccdf_dict = defaultdict(list)

for r in [1, 2, 3, 4]:
    print str(r)
    print "Initializing"
    p = c/(c+r)
    in_degree_cnt_list = np.zeros(n+1, dtype=np.int)
    in_degree_cnt_list[0] = -1
    in_degree_cnt_list[1:(c+1)] = c
    
    vertex_label_list = []
    for j in range(1, c+2):
        vertex_label_list.extend([j]*c)

    print "Price's Model simulation"
    for i in range(c+2, n+1):
        nodes = set()
        while len(nodes) < c:
            if random.random() < p:
                nodes.add(vertex_label_list[int(math.floor(c*(i-1)*random.random()))])
            else:
                nodes.add(int(math.ceil((i-1)*random.random())))
        vertex_label_list.extend(nodes)
        for node in nodes:
            in_degree_cnt_list[node] += 1
    
    print "Calculating ccdf"
    sorted_list = np.sort(in_degree_cnt_list)
    counts, bin_edges = np.histogram(sorted_list[1:], bins=range(0, max(sorted_list)+1))

    ccdf = np.zeros(len(counts), dtype=np.int)
    ccdf[0] = sum(counts)
    for k in range(1, len(counts)):
        ccdf[k] = ccdf[k-1] - counts[k-1]
    
    ccdf = [x/n for x in ccdf]
    ccdf_dict[r] = ccdf        

for r in ccdf_dict.keys():
    plt.plot(ccdf_dict[r], label="r = " + str(r))

plt.legend(loc='upper right', fancybox=True, shadow=True)
plt.tight_layout()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'in-degree ($k_{in}$)')
plt.ylabel(r'$Pr(K \geq k_{in})$')
plt.show()
