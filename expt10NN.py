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

def is_valid(v, path):
    if v not in G.neighbors(path[-1]): return False
    if v in path: return False
    return True

def hamiltonian(path):
    if len(path) == len(nodes):
        if path[0] in G.neighbors(path[-1]):
            return path + [path[0]]
        return None
    for v in nodes:
        if v not in path and is_valid(v, path):
            result = hamiltonian(path + [v])
            if result: return result
    return None

def find_cycle():
    for start in nodes:
        result = hamiltonian([start])
        if result: return result
    return None

print("Backtracking Algorithm - Finding Hamiltonian Circuit...")
cycle = find_cycle()

if cycle:
    print("\nHamiltonian Circuit FOUND:")
    print(" -> ".join(cycle))
    edges_cycle = list(zip(cycle, cycle[1:]))
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=1200)
    plt.title("Original Graph")
    plt.subplot(1,2,2)
    nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=1200)
    nx.draw_networkx_edges(G, pos, edgelist=edges_cycle, edge_color="red", width=3)
    plt.title("Hamiltonian Circuit (Backtracking)\n" + " -> ".join(cycle))
    plt.tight_layout()
    plt.show()
else:
    print("No Hamiltonian Circuit found")
