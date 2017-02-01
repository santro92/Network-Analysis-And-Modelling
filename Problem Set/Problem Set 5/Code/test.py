import networkx as nx
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

dataPath = "/home/santa/Dropbox/NAM/Problem Set 5/data/"
filename1 = "data_people.txt"
filename2 = "net1m_2011-08-01.txt"

mm = ff = mf = 0
edges = []
nodes = set()
lines = [line.rstrip('\n') for line in open(dataPath+filename2)]
for line in lines:
    vertexes = line.split("\t")
    label1 = labels[int(vertexes[0])]
    label2 = labels[int(vertexes[1])]
    nodes.add(int(vertexes[0]))
    nodes.add(int(vertexes[1]))
    edges.append((int(vertexes[0]),int(vertexes[1])))
    if label1 == 1 and label2 == 1:
        mm += 1
    elif label1 == 2 and label2 == 2:
        ff += 1
    else:
        mf += 1
        
# print str(mm) + "," + str(ff) + "," + str(mf)

labels = defaultdict(int)
m = []
f = []
lines = [line.rstrip('\n') for line in open(dataPath+filename1)]
for line in lines[1:]:
    node_id = int(line.split(" \"")[0])
    label = int(line.split("\" ")[1])
    if node_id in nodes:
        labels[node_id] = label
        if label == 1:
            m.append(node_id)
        else:
            f.append(node_id)

# print str(m) + "," + str(f)

G = nx.Graph()
G.add_edges_from(edges)
G.add_nodes_from(nodes)

pos = nx.fruchterman_reingold_layout(G)
print len(f)
print len(m)

nx.draw_networkx_nodes(G,pos,nodelist=f, node_color='r')
nx.draw_networkx_nodes(G,pos,nodelist=m, node_color='b')
nx.draw_networkx_edges(G,pos,edgelist=edges)
plt.show()
print "Over"