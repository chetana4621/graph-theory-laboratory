import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
G = nx.Graph()
G.add_nodes_from(["v1","v2","v3","v4","v5"])
nx.draw_circular(G, with_labels=True, node_color="lightgray", node_size=800)
plt.title("N5 (Null Graph)")

plt.subplot(2,3,2)
G = nx.complete_graph(["v1","v2","v3","v4","v5","v6"])
nx.draw_circular(G, with_labels=True, node_color="lightblue", node_size=800)
plt.title("K6 (Complete Graph)")

plt.subplot(2,3,3)
G = nx.path_graph(["v1","v2","v3","v4","v5"])
nx.draw(G, with_labels=True, node_color="lightgreen", node_size=800)
plt.title("P5 (Path Graph)")

plt.subplot(2,3,4)
G = nx.complete_bipartite_graph(3,4)
mapping = {0:"u1",1:"u2",2:"u3",3:"v1",4:"v2",5:"v3",6:"v4"}
G = nx.relabel_nodes(G, mapping)
pos = nx.bipartite_layout(G, ["u1","u2","u3"])
colors = ["orange" if node.startswith("u") else "lightblue" for node in G.nodes()]
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=800)
plt.title("K3,4 (Bipartite Graph)")

plt.subplot(2,3,5)
G = nx.cycle_graph(["v1","v2","v3","v4","v5","v6","v7","v8"])
nx.draw_circular(G, with_labels=True, node_color="pink", node_size=800)
plt.title("C8 (Cycle Graph)")

plt.subplot(2,3,6)
G = nx.Graph()
G.add_nodes_from(["c","v1","v2","v3","v4","v5"])
edges = [("v1","v2"),("v2","v3"),("v3","v4"),("v4","v5"),("v5","v1")]
G.add_edges_from(edges)
for v in ["v1","v2","v3","v4","v5"]:
    G.add_edge("c", v)
pos = nx.circular_layout(["v1","v2","v3","v4","v5"])
pos["c"] = [0,0]
colors = ["red" if node=="c" else "yellow" for node in G.nodes()]
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=900)
plt.title("W6 (Wheel Graph)")

plt.tight_layout()
plt.show()
