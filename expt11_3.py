import networkx as nx
import matplotlib.pyplot as plt
import copy

# Sudoku as Graph Colouring
sudoku = [[0,0,0,2],[2,0,0,0],[0,0,0,0],[0,0,2,0]]
unsolved = copy.deepcopy(sudoku)
SIZE = 4; SUBGRID = 2
colors = {1:"red",2:"blue",3:"green",4:"yellow"}

def is_valid(board, row, col, num):
    for x in range(SIZE):
        if board[row][x] == num or board[x][col] == num: return False
    sr = row - row%SUBGRID; sc = col - col%SUBGRID
    for i in range(SUBGRID):
        for j in range(SUBGRID):
            if board[sr+i][sc+j] == num: return False
    return True

def solve(board):
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == 0:
                for num in range(1, SIZE+1):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board): return True
                        board[row][col] = 0
                return False
    return True

print("Initial Sudoku:")
for row in unsolved: print(" ", row)

solve(sudoku)

print("\nSolved Sudoku:")
for row in sudoku: print(" ", row)

G = nx.Graph()
for r in range(SIZE):
    for c in range(SIZE): G.add_node((r,c))
for r in range(SIZE):
    for c in range(SIZE):
        for k in range(SIZE):
            if k!=c: G.add_edge((r,c),(r,k))
            if k!=r: G.add_edge((r,c),(k,c))
        sr=r-r%SUBGRID; sc=c-c%SUBGRID
        for i in range(sr,sr+SUBGRID):
            for j in range(sc,sc+SUBGRID):
                if (i,j)!=(r,c): G.add_edge((r,c),(i,j))

pos = {(r,c):(c,-r) for r in range(SIZE) for c in range(SIZE)}
labels_u = {(r,c):str(unsolved[r][c]) if unsolved[r][c]!=0 else "" for r in range(SIZE) for c in range(SIZE)}
labels_sol = {(r,c):str(sudoku[r][c]) for r in range(SIZE) for c in range(SIZE)}
node_colors_s = [colors[sudoku[r][c]] for r in range(SIZE) for c in range(SIZE)]

fig, axes = plt.subplots(1, 2, figsize=(14,7))
nx.draw(G, pos, ax=axes[0], with_labels=True, labels=labels_u, node_color="lightgray", node_size=1200, font_size=14)
axes[0].set_title("Unsolved Sudoku")
nx.draw(G, pos, ax=axes[1], with_labels=True, labels=labels_sol, node_color=node_colors_s, node_size=1200, font_size=14)
axes[1].set_title("Solved Sudoku (Graph Coloured)")
plt.tight_layout()
plt.show()
