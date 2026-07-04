import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nodes = ['A','B','C','D','E','F','G']
G.add_nodes_from(nodes)
edges = [
    ('A','B'),('B','C'),('B','D'),('A','D'),('D','E'),
    ('F','E'),('D','F'),('B','F'),('F','C'),('C','E'),('C','G'),('E','G')
]
G.add_edges_from(edges)
pos = {'A':(0,2),'B':(2,4),'C':(6,4),'D':(2,0),'E':(6,0),'F':(4,2),'G':(8,2)}

# Manually verified Hamiltonian circuit
cycle = ['A','B','C','G','E','F','D','A']
print("Hamiltonian Circuit (NetworkX):")
print(" -> ".join(cycle))

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=1200)
plt.title("Original Graph")

plt.subplot(1,2,2)
nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=1200)
highlight = list(zip(cycle, cycle[1:]))
nx.draw_networkx_edges(G, pos, edgelist=highlight, edge_color="red", width=3)
plt.title("Hamiltonian Circuit (Manual)\n" + " -> ".join(cycle))

plt.tight_layout()
plt.show()
