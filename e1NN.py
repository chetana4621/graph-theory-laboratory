import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
G = nx.Graph()
G.add_nodes_from(["v1","v2","v3","v4","v5"])
nx.draw_circular(G, with_labels=True, node_color="lightgray", node_size=800)
plt.title("N5 (Null Graph)")

plt.subplot(2,3,2)
G = nx.Graph()
nodes = ["v1","v2","v3","v4","v5","v6"]
G.add_nodes_from(nodes)
for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        G.add_edge(nodes[i], nodes[j])
nx.draw_circular(G, with_labels=True, node_color="lightblue", node_size=800)
plt.title("K6 (Complete Graph)")

plt.subplot(2,3,3)
G = nx.Graph()
nodes = ["v1","v2","v3","v4","v5"]
G.add_nodes_from(nodes)
for i in range(len(nodes)-1):
    G.add_edge(nodes[i], nodes[i+1])
nx.draw(G, with_labels=True, node_color="lightgreen", node_size=800)
plt.title("P5 (Path Graph)")

plt.subplot(2,3,4)
G = nx.Graph()
U = ["u1","u2","u3"]; V = ["v1","v2","v3","v4"]
G.add_nodes_from(U); G.add_nodes_from(V)
for u in U:
    for v in V:
        G.add_edge(u, v)
pos = nx.bipartite_layout(G, U)
colors = ["orange" if node.startswith("u") else "lightblue" for node in G.nodes()]
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=800)
plt.title("K3,4 (Bipartite Graph)")

plt.subplot(2,3,5)
G = nx.Graph()
nodes = ["v1","v2","v3","v4","v5","v6","v7","v8"]
G.add_nodes_from(nodes)
for i in range(len(nodes)-1):
    G.add_edge(nodes[i], nodes[i+1])
G.add_edge(nodes[-1], nodes[0])
nx.draw_circular(G, with_labels=True, node_color="pink", node_size=800)
plt.title("C8 (Cycle Graph)")

plt.subplot(2,3,6)
G = nx.Graph()
outer = ["v1","v2","v3","v4","v5"]
G.add_nodes_from(["c"] + outer)
for i in range(len(outer)-1):
    G.add_edge(outer[i], outer[i+1])
G.add_edge(outer[-1], outer[0])
for v in outer:
    G.add_edge("c", v)
pos = nx.circular_layout(outer)
pos["c"] = [0,0]
colors = ["red" if node=="c" else "yellow" for node in G.nodes()]
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=900)
plt.title("W6 (Wheel Graph)")

plt.tight_layout()
plt.show()
