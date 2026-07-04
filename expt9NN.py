import networkx as nx
import matplotlib.pyplot as plt

def count_components(G):
    visited = set(); count = 0
    for node in G.nodes():
        if node not in visited:
            stack = [node]; count += 1
            while stack:
                u = stack.pop()
                if u not in visited:
                    visited.add(u)
                    for v in G[u]:
                        if v not in visited: stack.append(v)
    return count

def is_bridge(G, u, v):
    if G.degree(u) == 1: return False
    before = count_components(G)
    G.remove_edge(u, v)
    after = count_components(G)
    G.add_edge(u, v)
    return after > before

def fleury(G_orig):
    G = G_orig.copy()
    odd_nodes = [v for v in G.nodes() if G.degree(v) % 2 != 0]
    if len(odd_nodes) != 0:
        return None, []
    curr = list(G.nodes())[0]; path = [curr]; steps = []
    steps.append((G.copy(), list(path), None))
    while G.number_of_edges() > 0:
        neighbors = list(G.neighbors(curr)); chosen = None
        for n in neighbors:
            if not is_bridge(G, curr, n): chosen = n; break
        if chosen is None: chosen = neighbors[0]
        edge_taken = (curr, chosen)
        G.remove_edge(curr, chosen); curr = chosen; path.append(curr)
        steps.append((G.copy(), list(path), edge_taken))
    return path, steps

G1 = nx.Graph()
edges = [
    ('A','B'),('B','C'),('B','D'),('A','D'),
    ('D','E'),('E','F'),('D','F'),('B','F'),
    ('C','F'),('C','E'),('C','G'),('E','G')
]
G1.add_edges_from(edges)

pos1 = {'B':(0,2),'C':(2,2),'A':(-1,1),'F':(1,1),'D':(0,0),'E':(2,0),'G':(3,1)}

print("Fleury's Algorithm - Manual Implementation")
print("Degrees:", dict(G1.degree()))

path, steps = fleury(G1)

if not steps:
    print("No Eulerian Circuit (odd degree vertices exist)")
else:
    print("Eulerian Circuit:", " -> ".join(map(str, path)))

    num_steps = min(len(steps), 6)
    cols = 3; rows = 2
    plt.figure(figsize=(15, 8))

    for i in range(num_steps):
        g_state, current_path, edge = steps[i]
        ax = plt.subplot(rows, cols, i+1)
        nx.draw_networkx_nodes(G1, pos1, node_color='lightblue', ax=ax, node_size=500)
        nx.draw_networkx_labels(G1, pos1, ax=ax)
        nx.draw_networkx_edges(g_state, pos1, ax=ax, edge_color='black', width=2)
        walk_edges = [(current_path[j], current_path[j+1]) for j in range(len(current_path)-1)]
        nx.draw_networkx_edges(G1, pos1, edgelist=walk_edges, edge_color='red', width=2, ax=ax)
        title = "Start" if i == 0 else f"Step {i}: {edge[0]}→{edge[1]}"
        ax.set_title(title); ax.axis("off")

    plt.suptitle(f"Fleury's Algorithm\nFinal Circuit: {' -> '.join(map(str, path))}", fontsize=12)
    plt.tight_layout()
    plt.show()
