import networkx as nx
import matplotlib.pyplot as plt

edges = [
    ('A','B',32),('A','D',15),('A','C',20),('B','D',30),('B','G',18),
    ('C','D',10),('C','F',42),('D','F',53),('D','E',47),
    ('E','F',45),('E','G',24),('E','H',20),('G','H',18)
]
pos = {'A':(0,1),'B':(1,2),'C':(1,0),'D':(2,1),'E':(3,1),'F':(3,0),'G':(3,2),'H':(5,1)}

G = nx.Graph()
G.add_weighted_edges_from(edges)

mst = nx.minimum_spanning_tree(G, algorithm='kruskal')
cost = sum(w for _,_,w in mst.edges.data('weight'))

print("MST Edges:")
for u,v,w in sorted(mst.edges.data('weight'), key=lambda x: x[2]):
    print(f"  {u} -- {v}: {w}")
print(f"\nTotal MST Cost = {cost}")

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G,'weight'))
plt.title("Original Graph")

plt.subplot(1,2,2)
nx.draw(mst, pos, with_labels=True, node_color='lightgreen', node_size=700)
nx.draw_networkx_edge_labels(mst, pos, edge_labels=nx.get_edge_attributes(mst,'weight'))
plt.title("Minimum Spanning Tree")

plt.figtext(0.5, 0.02, f"Total MST Cost = {cost}", ha='center', fontsize=14)
plt.tight_layout(rect=[0,0.05,1,1])
plt.show()
