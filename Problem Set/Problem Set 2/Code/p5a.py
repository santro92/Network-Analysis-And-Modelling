import networkx as nx
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

def getEdges(G):
    edges = []
    name = []
    fileName = "/home/santa/Dropbox/NAM/Problem Set 2/Data/data_medici_network.txt"
    lines = [line.rstrip('\n') for line in open(fileName)]
    vertex=0
    for line in lines:
        G.add_node(vertex)
        openBracket = line.index('[')
        closeBracket = line.index(']')
        subStr = line[openBracket+1:closeBracket]
        list = []
        for i in range(len(subStr)):
            if subStr[i] == "(":
                word = ''
                while subStr[i+1] != ",":
                    i = i+1
                    word = word+subStr[i]
                list.append(word)
        for l in list:
            edges.append((vertex,int(l)))
        vertex=vertex+1
        name.append(line.split()[1].replace(",","").strip())
    return name, edges

def generateGraph():
    G = nx.Graph()
    name, edges = getEdges(G)
    G.add_edges_from(edges)
    return name, G 

def getDegreeCent(G):
    degreeCent = nx.degree_centrality(G)
    for k,v in degreeCent.items():
        degreeCent[k] = round(v,3)
    return degreeCent

def getHarmonicCent(G):
    harmonicCent = nx.harmonic_centrality(G)
    for k,v in harmonicCent.items():
        harmonicCent[k] = round(v/(G.number_of_nodes()-1),3)
    return harmonicCent

def getEigenCent(G):
    eigenCent = nx.eigenvector_centrality(G)
    for k,v in eigenCent.items():
        eigenCent[k] = round(v,3)
    return eigenCent

def getBetweenCent(G):
    betweenCent = nx.betweenness_centrality(G,normalized=False)
    for k,v in betweenCent.items():
        betweenCent[k] = round(v/(G.number_of_nodes()**2),3)
    return betweenCent
    
def calcCentralityScores():
    name, G = generateGraph
    data = {'Node' : pd.Series(range(G.number_of_nodes())),
            'Name' : pd.Series(name),
            'Degree' : pd.Series(getDegreeCent(G)),
            'Harmonic' : pd.Series(getHarmonicCent(G)),
            'Eigen' : pd.Series(getEigenCent(G)),
            'Betweenness' : pd.Series(getBetweenCent(G))}
    
    family = pd.DataFrame(data, columns=['Node', 'Name', 'Degree', 'Harmonic', 'Eigen', 'Betweenness'])
    #family.to_csv('/home/santa/Dropbox/NAM/Problem Set 2/Data/family.csv', index=False)
    
    data1 = {}
    for col in ['Degree', 'Harmonic', 'Eigen', 'Betweenness']:
        index = np.argsort(family[col])
        list = []
        for item in index[::-1]:
            list.append((name[item], round(family[col][item],3)))
        data1[col] = pd.Series(list)
    
    sort_family = pd.DataFrame(data1, columns=['Degree', 'Harmonic', 'Eigen', 'Betweenness'])
    #sort_family.to_csv('/home/santa/Dropbox/NAM/Problem Set 2/Data/sort_family.csv', index=False)

def getDegreeSeq():
    G = nx.Graph()
    name, edges = getEdges(G)
    G.add_edges_from(edges)
    return list(G.degree(G.nodes()).values())

def generateConfigModel():
    degreeSeq = getDegreeSeq()
    vector = []
    for i in range(len(degreeSeq)):
       for j in range(degreeSeq[i]):
           vector.append(i)
    
    noOfIter = 10000
    noOfNodes = len(degreeSeq)
    data = {}
    for i in range(noOfIter):
        random.shuffle(vector)
        edges = []
        for a,b in zip(vector[0:][::2],vector[1:][::2]):
            edges.append((a,b))
        G = nx.Graph()
        G.add_edges_from(edges)
        G.remove_edges_from(G.selfloop_edges())
        G.add_nodes_from(range(noOfNodes))
        data[i] = pd.Series(getHarmonicCent(G))
    
    configModel = pd.DataFrame(data)
    return configModel
    
def plotGraph():
    model_harmonic = generateConfigModel()
    name, G = generateGraph()
    orig_harmonic = pd.Series(getHarmonicCent(G))
    
    mean_diff = orig_harmonic - model_harmonic.mean(axis=1)
    quant_25  = orig_harmonic - model_harmonic.quantile(q=0.25,axis=1)
    quant_75  = orig_harmonic - model_harmonic.quantile(q=0.75,axis=1)
    
    plt.xlim(0,len(name)-1)
    plt.plot(mean_diff, label = 'mean')
    plt.plot(quant_25, label = '25% quantiles')
    plt.plot(quant_75, label = '75% quantiles')
    plt.plot(range(len(name)),[0]*len(name),'k--')
    plt.fill_between(range(len(name)),quant_25,quant_75, color='grey')
    plt.ylabel('difference')
    plt.xlabel('vertex label')
    plt.legend(loc='upper right', bbox_to_anchor=(0.5, 1.05), fancybox=True, shadow=True)
    plt.tight_layout()
    plt.show()
        
#calcCentralityScores()
#getDegreeSeq()
#generateConfigModel()
plotGraph()