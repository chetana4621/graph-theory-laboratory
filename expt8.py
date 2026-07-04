import networkx as nx
import matplotlib.pyplot as plt
import random

def convert(G, path):
    result = []
    for i in range(len(path)-1):
        u, v = path[i], path[i+1]
        if G.has_edge(u, v):
            result.append(str(u))
            result.append(G[u][v]['label'])
    result.append(str(path[-1]))
    return " -> ".join(result)

def closed_path(G):
    cycles = nx.cycle_basis(G)
    if not cycles: return None
    c = cycles[0]; return c + [c[0]]

def closed_trail(G):
    if nx.is_eulerian(G):
        euler = list(nx.eulerian_circuit(G))
        path = [euler[0][0]]
        for u,v in euler: path.append(v)
        return path
    return None

def closed_walk(G):
    cycles = nx.cycle_basis(G)
    if not cycles: return None
    c = cycles[0]
    return c + c[:2] + [c[0]]

def show_results(G, name):
    print(f"\n{name}")
    cp = closed_path(G)
    ct = closed_trail(G)
    cw = closed_walk(G)
    print("Closed Path  =", convert(G, cp) if cp else "Not Found")
    print("Closed Trail =", convert(G, ct) if ct else "Graph is not Eulerian")
    print("Closed Walk  =", convert(G, cw) if cw else "Not Found")

edges1 = [
    ('A','B','E1'),('A','D','E4'),('B','D','E3'),('B','C','E2'),
    ('B','F','E8'),('D','F','E7'),('D','E','E5'),('F','E','E6'),
    ('F','C','E9'),('C','E','E10')
]
edges2 = edges1 + [('C','G','E11'),('E','G','E12')]

G1 = nx.Graph()
for u,v,w in edges1: G1.add_edge(u,v,label=w)

G2 = nx.Graph()
for u,v,w in edges2: G2.add_edge(u,v,label=w)

show_results(G1, "GRAPH 1")
show_results(G2, "GRAPH 2")

pos1 = {'B':(0,2),'C':(2,2),'A':(-1,1),'F':(1,1),'D':(0,0),'E':(2,0)}
pos2 = {'B':(0,2),'C':(2,2),'A':(-1,1),'F':(1,1),'D':(0,0),'E':(2,0),'G':(3,1)}

plt.figure(figsize=(12,5))
plt.subplot(121)
nx.draw(G1, pos1, with_labels=True, node_size=2000, node_color="green")
nx.draw_networkx_edge_labels(G1, pos1, edge_labels={(u,v):d['label'] for u,v,d in G1.edges(data=True)})
plt.title("Graph 1")
plt.subplot(122)
nx.draw(G2, pos2, with_labels=True, node_size=2000, node_color="red")
nx.draw_networkx_edge_labels(G2, pos2, edge_labels={(u,v):d['label'] for u,v,d in G2.edges(data=True)})
plt.title("Graph 2")
plt.tight_layout()
plt.show()
