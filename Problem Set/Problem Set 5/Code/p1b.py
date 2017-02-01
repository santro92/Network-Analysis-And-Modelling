from __future__ import division
import csv
import random
import networkx as nx
import numpy as np
from sklearn import metrics


def calc_degree_score(graph, u, v, degree_score_set):
    degree = graph.degree(u) * graph.degree(v)
    if degree in degree_score_set:
        degree += random.uniform(0, 1)/no_of_nodes
    return degree


def calc_neighbor_score(graph, u, v, neighbor_score_set):
    i_neighbor = set(graph.neighbors(u))
    j_neighbor = set(graph.neighbors(v))
    union = len(i_neighbor | j_neighbor)
    intersection = len(i_neighbor & j_neighbor)
    neighbor = intersection/union if union != 0 else 0
    if neighbor in neighbor_score_set:
        neighbor += random.uniform(0, 1) / no_of_nodes
    return neighbor


def calc_path_score(graph, u, v, path_score_set):
    try:
        path = 1/nx.shortest_path_length(graph, source=u, target=v)
    except:
        path = 0
    if path in path_score_set:
        path += random.uniform(0, 1) / no_of_nodes
    return path


dataPath = "/home/santa/Dropbox/NAM/Problem Set 5/"
files = [("net1m_2011-08-01.txt", "data_people.txt"), ("HVR_5.txt", "metadata_CysPoLV.txt")]

for (filename1, filename2) in files:
    lines = [line.rstrip('\n') for line in open(dataPath+"data/"+filename2)]
    tot_no_of_nodes = len(lines)
    if filename1.startswith("data"):
        tot_no_of_nodes -= 1
    A_Full = np.zeros(shape=(tot_no_of_nodes, tot_no_of_nodes))
    
    edges = []
    nodes = set()
    lines = [line.rstrip('\n') for line in open(dataPath+"data/"+filename1)]
    for line in lines:
        vertexes = line.split("\t")
        edges.append((int(vertexes[0]), int(vertexes[1])))
        nodes.add(int(vertexes[0]))
        nodes.add(int(vertexes[1]))
        A_Full[int(vertexes[0])-1][int(vertexes[1])-1] = 1
        A_Full[int(vertexes[1])-1][int(vertexes[0])-1] = 1
    no_of_edges = len(edges)
    node_list = list(nodes)
    no_of_nodes = len(node_list)
    
    fp = open(dataPath+"Code/prob1b_"+filename1.split("_")[0]+".csv", "wt")
    writer = csv.writer(fp)
    writer.writerow(("f", "d", "n", "p"))
    fp.close()
    
    no_of_iter = 10
    for f in range(1, 100):
        print f
        f /= 100
        train_size = int(f*no_of_edges)
        degree_accuracy = 0
        neighbor_accuracy = 0
        path_accuracy = 0
    
        for itr in range(no_of_iter):
            train_set = random.sample(edges, train_size)
            G = nx.Graph()
            G.add_edges_from(train_set)
            G.add_nodes_from(node_list)
            A = np.zeros(shape=(tot_no_of_nodes, tot_no_of_nodes))
            for (x, y) in train_set:
                A[x-1][y-1] = 1
                A[y-1][x-1] = 1
            
            y_true = []
            y_degree_score = []
            y_degree_score_set = set()
            y_neighbor_score = []
            y_neighbor_score_set = set()
            y_path_score = []
            y_path_score_set = set()
    
            for x in range(0, no_of_nodes):
                i = node_list[x]
                for y in range(x+1, no_of_nodes):
                    j = node_list[y]
                    if A[i-1][j-1] == 0:
                        if A_Full[i-1][j-1] == 1:
                            y_true.append(1)
                        else:
                            y_true.append(0)
    
                        degree_score = calc_degree_score(G, i, j, y_degree_score_set)
                        y_degree_score.append(degree_score)
                        y_degree_score_set.add(degree_score)
    
                        neighbor_score = calc_neighbor_score(G, i, j, y_neighbor_score_set)
                        y_neighbor_score.append(neighbor_score)
                        y_neighbor_score_set.add(neighbor_score)
    
                        path_score = calc_path_score(G, i, j, y_path_score_set)
                        y_path_score.append(path_score)
                        y_path_score_set.add(path_score)
    
            y_degree_score = np.asarray(y_degree_score)
            y_degree_score /= sum(y_degree_score)
            y_neighbor_score = np.asarray(y_neighbor_score)
            y_neighbor_score /= sum(y_neighbor_score)
            y_path_score = np.asarray(y_path_score)
            y_path_score /= sum(y_path_score)
    
            degree_accuracy += metrics.roc_auc_score(y_true, y_degree_score)
            neighbor_accuracy += metrics.roc_auc_score(y_true, y_neighbor_score)
            path_accuracy += metrics.roc_auc_score(y_true, y_path_score)
    
        fp = open(dataPath+"Code/prob1b_"+filename1.split("_")[0]+".csv", "a")
        writer = csv.writer(fp)
        writer.writerow((f, (degree_accuracy/no_of_iter), (neighbor_accuracy/no_of_iter), (path_accuracy/no_of_iter)))
        fp.close()
