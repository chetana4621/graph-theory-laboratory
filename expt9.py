import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
edges = [
    ('A','B','E1'),('A','D','E4'),('B','D','E3'),('B','C','E2'),
    ('B','F','E8'),('D','F','E7'),('D','E','E5'),('F','E','E6'),
    ('F','C','E9'),('C','E','E10'),('C','G','E11'),('E','G','E12')
]
for u,v,w in edges:
    G.add_edge(u, v, label=w)

pos = {'B':(0,2),'C':(2,2),'A':(-1,1),'F':(1,1),'D':(0,0),'E':(2,0),'G':(3,1)}

print("Checking for Eulerian Circuit:")
print("Degrees:", dict(G.degree()))
odd_vertices = [v for v in G.nodes() if G.degree(v) % 2 != 0]
print("Odd degree vertices:", odd_vertices if odd_vertices else "None")

fig = plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=1000, edge_color="black")
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u,v):d['label'] for u,v,d in G.edges(data=True)}, font_size=7)
plt.title("Original Graph")

plt.subplot(1,2,2)
if nx.is_eulerian(G):
    circuit = list(nx.eulerian_circuit(G))
    path = [circuit[0][0]] + [v for u,v in circuit]
    print("\nEulerian Circuit EXISTS")
    print("Circuit:", " -> ".join(path))
    DG = nx.DiGraph(); DG.add_edges_from(circuit)
    nx.draw(DG, pos, with_labels=True, node_color="plum", node_size=1000, edge_color="brown", arrows=True)
    plt.title("Eulerian Circuit")
else:
    print("\nNo Eulerian Circuit (some vertices have odd degree)")
    nx.draw(G, pos, with_labels=True, node_color="lightcoral", node_size=1000)
    plt.title("No Eulerian Circuit")

plt.tight_layout()
plt.show()
