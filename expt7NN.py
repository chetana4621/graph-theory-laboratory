import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
edges = [
    ('A','B',6),('A','G',15),('B','C',11),('C','G',25),
    ('G','F',12),('F','E',10),('E','D',22),('D','B',5),
    ('C','D',21),('C','F',9)
]
G.add_weighted_edges_from(edges)

pos = {'A':(-2,0),'B':(-1,2),'C':(0,0),'D':(1,2),'E':(2,0),'F':(1,-2),'G':(-1,-2)}

source, target = 'A', 'E'
nodes_list = ['A','B','C','D','E','F','G']

dist = {n: float('inf') for n in nodes_list}
prev = {n: None for n in nodes_list}
dist[source] = 0
visited = set()

print("Manual Dijkstra's Algorithm:\n")
print(f"{'Step':<6}{'Visited':<30}" + "".join([f"{v:<8}" for v in nodes_list]))
print("-"*80)

while len(visited) < len(nodes_list):
    u = min((n for n in nodes_list if n not in visited), key=lambda x: dist[x])
    visited.add(u)
    for v in G.neighbors(u):
        w = G[u][v]['weight']
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            prev[v] = u
    row = f"{u:<6}{' '.join(visited):<30}"
    for v in nodes_list:
        val = dist[v] if dist[v] != float('inf') else '∞'
        row += f"{val:<8}"
    print(row)

# Reconstruct path
path = []; cur = target
while cur is not None:
    path.append(cur); cur = prev[cur]
path.reverse()

print(f"\nShortest Path: {' -> '.join(path)}")
print(f"Total Distance: {dist[target]}")

path_edges = list(zip(path, path[1:]))
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightgray', font_size=12)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G,'weight'), font_size=10)
plt.title("Original Graph"); plt.axis('off')

plt.subplot(1,2,2)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightgray', font_size=12)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G,'weight'), font_size=10)
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
plt.title(f"Shortest Path (Manual): {' -> '.join(path)}"); plt.axis('off')

plt.tight_layout()
plt.show()
