from __future__ import division
import operator
import networkx as nx
from collections import defaultdict
import sys

dataPath = "/home/santa/Dropbox/NAM/Problem Set 6/data/"
filename1 = 'Cit-HepPh.txt'
filename2 = 'cit-HepPh-dates.txt'

lines = [line.rstrip('\n') for line in open(dataPath+filename1)]
G = nx.DiGraph()
for line in lines:
    vertexes = line.split("\t")
    G.add_edge(int(vertexes[0]), int(vertexes[1]))

nodes = G.nodes()
lines = [line.rstrip('\n\r') for line in open(dataPath+filename2)]
date_map = defaultdict()
for line in lines:
    node_id, date = line.split("\t")
    if int(node_id) in nodes:
        date_map[int(node_id)] = date

print len(date_map)
sys.exit()
sorted_date_map = sorted(date_map.items(), key=operator.itemgetter(1))
tenPC = int(len(sorted_date_map)/10)

avg_first_10 = 0
avg_last_10 = 0

for tup in sorted_date_map[:tenPC]:
    if tup[0] in nodes:
        avg_first_10 += G.in_degree(tup[0])

for tup in sorted_date_map[-tenPC:]:
    if tup[0] in nodes:
        avg_last_10 += G.in_degree(tup[0])

print avg_first_10/tenPC
print avg_last_10/tenPC
