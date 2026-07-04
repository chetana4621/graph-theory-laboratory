import networkx as nx
import matplotlib.pyplot as plt

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

def degree_sequence(G):
    return sorted([G.degree(n) for n in G.nodes()])

def find_cycles(adj):
    cycles = set()
    for u in adj:
        for v in adj[u]:
            for w in adj[v]:
                if w != u and u in adj[w]:
                    cycles.add(tuple(sorted([u,v,w])))
    return list(cycles)

def graph_properties(G, name):
    print(f"\nProperties of {name}:")
    print("Vertices:", G.number_of_nodes())
    print("Edges:", G.number_of_edges())
    print("Degree Sequence:", degree_sequence(G))
    adj = {}
    for u,v in G.edges():
        adj.setdefault(u,[]).append(v); adj.setdefault(v,[]).append(u)
    cycles = find_cycles(adj)
    print("Triangles found:", len(cycles))

def check_isomorphic(G1, G2):
    if G1.number_of_nodes() != G2.number_of_nodes(): return False
    if G1.number_of_edges() != G2.number_of_edges(): return False
    if degree_sequence(G1) != degree_sequence(G2): return False
    return True

graph_properties(G1, "Graph 1")
graph_properties(G2, "Graph 2")

if check_isomorphic(G1, G2):
    print("\nGraphs are ISOMORPHIC (Degree Sequence Method)")
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
