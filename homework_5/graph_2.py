import networkx as nx 
import matplotlib.pyplot as plt

Graph = nx.Graph()
list_of_edges_1 = [(0, 1), (0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 5)]
list_of_edges_2 = ([(6, 8), (6, 10), (6, 11), (7, 6), (7, 8), (7, 11), (8, 10), (8, 11), (9, 10)])
Graph.add_edges_from(list_of_edges_1)
Graph.add_edges_from(list_of_edges_2)
nx.edge_betweenness_centrality(Graph, normalized=True, weight=None)
nx.draw(Graph, with_labels=True)
plt.show()