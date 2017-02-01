from __future__ import division
import random
import math
import numpy as np
from collections import defaultdict

c = 12
r = 5
n = 1000000
no_of_iter = 200
ccdf_dict = defaultdict(list)

avg_first_10 = 0
avg_last_10 = 0

for itr in range(no_of_iter):
    print str(itr)
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
    
    print "Calculating average"
    avg_first_10 += sum(in_degree_cnt_list[:100000])/100000
    avg_last_10 += sum(in_degree_cnt_list[-100000:])/100000    

print avg_first_10/no_of_iter
print avg_last_10/no_of_iter
