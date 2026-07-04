import networkx as nx
import matplotlib.pyplot as plt
import math

edges = [
    ('A','B',32),('A','D',15),('A','C',20),('B','D',30),('B','G',18),
    ('C','D',10),('C','F',42),('D','F',53),('D','E',47),
    ('E','F',45),('E','G',24),('E','H',20),('G','H',18)
]
pos = {'A':(0,1),'B':(1,2),'C':(1,0),'D':(2,1),'F':(3,0),'E':(3,1),'G':(3,2),'H':(5,1)}

edges_sorted = sorted(edges, key=lambda x: x[2])

parent = {}
nodes = set()
for u,v,w in edges:
    nodes.add(u); nodes.add(v)
for n in nodes:
    parent[n] = n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

mst_edges = []
steps = []

print("Kruskal's Algorithm - Stepwise:\n")
for u,v,w in edges_sorted:
    if find(u) != find(v):
        union(u, v)
        mst_edges.append((u,v,w))
        steps.append(mst_edges.copy())
        print(f"  Add edge {u}--{v} (weight {w})")
    else:
        print(f"  Skip edge {u}--{v} (weight {w}) - would form cycle")

cost = sum(w for _,_,w in mst_edges)
print(f"\nTotal MST Cost = {cost}")

cols = 3
rows = math.ceil((len(steps)+1) / cols)
plt.figure(figsize=(cols*4, rows*3.5))

plt.subplot(rows, cols, 1)
G_orig = nx.Graph()
for u,v,w in edges:
    G_orig.add_edge(u,v,weight=w)
nx.draw(G_orig, pos, with_labels=True, node_size=700, node_color='lightblue', edge_color='black')
nx.draw_networkx_edge_labels(G_orig, pos, edge_labels=nx.get_edge_attributes(G_orig,'weight'))
plt.title("Original Graph"); plt.axis('off')

for i,step_edges in enumerate(steps):
    plt.subplot(rows, cols, i+2)
    temp = nx.Graph()
    for u,v,w in step_edges:
        temp.add_edge(u,v,weight=w)
    nx.draw_networkx_nodes(temp, pos, node_size=700, node_color='lightgreen')
    nx.draw_networkx_labels(temp, pos)
    nx.draw_networkx_edges(temp, pos, edgelist=[(u,v) for u,v,w in step_edges], edge_color='lightgray', width=2)
    ne = step_edges[-1]
    nx.draw_networkx_edges(temp, pos, edgelist=[(ne[0],ne[1])], edge_color='red', width=3)
    nx.draw_networkx_edge_labels(temp, pos, edge_labels=nx.get_edge_attributes(temp,'weight'))
    plt.title(f"Step {i+1}: Add {ne[0]}--{ne[1]}"); plt.axis('off')

plt.figtext(0.5, 0.02, f"Total MST Cost = {cost}", ha='center', fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0,0.05,1,1])
plt.show()
