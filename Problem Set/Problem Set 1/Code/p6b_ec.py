import os
import re
import networkx as nx

dataPath = "/home/santa/Dropbox/NAM/Problem Set 1/Data/facebook100txt/"
for filename in os.listdir(dataPath):
    if filename.endswith(".txt") and not filename.endswith("attr.txt") and filename.find("readme") == -1:
        print filename
        lines = [line.rstrip('\n') for line in open(dataPath+filename)]
        G = nx.Graph()
        for line in lines:
            vertexes = line.split("\t")
            G.add_edge(vertexes[0], vertexes[1])
        
        graphs = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)
        largest_component = graphs[0]
        n = G.number_of_nodes()
        n_comp = largest_component.number_of_nodes()
        diameter = nx.diameter(largest_component)
        mean_length = nx.average_shortest_path_length(largest_component)
        
        name = filename[:re.search("\d", filename).start()]
        file = open("/home/santa/Dropbox/NAM/Problem Set 1/Code/ec.txt", "a")
        file.write(name + "," + str(diameter) + "," + str(n) + "," + str(mean_length) + "," + str(n_comp) + "\n")
        file.close()