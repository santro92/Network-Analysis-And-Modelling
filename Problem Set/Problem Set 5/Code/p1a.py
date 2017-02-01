from __future__ import division
import random
import csv
import networkx as nx
from collections import defaultdict
from collections import Counter

dataPath = "/home/santa/Dropbox/NAM/Problem Set 5/"
files = [("net1m_2011-08-01.txt", "data_people.txt")]#, ("HVR_5.txt", "metadata_CysPoLV.txt")]
for (filename1, filename2) in files:
    lines = [line.rstrip('\n') for line in open(dataPath+"data/"+filename1)]
    G = nx.Graph()
    for line in lines:
        vertexes = line.split("\t")
        G.add_edge(int(vertexes[0]), int(vertexes[1]))
        G.add_node(int(vertexes[0]))
        G.add_node(int(vertexes[1]))
    
    lines = [line.rstrip('\n') for line in open(dataPath+"data/"+filename2)]
    labels = defaultdict(int)
    
    if filename1.startswith("net1m"):
        for line in lines[1:]:
            node_id = int(line.split(" \"")[0])
            label = int(line.split("\" ")[1])
            if node_id in G.nodes():
                labels[node_id] = label
    else:
        cnt = 1
        for line in lines:
            if cnt in G.nodes():
                labels[cnt] = int(line.strip())
            cnt += 1
    
    labels_set = set(labels.values())
    no_of_iter = 200
    no_of_nodes = G.number_of_nodes()
    fp = open(dataPath+"Code/prob1a_flip_"+filename1.split("_")[0]+".csv", 'a')
    writer = csv.writer(fp)
    writer.writerow(("f", "acc"))
    for f in range(1, 100):
        print f
        f /= 100
        train_size = int(f*no_of_nodes)
        avg_accuracy = 0
        for i in range(no_of_iter):
            train_set = defaultdict(int)
            test_set = defaultdict(int)
    
            while len(train_set) <= train_size:
                key = int(random.choice(labels.keys()))
                train_set[key] = int(labels[key])
    
            for node in G.nodes():
                if not int(node) in train_set:
                    edges = G.edges(node)
                    lst = []
                    for edge in edges:
                        if edge[1] in train_set:
                            lst.append(train_set[edge[1]])
    
                    data = Counter(lst)
                    max_count = 0 if len(data) == 0 else min(data.values())
                    mode = [k for k, v in data.items() if v == max_count]
    
                    if len(mode) == 1:
                        test_set[node] = int(mode[0])
                    else:
                        if len(mode) != 0:
                            test_set[node] = int(random.choice(mode))
                        else:
                            test_set[node] = int(random.sample(labels_set, 1)[0])
    
            cnt = 0
            for key in test_set.keys():
                if test_set[key] == labels[key]:
                    cnt += 1
    
            accuracy = cnt/len(test_set)
            avg_accuracy += accuracy
        writer.writerow((f, (avg_accuracy/no_of_iter)))
    fp.close()
