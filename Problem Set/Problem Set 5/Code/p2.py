from __future__ import division
import random
import networkx as nx
import csv
from collections import defaultdict

dataPath = "/home/santa/Dropbox/NAM/Problem Set 5/"
files = ["Caltech36", "Reed98"]
for filename in files:
    lines = [line.rstrip('\n') for line in open(dataPath+"data/"+filename+".txt")]
    G = nx.Graph()
    for line in lines:
        vertexes = line.split("\t")
        G.add_edge(vertexes[0], vertexes[1])
    avg_deg = sum(list(G.degree(G.nodes()).values()))/G.number_of_nodes()
    p = 1/avg_deg
    no_of_iter = 1000
    
    f = open(dataPath+"Code/"+filename+".csv", 'a')
    writer = csv.writer(f)
    writer.writerow(("node_id", "spreading centrality", "degree"))
    for i in G.nodes():
        print i
        epidemic_size = 0
        for j in range(no_of_iter):
            infected_list = defaultdict(int)
            infected_list[i] = 1
            lst = [i]
            while len(lst):
                newList = []
                for infected_node in lst:
                    edges = G.edges(infected_node)
                    for edge in edges:
                        if random.uniform(0, 1) <= p:
                            if infected_list[edge[1]] != 1:
                                newList.append(edge[1])
                                infected_list[edge[1]] = 1
                lst = newList
            epidemic_size += len(infected_list)
        writer.writerow((i, (epidemic_size/no_of_iter), G.degree(i)))
    f.close()
