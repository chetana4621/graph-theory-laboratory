import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nodes = ['A','B','C','D','E','F','G','H']
G.add_nodes_from(nodes)
edges = [
    ('A','B'),('A','C'),('A','E'),('A','G'),('A','H'),
    ('B','C'),('B','D'),('B','F'),('B','H'),
    ('C','D'),('C','E'),('C','G'),
    ('D','E'),('D','F'),('D','H'),
    ('E','F'),('E','G'),
    ('F','G'),('F','H'),('G','H')
]
G.add_edges_from(edges)
pos = {'A':(-2,1),'B':(-1,2),'C':(1,2),'D':(2,1),'E':(2,-1),'F':(1,-2),'G':(-1,-2),'H':(-2,-1)}

# Manual greedy colouring
vertex_colors = {}
colors = ['red','green','blue','yellow','orange','pink','cyan','purple']

print("Manual Greedy Graph Colouring:\n")
for node in G.nodes():
    neighbor_cols = {vertex_colors[n] for n in G.neighbors(node) if n in vertex_colors}
    c = 0
    while c in neighbor_cols: c += 1
    vertex_colors[node] = c
    print(f"  Vertex {node} -> Color {colors[c % len(colors)]}")

chromatic = max(vertex_colors.values()) + 1
print(f"\nChromatic Number χ(G) = {chromatic}")

node_colors = [colors[vertex_colors[n] % len(colors)] for n in G.nodes()]

plt.figure(figsize=(8,8))
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1200,
        font_size=14, font_weight='bold', edgecolors='black')
plt.title(f"Graph Colouring (Manual Greedy)  |  χ(G) = {chromatic}")
plt.axis('off')
plt.show()
