import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import isomorphism

edges1 = [
    (1,2),(2,3),(3,4),(4,5),(5,6),(6,1),
    (1,3),(2,4),(3,5),(4,6),(5,1),(6,2)
]
edges2 = [
    ("A","B"),("A","C"),("B","C"),
    ("A","D"),("A","E"),
    ("D","E"),("D","F"),("E","F"),
    ("B","D"),("B","F"),
    ("C","E"),("C","F")
]

G1 = nx.Graph(); G1.add_edges_from(edges1)
G2 = nx.Graph(); G2.add_edges_from(edges2)

def graph_properties(G, name):
    print(f"\nProperties of {name}:")
    print("Number of vertices:", G.number_of_nodes())
    print("Number of edges:", G.number_of_edges())
    print("Degrees:", dict(G.degree()))
    cycles = nx.cycle_basis(G)
    print("Number of cycles:", len(cycles))

graph_properties(G1, "Graph 1")
graph_properties(G2, "Graph 2")

GM = isomorphism.GraphMatcher(G1, G2)
if GM.is_isomorphic():
    print("\nGraphs are ISOMORPHIC")
    print("Bijection Mapping:")
    for k,v in GM.mapping.items():
        print(f"  {k} -> {v}")
else:
    print("\nGraphs are NOT ISOMORPHIC")

pos1 = {1:(0,1),2:(1,0.5),3:(1,-0.5),4:(0,-1),5:(-1,-0.5),6:(-1,0.5)}
pos2 = {"A":(0,3),"B":(-3,0),"C":(3,0),"D":(-1,1.5),"E":(1,1.5),"F":(0,0.8)}

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
nx.draw(G1, pos1, with_labels=True, node_size=800, node_color="lightblue", edge_color="black", width=2)
plt.title("Graph 1")
plt.subplot(1,2,2)
nx.draw(G2, pos2, with_labels=True, node_size=800, node_color="lightgreen", edge_color="black", width=2)
plt.title("Graph 2")
plt.tight_layout()
plt.show()
