import re
import os
import networkx as nx

dataPath = "/home/santa/Dropbox/NAM/Problem Set 1/Data/facebook100txt/"

file = open("/home/santa/Dropbox/NAM/Problem Set 1/Code/data1.txt", "w")
for filename in os.listdir(dataPath):
    if filename.endswith(".txt") and not filename.endswith("attr.txt") and filename.find("readme") == -1:
        lines = [line.rstrip('\n') for line in open(dataPath+filename)]
        
        G = nx.Graph()
        for line in lines:
            vertexes = line.split("\t")
            G.add_edge(vertexes[0], vertexes[1])
        
        listDegree = []
        for node in G.nodes():
            listDegree.append(G.degree(node))
        
        average_degree = sum(listDegree) / (1.0 * G.number_of_nodes())
        average_squared_degree = sum([i ** 2 for i in listDegree]) / (1.0 * G.number_of_nodes())
        mean_neighbour_degree = average_squared_degree / (1.0 * average_degree)
        name = filename[:re.search("\d", filename).start()]
        file.write(name + "," + str(average_degree) + "," + str(mean_neighbour_degree/(1.0 * average_degree)) + "\n")
file.close()