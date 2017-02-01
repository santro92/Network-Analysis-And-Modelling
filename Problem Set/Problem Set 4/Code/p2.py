from __future__ import division
import networkx as nx
import numpy as np
import random
from Queue import Queue

n= 1000
c = 8
l = 2
k = 500
epsilon = 0
p_in = (2*c + epsilon)/(2*n)
p_out = (2*c - epsilon)/(2*n)
sbm = [[p_in, p_out],[p_out, p_in]]

for i in range(0,100):
    print i+1
    p = i/100
    length = 0
    epidemic_size = 0
    no_of_iter = 500
    no_of_sim = 200
    for j in range(0,no_of_iter):
        G = nx.planted_partition_graph(l, k, p_in, p_out)
        for s in range(0,no_of_sim):
            infected_list = np.zeros(n)
            lst = [random.randint(0,n-1)]
            while len(lst):
                length += 1
                newList = []
                for infected_node in lst:
                    edges = G.edges(infected_node)
                    for edge in edges:
                        if(random.uniform(0, 1) <= p):
                            if(infected_list[edge[1]] != 1):
                                newList.append(edge[1])
                                infected_list[edge[1]] = 1
                lst = newList
            epidemic_size += sum(infected_list)
    file = open("/home/santa/Dropbox/NAM/Problem Set 4/Code/prob2.txt", "a")
    file.write(str(p) + "," + str(length/(no_of_iter*no_of_sim)) + "," + str(epidemic_size/(no_of_iter*no_of_sim)) + "\n")
    file.close()
