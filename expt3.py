import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([
    (1,2),(2,3),(3,4),(4,5),(6,1),
    (3,2),(6,4),(1,5),(6,2),(6,3)
])
pos = {1:(2.76,4.18),2:(4.6,4.2),3:(4.33,2.25),4:(2.93,2.25),5:(1.96,3.12),6:(3.42,3.29)}

H = nx.Graph()
H.add_nodes_from(G.nodes())
H.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,6)])

P = G.subgraph([1,2,3,6])

S = nx.Graph()
S.add_edges_from([(1,2),(6,3),(6,4)])

plt.figure(figsize=(10,8))
plt.subplot(221)
nx.draw(G, pos, with_labels=True, node_color="green", node_size=800, edge_color="black", width=2)
plt.title("Original Graph")
plt.subplot(222)
nx.draw(H, pos, with_labels=True, node_color="red", node_size=800, edge_color="black", width=2)
plt.title("Spanning Subgraph")
plt.subplot(223)
nx.draw(P, pos, with_labels=True, node_color="orange", node_size=800, edge_color="black", width=2)
plt.title("Induced Vertex Subgraph")
plt.subplot(224)
nx.draw(S, pos, with_labels=True, node_color="blue", node_size=800, edge_color="black", width=2)
plt.title("Edge Induced Subgraph")
plt.tight_layout()
plt.show()
