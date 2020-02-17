import networkx as nx 
import matplotlib.pyplot as plt

Graph = nx.Graph()
list_of_edges = [(0, 2), (0, 5), (0, 6), (0, 7), (0, 5), (1, 4), (1, 7), (2, 4), (2, 7), (3, 5), (3, 6), (5, 6), (5, 7), (6, 7)]
Graph.add_edges_from(list_of_edges)
nx.draw(Graph, with_labels=True)
plt.show()