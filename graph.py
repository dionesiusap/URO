#Menggambar graf dengan 8 nodes
import matplotlib
import networkx as nx
import itertools

G = nx.Graph()

#Menambah node
L = ['a','b','c','d','e','f','g','h']
G.add_nodes_from(L)
'''
Kak ini kenapa nodesnya selalu kerandom ya? :(
'''

#Menambah edge
pairs = itertools.combinations(L,2)

edges = list()
for pair in pairs:
    edges.append(pair)

for edge in edges:
    G.add_edge(*edge)

#Menampilkan gambar
nx.draw_circular(G, with_labels = True, edge_color='b')
matplotlib.pyplot.show()
