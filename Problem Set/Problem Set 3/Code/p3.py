import networkx as nx
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
from sklearn import metrics
import math
import collections

def NMI( labels_pred, labels_true ):
    V = len(labels_pred)
    C = set(labels_pred)
    Cdash = set(labels_true)
    Ci = defaultdict(int)
    Cdashj = defaultdict(int)
    
    HC = 0
    for i in C:
        Ci[i] = len([1 for j in labels_pred if j == i])
        HC += ((float(Ci[i])/V) * math.log(float(Ci[i])/V))
    
    HCdash = 0
    for i in Cdash:
        Cdashj[i] = len([1 for j in labels_true if j == i])
        HCdash += ((float(Cdashj[i])/V) * math.log(float(Cdashj[i])/V))
    
    merge = zip(labels_pred, labels_true)
    ICCdash = 0
    for i in C:
        for j in Cdash:
            intersect = len([1 for (u,v) in merge if (u == i and v == j)])
            if intersect != 0:
                ICCdash += ((float(intersect)/V) * math.log((float(intersect) * V)/(Ci[i] * Cdashj[j])) )
    
    return (-2.0 * ICCdash) / (HC + HCdash)

def geteuv(edges, group_u, group_v):
    sum = 0
    for x,y in edges:
        if (x in group_u and y in group_v) or (x in group_v and y in group_u):
            if (group_u == group_v):
                sum = sum + 2
            else:
                sum = sum + 1
    return sum/(2.0*len(edges))

fileName = "/home/santa/Dropbox/NAM/Problem Set 3/Data/karate_club_edges.txt"
lines = [line.rstrip('\n') for line in open(fileName)]
edges = []
for line in lines:
    edges.append((int(line.split()[0]),int(line.split()[1])))
G = nx.Graph()
G.add_edges_from(edges)

sum = 0   
for node in G.nodes():
    sum = sum + (G.degree(node)**2)
Q = (-1.0/(4.0*(G.number_of_edges()**2))) * sum

groups = {}
bestgroup = {}
for i in range(1,G.number_of_nodes()+1):
    groups[i] = range(i,i+1)

qList = []
qList.append(Q)
while len(groups) > 1:
    
    e = np.zeros((G.number_of_nodes()+1,G.number_of_nodes()+1))
    for u in groups:
        for v in groups:
            e[u][v] = geteuv(edges, groups[u], groups[v])

    delQ = -10
    dQ = np.zeros((len(groups)+1,len(groups)+1))
    for i in range(len(groups)):
        for j in range(i+1,len(groups)):
            u = groups.keys()[i]
            v = groups.keys()[j]
            temp = 2 * (e[u][v] - (e[:,u].sum() * e[:,v].sum()))
            dQ[i][j] = temp
            if temp > delQ:
                delQ = temp
                maxu, maxv = u,v
    if Q > Q+delQ:
        break
    groups[maxu] = groups[maxu] + groups[maxv]
    groups.pop(maxv,None)
    Q = Q+delQ
    qList.append(Q)

groups_labels = {}
club_labels = {}
i = 0
for k,v in groups.iteritems():
    i = i+1
    for l in v:
        groups_labels[l] = l
        club_labels[l] = i

# plt.plot(qList)
# plt.xlabel('Number of merges')
# plt.ylabel('Modularity (Q)')
# plt.show()

# pos = nx.fruchterman_reingold_layout(G)
# nx.draw_networkx_nodes(G,pos,nodelist=groups[1], node_color='b')
# nx.draw_networkx_nodes(G,pos,nodelist=groups[2], node_color='g')
# nx.draw_networkx_nodes(G,pos,nodelist=groups[9], node_color='r')
# nx.draw_networkx_edges(G,pos,edgelist=edges)
# nx.draw_networkx_labels(G,pos,groups_labels,font_size=8)
# plt.show()

# file = open("/home/santa/Dropbox/NAM/Problem Set 3/Data/karate_club_edges_predict.txt", "w")
club_labels = collections.OrderedDict(sorted(club_labels.items()))
list_pred = []
for k in club_labels:
    list_pred.append(int(club_labels[k]))
    # file.write(str(k) + "\t" + str(club_labels[k]) + "\n")
# file.close()

fileName = "/home/santa/Dropbox/NAM/Problem Set 3/Data/karate_club_labels.txt"
lines = [line.rstrip('\n') for line in open(fileName)]
list_true = []
for line in lines:
    list_true.append(int(line.split()[1]))

print NMI(list_pred, list_true)
