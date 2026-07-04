import networkx as nx
import matplotlib.pyplot as plt
import math

degree_sequence = [7, 6, 5, 5, 4, 3, 2, 2]
n = len(degree_sequence)

G = nx.Graph()
G.add_nodes_from(range(n))

deg_list = [(degree_sequence[i], i) for i in range(n)]

graphs = []
titles = []
step = 1

print("Degree Sequence:", degree_sequence)
print("\nHavel-Hakimi Stepwise Construction:\n")

while True:
    deg_list.sort(reverse=True)
    if all(d == 0 for d, _ in deg_list):
        break
    d, v = deg_list[0]
    deg_list = deg_list[1:]
    if d > len(deg_list):
        print("Invalid Degree Sequence")
        break
    print(f"Step {step}: Connect vertex {v} (degree {d}) to next {d} vertices")
    for i in range(d):
        deg, u = deg_list[i]
        G.add_edge(v, u)
        deg_list[i] = (deg - 1, u)
    graphs.append(G.copy())
    titles.append(f"Step {step}")
    step += 1

graphs.append(G.copy())
titles.append("Final Graph")

print("\nFinal degrees:")
for node, degree in G.degree():
    print(f"  Node {node}: Degree {degree}")

cols = 2
rows = math.ceil(len(graphs) / cols)
fig, axes = plt.subplots(rows, cols, figsize=(12, rows * 5))
if rows == 1:
    axes = list(axes)
else:
    axes = axes.flatten()

pos = nx.circular_layout(G)
for i in range(len(graphs)):
    nx.draw(graphs[i], pos, ax=axes[i], with_labels=True,
            node_color="lightgreen", node_size=700, edge_color="black", width=2)
    axes[i].set_title(titles[i])
for i in range(len(graphs), len(axes)):
    axes[i].axis("off")

plt.suptitle("Havel-Hakimi Stepwise Construction", fontsize=16)
plt.tight_layout()
plt.show()
