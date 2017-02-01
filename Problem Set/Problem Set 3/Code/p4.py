import os
import re
import networkx as nx
from collections import defaultdict

def modularity(edges, groups, attribute):
    e = np.zeros((len(attribute),len(attribute)))
    for edge in edges:
        u = attribute.index(int(groups[edge[0]]))
        v = attribute.index(int(groups[edge[1]]))
        e[u][v] += 1
    for row in range(len(attribute)):
        for col in range(len(attribute)):
            e[row][col] = e[row][col] / (1.0 * len(edges))
    ai = ei =0
    for i in range(len(attribute)):
        ai = ai + e[i].sum()**2
        ei = ei + e[i][i]
    return ei - ai

def vertexDegree(matrix, no_of_edges, degree, nodes):
    num = den = 0
    for i in range(len(nodes)):
        xi = degree[i]
        for j in range(i,len(nodes)):
            xj = degree[j]
            prod = (xi*xj)
            temp = (prod)/(2.0*no_of_edges)
            if i==j:
                den += ((xi - temp)*prod)
                num -= (prod * temp)
            else:
                den -= (2.0 * temp * prod) 
                num += (2.0 * prod * (matrix[i,j] - temp))
    return (num/den)

dataPath = "/home/santa/Dropbox/NAM/Problem Set 3/Data/facebook100txt/"
for filename in os.listdir(dataPath):
    if filename.endswith(".txt") and not filename.endswith("attr.txt") and filename.find("readme") == -1:
        print filename
        lines = [line.rstrip('\n') for line in open(dataPath+filename)]
        edges = []
        nodes = set()
        for line in lines:
            vertexes = line.split("\t")
            x,y = int(vertexes[0]), int(vertexes[1])
            nodes.add(x)
            nodes.add(y)
            edges.append((x,y))
        
        G = nx.Graph()
        G.add_edges_from(edges)
        G.add_nodes_from(nodes)
        degree = list(G.degree(G.nodes()).values())
        matrix = nx.adjacency_matrix(G)
        matrix = matrix.todense()

        attr_filename = filename.replace(".txt","_attr.txt")
        lines = [line.rstrip('\n') for line in open(dataPath+attr_filename)]
        lines.pop(0)
        major = defaultdict(list)
        majorSet = set()
        sfstatus = defaultdict(list)
        sfstatusSet = set()
        for line in lines:
            values = line.split("\t")
            sfstatusSet.add(int(values[1]))
            sfstatus[int(values[0])] = int(values[1])
            majorSet.add(int(values[3]))
            major[int(values[0])] = int(values[3])
        
        name = filename[:re.search("\d", filename).start()]
        file = open("/home/santa/Dropbox/NAM/Problem Set 3/Code/prob4.txt", "a")
        file.write(name + "," + str(len(nodes)) + "," + str(modularity(edges, sfstatus, list(sfstatusSet))) + "," + str(modularity(edges, major, list(majorSet))) + "," + str(vertexDegree(matrix, G.number_of_edges(), degree, nodes)) + "\n")
        file.close()