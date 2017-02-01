import networkx as nx

def getDegreeCent(G):
    degreeCent = nx.degree_centrality(G)
    #for k,v in degreeCent.items():
    #    degreeCent[k] = round(v,3)
    return degreeCent

def getBetweenCent(G):
    betweenCent = nx.betweenness_centrality(G,normalized=False)
    for k,v in betweenCent.items():
        betweenCent[k] = v/(G.number_of_nodes()**2)
    return betweenCent

G = nx.Graph()
G.add_edge(0,2)
G.add_edge(0,1)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,5)
G.add_edge(4,6)
G.add_edge(5,6)
print G.number_of_nodes()
nx.draw(G)

data = {'Node' : pd.Series(range(G.number_of_nodes())),
        'Degree' : pd.Series(getDegreeCent(G)),
        'Betweenness' : pd.Series(getBetweenCent(G))}

family = pd.DataFrame(data, columns=['Node', 'Degree', 'Betweenness'])
print family