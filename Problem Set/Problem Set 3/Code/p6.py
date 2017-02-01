import networkx as nx
import random

for p in range(0,101,1):
    size = 0
    degreeSeq = []
    noOfNodes = 10000
    for i in range(noOfNodes):
        if random.uniform(0, 1) <= (float(p)/100):
            degreeSeq.append(int(1))
        else:
            degreeSeq.append(int(3))
    
    vector = []
    for i in range(len(degreeSeq)):
       for j in range(degreeSeq[i]):
           vector.append(i)
    
    noOfIter = 2000
    for i in range(noOfIter):
        random.shuffle(vector)
        edges = []
        for a,b in zip(vector[0:][::2],vector[1:][::2]):
            edges.append((a,b))
        G = nx.Graph()
        G.add_edges_from(edges)
        G.remove_edges_from(G.selfloop_edges())
        G.add_nodes_from(range(noOfNodes))
        Gcc=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
        G0=Gcc[0]
        size += float(G0.number_of_nodes())/10000
    
    file = open("/home/santa/Dropbox/NAM/Problem Set 3/Code/prob6_2.txt", "a")
    file.write(str((float(p)/100)) + "," + str(size/noOfIter) + "\n")
    file.close()
