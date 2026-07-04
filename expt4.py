import networkx as nx
import matplotlib.pyplot as plt

degree_sequence = [7, 6, 5, 5, 4, 3, 2, 2]
print("Degree Sequence:", degree_sequence)
print("Sum:", sum(degree_sequence))

G = nx.havel_hakimi_graph(degree_sequence)

print("\nGraph generated successfully.")
print("Number of vertices:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("\nDegrees of vertices:")
for node, degree in G.degree():
    print(f"  Node {node}: Degree {degree}")

pos = nx.circular_layout(G)
plt.figure(figsize=(6,6))
nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=700, edge_color="black", width=2)
plt.title("Graph Generated using Havel-Hakimi Algorithm\nDegree Sequence: [7, 6, 5, 5, 4, 3, 2, 2]")
plt.show()
