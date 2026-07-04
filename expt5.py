import networkx as nx
import matplotlib.pyplot as plt
import math

G = nx.Graph()
edges = [
    ('0','1','e1'),('0','7','e2'),('7','1','e3'),('1','2','e4'),
    ('7','8','e5'),('7','6','e6'),('2','8','e7'),('6','8','e8'),
    ('6','5','e9'),('2','5','e10'),('2','3','e11'),('5','4','e12'),('3','4','e13')
]
for u,v,label in edges:
    G.add_edge(u, v, label=label)

pos = {
    '0':(0,1.5),'1':(0.5,2),'7':(0.5,0.7),'8':(1.4,1.5),
    '6':(1.4,0.7),'2':(1.4,2),'5':(2,0.7),'3':(2,2),'4':(2.5,1.5)
}

edge_label_map = {}
edge_list = []
for u,v,d in G.edges(data=True):
    edge_label_map[(u,v)] = d['label']
    edge_label_map[(v,u)] = d['label']
    edge_list.append((u,v))

L = nx.Graph()
steps = []
for i in range(len(edge_list)):
    e1 = edge_list[i]; label1 = edge_label_map[e1]
    L.add_node(label1); new_edges = []
    for j in range(i):
        e2 = edge_list[j]; label2 = edge_label_map[e2]
        if (e1[0] in e2) or (e1[1] in e2):
            L.add_edge(label1, label2); new_edges.append((label1, label2))
    steps.append((list(L.nodes()), list(L.edges()), new_edges))

pos_L = nx.spring_layout(L, seed=42, k=0.7)

total_plots = len(steps) + 1
cols = 4
rows = math.ceil(total_plots / cols)

plt.figure(figsize=(cols*4, rows*3.5))

plt.subplot(rows, cols, 1)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue')
edge_labels = {(u,v):d['label'] for u,v,d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
plt.title("Original Graph", fontsize=10)

for i,(nodes,all_edges,new_edges) in enumerate(steps):
    plt.subplot(rows, cols, i+2)
    temp = nx.Graph()
    temp.add_nodes_from(nodes); temp.add_edges_from(all_edges)
    nx.draw(temp, pos_L, with_labels=True, node_size=500, edge_color='black')
    nx.draw_networkx_edges(temp, pos_L, edgelist=new_edges, edge_color='red', width=2)
    plt.title(f"Step {i+1}", fontsize=9)

plt.subplots_adjust(left=0.05, right=0.98, top=0.95, bottom=0.05, wspace=0.35, hspace=0.5)
plt.show()
