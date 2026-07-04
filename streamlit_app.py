import streamlit as st
import os
import sys
import importlib.util
from io import StringIO
import traceback
import matplotlib.pyplot as plt

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Graph Theory Laboratory",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

/* Entire App */
.stApp {
    background: linear-gradient(135deg, #0f0c29 0%, #1a1040 50%, #0d0d1a 100%);
    color: #e2e0f0;
    overflow-x: hidden;
    padding-top: 90px;
    padding-bottom: 50px;
    font-family: 'Inter', sans-serif;
}

.footer-fixed {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: rgba(15, 12, 41, 0.95);
    color: #c4b5fd;
    text-align: center;
    padding: 12px;
    border-top: 1px solid rgba(139, 92, 246, 0.3);
    z-index: 9999;
    backdrop-filter: blur(10px);
    font-family: 'Inter', sans-serif;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(15, 12, 41, 0.97);
    border-right: 1px solid rgba(139, 92, 246, 0.2);
    margin-top: 76px !important;
}

/* Main content area */
[data-testid="stMainBlockContainer"] {
    padding-top: 30px !important;
}

/* Sidebar radio */
div[role="radiogroup"] > label {
    background: rgba(139, 92, 246, 0.06);
    padding: 12px 15px;
    margin-bottom: 8px;
    border-radius: 12px;
    border: 1px solid rgba(139, 92, 246, 0.12);
    transition: all 0.25s ease;
    color: #c4b5fd !important;
}

div[role="radiogroup"] > label:hover {
    background: rgba(139, 92, 246, 0.18);
    border-color: rgba(139, 92, 246, 0.4);
    transform: translateX(4px);
}

/* Main title */
.main-title {
    font-size: 48px;
    font-weight: 800;
    background: linear-gradient(90deg, #a78bfa, #f59e0b, #a78bfa);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 4s linear infinite;
    margin-bottom: 8px;
    letter-spacing: -1px;
}

@keyframes shimmer {
    to { background-position: 200% center; }
}

/* Subtitle */
.subtitle {
    color: #9ca3af;
    font-size: 16px;
    margin-bottom: 12px;
    line-height: 1.6;
    max-width: 700px;
    padding-bottom: 18px;
    border-bottom: 1px solid rgba(139, 92, 246, 0.15);
}

/* Sticky Header */
.sticky-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 9999;
    background: rgba(15, 12, 41, 0.92);
    padding: 14px 24px;
    border-bottom: 1px solid rgba(139, 92, 246, 0.25);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
}

.header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
}

.header-left h1 {
    margin: 0;
    font-size: 26px;
}

.header-right {
    text-align: right;
    font-size: 13px;
    color: #a78bfa;
    line-height: 1.5;
}

.header-right .header-name {
    color: #e2e0f0;
    font-weight: 600;
    font-size: 14px;
}

.header-right .header-count {
    color: #f59e0b;
    font-weight: 600;
    letter-spacing: 0.3px;
}

.header-right p {
    margin: 2px 0;
}

/* Field labels (Aim / Date) */
.field-label {
    display: inline-block;
    color: #f59e0b;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-right: 8px;
}

/* Cards */
.card {
    background: rgba(139, 92, 246, 0.07);
    border: 1px solid rgba(139, 92, 246, 0.18);
    border-radius: 16px;
    padding: 24px 28px;
    margin-top: 8px;
    margin-bottom: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0 4px 24px rgba(139, 92, 246, 0.12), 0 1px 4px rgba(0,0,0,0.3);
    transition: box-shadow 0.3s ease;
}

.card p {
    line-height: 1.7;
    max-width: 900px;
}

.card:hover {
    box-shadow: 0 8px 32px rgba(139, 92, 246, 0.2), 0 2px 8px rgba(0,0,0,0.4);
}

/* Small section-title cards sitting right above a tab group */
.card-tight {
    background: rgba(139, 92, 246, 0.07);
    border: 1px solid rgba(139, 92, 246, 0.18);
    border-left: 3px solid #f59e0b;
    border-radius: 12px;
    padding: 14px 20px;
    margin-bottom: 16px;
}

.card-tight h3 {
    margin: 0;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 10px;
    background: linear-gradient(90deg, #7c3aed, #a855f7);
    color: white;
    border: none;
    padding: 12px 20px;
    font-weight: 600;
    font-size: 14px;
    letter-spacing: 0.3px;
    transition: all 0.25s ease;
    font-family: 'Inter', sans-serif;
    box-shadow: 0 4px 14px rgba(124, 58, 237, 0.35);
}

.stButton > button:hover {
    transform: translateY(-2px);
    background: linear-gradient(90deg, #8b5cf6, #c084fc);
    box-shadow: 0 6px 20px rgba(139, 92, 246, 0.5);
}

.stButton > button:active {
    transform: translateY(0);
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    background: rgba(139, 92, 246, 0.06);
    border-radius: 10px;
    margin-right: 8px;
    padding: 10px 22px;
    border: 1px solid rgba(139, 92, 246, 0.1);
    color: #9ca3af;
    transition: all 0.2s ease;
}

.stTabs [data-baseweb="tab"]:hover {
    background: rgba(139, 92, 246, 0.12);
    color: #e2e0f0;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(90deg, #7c3aed, #8b5cf6) !important;
    color: white !important;
    border-color: transparent !important;
    box-shadow: 0 4px 12px rgba(124, 58, 237, 0.4);
}

/* Code */
pre {
    border-radius: 14px !important;
    border: 1px solid rgba(139, 92, 246, 0.18) !important;
    background: rgba(10, 8, 30, 0.85) !important;
    box-shadow: 0 4px 20px rgba(139, 92, 246, 0.08) !important;
    font-family: 'JetBrains Mono', monospace !important;
}

/* Output Box */
.output-box {
    background: rgba(10, 8, 30, 0.9);
    border: 1px solid rgba(245, 158, 11, 0.25);
    padding: 16px 18px;
    border-radius: 12px;
    color: #fbbf24;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    white-space: pre-wrap;
    line-height: 1.6;
    box-shadow: inset 0 2px 8px rgba(0,0,0,0.3);
}

/* Headers */
h1, h2, h3 {
    color: #e2e0f0 !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 700 !important;
}

h2 {
    font-size: 22px !important;
    color: #c4b5fd !important;
}

h3 {
    font-size: 16px !important;
    color: #a78bfa !important;
    letter-spacing: 0.3px;
}

/* Sidebar heading */
.css-1629p8f h1, .css-1629p8f h2, .css-1629p8f h3 {
    color: #c4b5fd !important;
}

/* Hide Streamlit menu/footer */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 6px;
}
::-webkit-scrollbar-track {
    background: rgba(255,255,255,0.03);
}
::-webkit-scrollbar-thumb {
    background: rgba(139, 92, 246, 0.35);
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
    background: rgba(139, 92, 246, 0.6);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# EXPERIMENT FILES
# ---------------------------------------------------

exp_dir = os.path.dirname(os.path.abspath(__file__))

experiments = {
    1: {
        "title": "Graph Creation",
        "aim": "To implement basic graphs such as null graph, complete graph, cycle graph, path graph, complete bipartite graph and wheel graph.",
        "date": "3/2/26",
        "theory": "<p><strong>Introduction to Graphs:</strong> A graph is a mathematical structure used to represent relationships between different objects. In graph theory, a graph is denoted as <strong>G = (V, E)</strong>, where <strong>V</strong> represents a set of vertices (also called nodes) and <strong>E</strong> represents a set of edges that connect pairs of vertices. Graphs are widely used in computer science, data structures, networking, social network analysis, transportation systems, and many other real-world applications where relationships between entities need to be modeled and analyzed.</p><p><strong>Types of Graphs:</strong></p><p><strong>1. Null Graph:</strong> A null graph contains a set of vertices but no edges. None of the vertices are connected to each other, representing completely independent or isolated elements. Denoted as having |V| vertices and |E| = 0 edges.</p><p><strong>2. Complete Graph:</strong> A complete graph is a simple graph where every pair of distinct vertices is connected by a unique edge. Each vertex is directly connected to every other vertex. A complete graph with <strong>n</strong> vertices is denoted <strong>K<sub>n</sub></strong> and contains <strong>n(n-1)/2</strong> edges. Complete graphs represent fully connected systems.</p><p><strong>3. Complete Bipartite Graph:</strong> A complete bipartite graph has a vertex set divided into two disjoint sets where every vertex of the first set connects to every vertex of the second set. Denoted <strong>K<sub>m,n</sub></strong>, it has <strong>m × n</strong> edges and models relationships between two different categories, such as students and courses.</p><p><strong>4. Cycle Graph:</strong> A cycle graph forms a closed loop where each vertex connects to exactly two other vertices forming a circular structure. A cycle graph with <strong>n</strong> vertices is denoted <strong>C<sub>n</sub></strong> and contains exactly <strong>n</strong> edges. Cycle graphs represent circular relationships or repeating processes.</p><p><strong>5. Wheel Graph:</strong> A wheel graph is formed by connecting a single central vertex to all vertices of a cycle graph, resembling a wheel with the cycle forming the rim and central vertex as the hub. Denoted <strong>W<sub>n</sub></strong>.</p><p><strong>6. Path Graph:</strong> A path graph arranges vertices in a linear sequence where each vertex connects to at most two other vertices (end vertices connect to only one). A path graph with <strong>n</strong> vertices is denoted <strong>P<sub>n</strong> and contains <strong>n-1</strong> edges. Path graphs represent linear structures such as chains of connected components.</p>",
        "nx": "e1.py",
        "nn": "e1NN.py"
    },
    2: {
        "title": "Graph Isomorphism",
        "aim": "To implement graph isomorphism verification in order to compare structural equivalence between graphs.",
        "date": "10/2/26",
        "theory": "<p><strong>Introduction to Graph Isomorphism:</strong> Graph isomorphism is a concept in graph theory used to check whether two graphs have the same structure even if the vertex labels are different. Two graphs are considered isomorphic when there is a one-to-one mapping between the vertices of the first graph and the vertices of the second graph. This mapping must maintain the connections between vertices. In other words, if two vertices are connected by an edge in the first graph, the corresponding vertices in the second graph must also be connected by an edge. Therefore, isomorphic graphs represent the same structural pattern, even though the vertices may be named or arranged differently. This concept is useful for comparing networks and determining whether they represent the same relationship structure.</p><p><strong>Properties of Isomorphic Graphs:</strong></p><p><strong>1. Equal Number of Vertices:</strong> For two graphs to be isomorphic, both must contain the same number of vertices. This is because a one-to-one correspondence must be created between the vertices of the two graphs. If one graph has more vertices than the other, such a mapping cannot exist, and therefore the graphs cannot be isomorphic.</p><p><strong>2. Equal Number of Edges:</strong> Isomorphic graphs must also have the same number of edges. Since the mapping between vertices preserves their connections, each edge in one graph must correspond to an edge in the other graph. If the number of edges is different, the connectivity structure of the graphs will not match.</p><p><strong>3. Same Degree Sequence:</strong> The degree of a vertex refers to the number of edges attached to it. In isomorphic graphs, the corresponding vertices must have identical degrees. Therefore, the list of vertex degrees (called the degree sequence) should be the same in both graphs. This indicates that the distribution of connections among vertices is similar.</p><p><strong>4. Adjacency Must Be Preserved:</strong> Another important property is that adjacency relationships remain unchanged. If two vertices are connected in the first graph, their mapped vertices must also be connected in the second graph. Likewise, if two vertices are not connected in one graph, they should also remain unconnected in the other graph.</p><p><strong>5. Different Labels but Identical Structure:</strong> Although isomorphic graphs may appear different due to different vertex labels or drawing styles, their internal structure is the same. The visual arrangement of vertices does not affect isomorphism; only the pattern of connections between vertices is important.</p>",
        "nx": "expt2.py",
        "nn": "expt2NN.py"
    },
    3: {
        "title": "Subgraph Generation",
        "aim": "To implement generation of various subgraphs such as induced subgraph, spanning subgraph and edge deleted subgraph.",
        "date": "17/2/26",
        "theory": "<p><strong>Introduction to Subgraphs:</strong> A subgraph is a graph that is formed from another graph by selecting some of its vertices and edges. If <strong>G = (V, E)</strong> is a graph, then a graph <strong>H = (V<sub>1</sub>, E<sub>1</sub>)</strong> is called a subgraph of G if <strong>V<sub>1</sub> ⊆ V</strong> and <strong>E<sub>1</sub> ⊆ E</strong>. This means the vertices and edges of the subgraph must come from the original graph. A subgraph cannot contain any new vertices or edges that are not present in the main graph. Subgraphs are useful in graph theory because they allow us to study a smaller part of a larger graph while maintaining the relationships between vertices. By analyzing subgraphs, we can understand specific structures or properties of the original graph.</p><p><strong>Types of Subgraphs:</strong></p><p><strong>1. Induced Subgraph:</strong> An induced subgraph is formed by choosing a subset of vertices from the original graph and including all the edges that exist between those selected vertices in the original graph. If <strong>G = (V, E)</strong> is a graph and <strong>S ⊆ V</strong>, then the induced subgraph <strong>G[S]</strong> consists of the vertex set S and all edges from E that connect pairs of vertices in S. In simple terms, once the vertices are selected, every edge between those vertices in the original graph must also appear in the induced subgraph. No such edges can be removed.</p><p><strong>2. Spanning Subgraph:</strong> A spanning subgraph is a subgraph that contains all the vertices of the original graph but only some of its edges. If <strong>G = (V, E)</strong> is a graph, then a spanning subgraph H will have the same vertex set V, but its edge set <strong>E<sub>1</sub> ⊆ E</strong>. This means the graph spans all vertices of the original graph but may have fewer edges. Spanning subgraphs are important in many applications, especially when studying spanning trees, which connect all vertices with the minimum number of edges.</p><p><strong>3. Edge Deleted Subgraph:</strong> An edge deleted subgraph is obtained by removing one or more edges from the original graph while keeping all vertices the same. If <strong>G = (V, E)</strong> is a graph and we remove an edge <strong>e</strong> from E, the resulting graph <strong>G − e</strong> is called an edge deleted subgraph. In this type of subgraph: the number of vertices remains unchanged and only the number of edges is reduced. Edge deleted subgraphs are useful when studying how the structure of a graph changes when certain connections are removed.</p>",
        "nx": "expt3.py",
        "nn": "expt3NN.py"
    },
    4: {
        "title": "Graphical Sequence",
        "aim": "To implement construction of a graph for a given degree sequence, verifying the sequence is graphical.",
        "date": "23/2/26",
        "theory": "<p><strong>Introduction to Degree Sequences:</strong> A degree sequence of a graph is a list that represents the degrees of all the vertices in that graph. The degree of a vertex indicates how many edges are connected to it. Usually, this list is written in non-increasing order, meaning the highest degree appears first. For example, if a graph has five vertices whose degrees are 3, 2, 2, 1, and 0, the degree sequence can be written as <strong>(3, 2, 2, 1, 0)</strong>. Degree sequences are useful in graph theory because they provide information about how vertices are connected in a graph and help determine whether such a graph can actually exist. If a sequence can correspond to at least one valid graph, it is known as a <strong>graphical sequence</strong>.</p><p><strong>Fundamental Rule:</strong> An important rule related to degree sequences is that the sum of all vertex degrees must be an even number, since each edge contributes one degree to two different vertices. This rule is essential for determining whether a given sequence can be graphical. Formally, for a degree sequence <strong>d<sub>1</sub>, d<sub>2</sub>, ..., d<sub>n</sub></strong>, we must have <strong>∑d<sub>i</sub></strong> is even.</p><p><strong>Constructing Graphs from Degree Sequences:</strong> To build a graph from a given degree sequence, vertices are first assigned according to the sequence and edges are added so that each vertex achieves the required degree. One common technique used for this purpose is the <strong>Havel–Hakimi method</strong>. In this approach, the sequence is first arranged in decreasing order. The vertex with the largest degree is then connected to the next set of vertices equal to its degree value. After making these connections, the degrees of those vertices are reduced by one. The updated sequence is again rearranged in descending order and the same step is repeated. If during this process a negative value appears or the connections cannot be completed, the sequence cannot represent a graph. However, if the sequence eventually becomes all zeros, it means the graph has been successfully constructed.</p>",
        "nx": "expt4.py",
        "nn": "expt4NN.py"
    },
    5: {
        "title": "Line Graph Transformation",
        "aim": "Convert the original graph into its line graph, where each edge of the original graph becomes a vertex in the new graph, and adjacency is defined by shared endpoints in the original graph.",
        "date": "10/3/26",
        "theory": "<p><strong>Introduction to Line Graphs:</strong> Let <strong>G = (V, E)</strong> be a simple graph, where <strong>V</strong> is the set of vertices and <strong>E</strong> is the set of edges. The line graph of G, denoted by <strong>L(G)</strong>, is a graph formed from G in such a way that each edge of G becomes a vertex in L(G). This transformation provides a unique perspective on the original graph by shifting focus from the relationships between vertices to the relationships between edges.</p><p><strong>Definition and Adjacency:</strong> In the line graph L(G), two vertices are connected if their corresponding edges in the original graph G share a common vertex. In simple words, if two edges in G are touching or incident, then in L(G), those edges are represented as vertices and are joined by an edge. The concept of connection is fundamentally shifted from vertices to edges, creating a dual representation of the original graph structure.</p><p><strong>Mathematical Formulation:</strong> If <strong>G = (V, E)</strong> is a graph, then the line graph is formally defined as <strong>L(G) = (V', E')</strong>, where <strong>V' = E</strong> (the vertex set of the line graph equals the edge set of the original graph) and <strong>E' = {(e<sub>1</sub>, e<sub>2</sub>) | e<sub>1</sub> and e<sub>2</sub> share a common vertex in G}</strong>. This means that every edge in G is converted into a vertex in L(G), and adjacency between edges in G becomes adjacency between vertices in L(G).</p><p><strong>Illustrative Example:</strong> Consider three edges <strong>e<sub>1</sub> = (u, v)</strong>, <strong>e<sub>2</sub> = (v, w)</strong>, and <strong>e<sub>3</sub> = (w, x)</strong> in the original graph G. Here, <strong>e<sub>1</sub></strong> and <strong>e<sub>2</sub></strong> share vertex v, and <strong>e<sub>2</sub></strong> and <strong>e<sub>3</sub></strong> share vertex w. Therefore, in the line graph L(G), the vertex representing <strong>e<sub>1</sub></strong> is connected to the vertex representing <strong>e<sub>2</sub></strong>, and the vertex representing <strong>e<sub>2</sub></strong> is connected to the vertex representing <strong>e<sub>3</sub></strong>.</p><p><strong>Important Properties of Line Graphs:</strong></p><p><strong>1. Vertex Count:</strong> The number of vertices in L(G) is equal to the number of edges in G. Formally, <strong>|V(L(G))| = |E(G)|</strong>. This is because each edge in the original graph becomes exactly one vertex in the line graph.</p><p><strong>2. Edge Count Relationship:</strong> The number of edges in L(G) depends on how many pairs of edges in G are incident (share a common vertex). If a vertex in G has degree d, then it contributes <strong>C(d, 2)</strong> edges to L(G), because each pair of edges at that vertex will form a connection in the line graph. The binomial coefficient <strong>C(d, 2) = d(d-1)/2</strong> represents the number of ways to choose two edges from the d edges incident to that vertex.</p><p><strong>3. Simplicity:</strong> The line graph of a simple graph is always simple, meaning it does not contain self-loops or multiple edges. This property ensures that the transformation preserves certain structural properties of the original graph.</p>",
        "nx": "expt5.py",
        "nn": "expt5NN.py"
    },
    6: {
        "title": "Minimum Spanning Tree",
        "aim": "To implement Kruskal’s algorithm to generate an MST, ensuring all vertices are connected with minimum possible total edge weight and without cycles.",        "date": "24/3/26",        "theory": "<p><strong>Introduction to Minimum Spanning Tree:</strong> A Minimum Spanning Tree (MST) of a connected, undirected, weighted graph is a tree that connects all the vertices of the graph with the minimum possible total edge weight and without forming any cycles. The MST is a fundamental concept in graph theory with applications in network design, transportation systems, and clustering algorithms. An important property of spanning trees is that a spanning tree of a graph with <strong>n</strong> vertices always contains exactly <strong>n − 1</strong> edges. This ensures that all vertices are connected while maintaining the acyclic property of a tree structure.</p><p><strong>Overview of Kruskal's Algorithm:</strong> Kruskal's Algorithm is a greedy algorithm used to find the MST of a graph. It works by selecting edges in increasing order of their weights and adding them to the spanning tree, ensuring that no cycle is formed. The algorithm is known for its simplicity and efficiency, making it one of the most popular methods for finding MSTs. It uses the concept of disjoint sets (also known as Union-Find) to detect cycles efficiently. Initially, each vertex is treated as a separate set, and edges are added only if they connect two different sets.</p><p><strong>Kruskal's Algorithm Steps:</strong></p><p><strong>Step 1 - Initialization:</strong> Choose an edge <strong>e<sub>1</sub></strong> from the edge set such that <strong>w(e<sub>1</sub>)</strong> is as small as possible. This edge will be the first edge added to the MST. The weight function <strong>w(e)</strong> denotes the weight of an edge <strong>e</strong>.</p><p><strong>Step 2 - Iterative Edge Selection:</strong> If edges <strong>e<sub>1</sub>, e<sub>2</sub>, ..., e<sub>i</sub></strong> have been chosen, then choose an edge <strong>e<sub>i+1</sub></strong> from <strong>E \\ {e<sub>1</sub>, e<sub>2</sub>, ..., e<sub>i</sub>}</strong> (the remaining edges) in such a way that: (i) <strong>G[{e<sub>1</sub>, e<sub>2</sub>, ..., e<sub>i+1</sub>}]</strong> is acyclic (remains a forest without cycles), and (ii) <strong>w(e<sub>i+1</sub>)</strong> is as small as possible subject to condition (i). This ensures we always add the minimum weight edge that does not create a cycle.</p><p><strong>Step 3 - Termination:</strong> Stop when Step 2 cannot be implemented further. This occurs when we have added <strong>n − 1</strong> edges, connecting all <strong>n</strong> vertices into a single tree.</p><p><strong>How Kruskal's Algorithm Works:</strong> Kruskal's algorithm always picks the edge with the least weight and gradually builds the MST by connecting different components. The algorithm operates on the principle of disjoint sets, where initially each vertex is treated as a separate component. As edges are processed in increasing order of weight, an edge is added to the MST only if it connects two different components (sets). This is efficiently managed using the Union-Find data structure, which supports fast operations to check if two vertices belong to the same set and to merge two sets when an edge is added. The acyclic property is automatically maintained because we only add edges that connect different components; adding an edge within the same component would create a cycle, which is avoided by design.</p>",
        "nx": "expt6.py",
        "nn": "expt6NN.py"
    },
    7: {
        "title": "Shortest Path",
        "aim": "To implement a shortest path algorithm in order to compute the shortest path between vertices in a weighted graph.",
        "date": "31/3/26",
        "theory": "<p><strong>Introduction to Shortest Paths:</strong> A shortest path in a connected, weighted graph is a path between two vertices such that the sum of the edge weights is minimum. Unlike spanning trees, the shortest path does not necessarily include all vertices of the graph. The primary goal in shortest path problems is to find the minimum distance from a source vertex to all other vertices in the graph. This concept is crucial in various applications such as GPS navigation, network routing, social network analysis, and resource optimization. Shortest path algorithms form the backbone of many real-world systems where efficient routing and minimal cost connections are essential.</p><p><strong>Dijkstra's Algorithm Overview:</strong> Dijkstra's Algorithm is a greedy algorithm used to find the shortest path from a source vertex to all other vertices in a graph with non-negative edge weights. It works by selecting the vertex with the smallest tentative distance and updating its adjacent vertices. The algorithm maintains a set of vertices for which the shortest path has been determined and iteratively expands this set by finding the nearest unvisited vertex. This greedy approach guarantees the optimal solution when edge weights are non-negative, making it one of the most widely used shortest path algorithms in computer science.</p><p><strong>Dijkstra's Algorithm Steps:</strong></p><p><strong>Step 1 - Initialization:</strong> Set <strong>l(u<sub>0</sub>) = 0</strong> and <strong>l(v) = ∞</strong> for all vertices <strong>v ≠ u<sub>0</sub></strong>. Here, <strong>l(v)</strong> represents the tentative distance from the source vertex <strong>u<sub>0</sub></strong> to vertex <strong>v</strong>. Initialize the set <strong>S<sub>0</sub> = {u<sub>0</sub>}</strong> (the set of vertices for which the shortest path is determined) and set <strong>i = 0</strong> as the iteration counter.</p><p><strong>Step 2 - Distance Update and Vertex Selection:</strong> For each vertex <strong>v ∉ S<sub>i</sub></strong> (vertices not yet in the determined set), replace <strong>l(v)</strong> by <strong>min{ l(v), l(u<sub>i</sub>) + w(u<sub>i</sub>, v) }</strong>. This step relaxes the distances by checking if the path through the current vertex <strong>u<sub>i</sub></strong> is shorter than the previously known distance. Then, compute the minimum value of <strong>l(v)</strong> among all vertices <strong>v ∉ S<sub>i</sub></strong> and let <strong>u<sub>i+1</sub></strong> be the vertex for which this minimum is attained. Add this vertex to the determined set: <strong>S<sub>i+1</sub> = S<sub>i</sub> ∪ {u<sub>i+1</sub>}</strong>.</p><p><strong>Step 3 - Termination Condition:</strong> Check the iteration counter: if <strong>i = n − 1</strong> (where n is the total number of vertices), the algorithm has determined the shortest path to all vertices and should stop. Otherwise, if <strong>i < n − 1</strong>, increment the iteration counter by replacing <strong>i</strong> with <strong>i + 1</strong> and return to Step 2 to continue the process.</p><p><strong>Key Properties and Insights:</strong> The algorithm maintains the invariant that all distances in the set <strong>S<sub>i</sub></strong> are optimal and will not change. By always selecting the unvisited vertex with the minimum distance, Dijkstra's algorithm ensures that once a vertex is added to <strong>S<sub>i</sub></strong>, its shortest path distance is finalized. The weight function <strong>w(u<sub>i</sub>, v)</strong> represents the direct edge weight from vertex <strong>u<sub>i</sub></strong> to vertex <strong>v</strong>. The algorithm's correctness depends on non-negative edge weights, as negative weights could invalidate the greedy selection strategy.</p>",
        "nx": "expt7.py",
        "nn": "expt7NN.py"
    },
    8: {
        "title": "Closed Walks and Trails",
        "aim": "To implement the generation of closed walks, trails and paths in a connected graph.",
        "date": "7/4/26",
        "theory": "<p><strong>Introduction to Walks:</strong> A walk in a graph G is defined as a finite alternating sequence of vertices and edges that allows both vertices and edges to be repeated. Walks are the most general type of traversal in a graph, providing a flexible way to move through the graph structure. The concept of walks is fundamental to understanding more restricted traversal types like trails and paths, and is essential in many graph theory applications including connectivity analysis and cycle detection.</p><p><strong>Formal Definition of Walks:</strong> A walk in G is an alternating sequence of vertices and edges of the form <strong>W = v<sub>0</sub>, e<sub>1</sub>, v<sub>1</sub>, e<sub>2</sub>, v<sub>2</sub>, …, e<sub>k</sub>, v<sub>k</sub></strong>, where each edge <strong>e<sub>i</sub> = (v<sub>i−1</sub>, v<sub>i</sub>) ∈ E</strong> for <strong>i = 1, 2, …, k</strong>. The integer <strong>k</strong> is called the length of the walk, which represents the number of edges in the sequence. In a walk, both vertices and edges may be repeated any number of times without restriction.</p><p><strong>Closed vs Open Walks:</strong> A walk is said to be <strong>closed</strong> if the initial vertex and the final vertex are the same, that is, <strong>v<sub>0</sub> = v<sub>k</sub></strong>. If <strong>v<sub>0</sub> ≠ v<sub>k</sub></strong>, then the walk is called an <strong>open walk</strong>. Closed walks are useful in studying graph cycles and connectivity properties, while open walks represent paths between different vertices.</p><p><strong>Definition of Trails:</strong> A trail is a walk in which all edges are distinct, that is, <strong>e<sub>i</sub> ≠ e<sub>j</sub></strong> for all <strong>i ≠ j</strong>. However, vertices may still repeat in a trail, making trails more restrictive than walks but more flexible than paths. The length of a trail is also defined as the number of edges in it. Trails are important in solving the famous Eulerian path problem, which involves finding a trail that uses every edge exactly once.</p><p><strong>Closed Trails and Circuits:</strong> A trail is said to be <strong>closed</strong> if <strong>v<sub>0</sub> = v<sub>k</sub></strong>, and such a closed trail is sometimes referred to as a <strong>circuit</strong>. If <strong>v<sub>0</sub> ≠ v<sub>k</sub></strong>, then the trail is called an <strong>open trail</strong>. Closed trails represent important structures in graph theory, particularly in network routing and Eulerian circuit problems.</p><p><strong>Definition of Paths:</strong> A path is a walk in which all vertices are distinct, that is, <strong>v<sub>i</sub> ≠ v<sub>j</sub></strong> for all <strong>i ≠ j</strong>. As a result, no edge can be repeated in a path. A path represents the simplest form of movement in a graph without revisiting any vertex. Paths are the most restrictive traversal type and are crucial in computing shortest distances and connectivity measures in graphs.</p><p><strong>Open Paths and Cycles:</strong> A path is said to be <strong>open</strong> if <strong>v<sub>0</sub> ≠ v<sub>k</sub></strong>, connecting two different vertices without repetition. A closed path is one in which <strong>v<sub>0</sub> = v<sub>k</sub></strong> and no other vertices are repeated (meaning only the starting and ending vertices are the same). Such a closed path is called a <strong>cycle</strong>. The number of edges in a path is called its length.</p><p><strong>Hierarchical Relationship:</strong> Every path is a trail and every trail is a walk, but the converse is not necessarily true. This hierarchical relationship can be summarized as: <strong>Path ⊂ Trail ⊂ Walk</strong>. Specifically, if a sequence is a path, it automatically satisfies the constraints of being a trail (no repeated edges) and a walk (alternating sequence of vertices and edges). However, a walk need not be a trail, and a trail need not be a path. Understanding these relationships is essential for solving various graph traversal problems and analyzing graph properties.</p>",
        "nx": "expt8.py",
        "nn": "expt8NN.py"
    },
    9: {
        "title": "Eulerian Circuit",
        "aim": "To implement an algorithm that checks existence of an Eulerian circuit and constructs a circuit that traverses every edge exactly once.",
        "date": "28/4/26",
        "theory": "<p><strong>Introduction to Eulerian Circuits:</strong> Let <strong>G = (V, E)</strong> be a finite, connected, undirected graph, where <strong>V</strong> is the set of vertices and <strong>E</strong> is the set of edges. An Eulerian circuit is a special type of closed trail that has the remarkable property of traversing every single edge in the graph exactly once while returning to the starting vertex. Eulerian circuits have important applications in route optimization, network design, and solving real-world problems such as the famous Königsberg bridge problem, which was the historical origin of graph theory itself.</p><p><strong>Formal Definition of Eulerian Circuit:</strong> An Eulerian circuit in G is defined as a closed trail represented by the sequence: <strong>v<sub>0</sub>, e<sub>1</sub>, v<sub>1</sub>, e<sub>2</sub>, v<sub>2</sub>, …, e<sub>m</sub>, v<sub>m</sub></strong> such that the following conditions are satisfied:</p><p><strong>1. Closed Loop Property:</strong> <strong>v<sub>0</sub> = v<sub>m</sub></strong>, which means the circuit starts and ends at the same vertex, forming a closed loop. This is essential for the circuit to be considered Eulerian.</p><p><strong>2. Edge Connectivity:</strong> For each <strong>i = 1, 2, …, m</strong>, the edge <strong>e<sub>i</strong> connects the vertices <strong>v<sub>i−1</sub></strong> and <strong>v<sub>i</sub></strong>, ensuring that consecutive vertices in the sequence are adjacent. This guarantees that the sequence forms a valid trail in the graph.</p><p><strong>3. No Edge Repetition:</strong> <strong>e<sub>i</sub> ≠ e<sub>j</sub></strong> for all <strong>i ≠ j</strong>, which ensures that no edge is repeated in the traversal. This is the defining characteristic that distinguishes Eulerian circuits from general closed trails.</p><p><strong>4. Complete Edge Coverage:</strong> <strong>{e<sub>1</sub>, e<sub>2</sub>, …, e<sub>m</sub>} = E</strong>, which means every edge of the graph is included exactly once in the circuit. If the number of edges in the graph is <strong>m</strong>, then the Eulerian circuit contains exactly <strong>m</strong> edges and <strong>m + 1</strong> vertices in the sequence <strong>v<sub>0</sub>, v<sub>1</sub>, v<sub>2</sub>, …, v<sub>m</sub></strong>.</p><p><strong>Euler's Theorem - The Even Degree Condition:</strong> A connected graph <strong>G</strong> has an Eulerian circuit if and only if <strong>deg(v) ≡ 0 (mod 2)</strong> for all <strong>v ∈ V</strong>, that is, every vertex of the graph has even degree. This fundamental result is known as Euler's Theorem and provides a simple criterion for determining whether an Eulerian circuit exists in a graph. The reason for this condition is that whenever a vertex is entered during traversal, it must also be exited, so edges are used in pairs at each vertex, resulting in an even degree requirement.</p><p><strong>Important Consequences:</strong> If any vertex has odd degree, then an Eulerian circuit does not exist in the graph. However, if exactly two vertices have odd degree, then the graph contains an Eulerian path (but not a circuit) that starts at one odd-degree vertex and ends at the other. This distinction is crucial for understanding the broader context of Eulerian traversals.</p><p><strong>Fleury's Algorithm for Finding Eulerian Circuits:</strong> Fleury's Algorithm is a constructive method that finds an Eulerian circuit in a connected graph with all vertices of even degree. The algorithm proceeds as follows:</p><p><strong>Step 1 - Initialization:</strong> Choose an arbitrary vertex <strong>v<sub>0</sub> ∈ V</strong> and set <strong>w<sub>0</sub> = v<sub>0</sub></strong>. Any vertex can be chosen as the starting point since the graph is connected and all vertices have even degree.</p><p><strong>Step 2 - Trail Construction Setup:</strong> Suppose that a trail <strong>w<sub>0</sub>, e<sub>1</sub>, w<sub>1</sub>, e<sub>2</sub>, w<sub>2</sub>, …, e<sub>i</sub>, w<sub>i</sub></strong> has been constructed, where <strong>w<sub>i</sub></strong> is the current vertex and we have used <strong>i</strong> edges so far.</p><p><strong>Step 3 - Edge Selection Strategy:</strong> From the set of edges incident on <strong>w<sub>i</sub></strong>, select an edge <strong>e<sub>i+1</sub></strong> such that: <strong>e<sub>i+1</sub></strong> is not a bridge in the remaining graph (removing it would disconnect the graph), or <strong>e<sub>i+1</sub></strong> is the only edge incident on <strong>w<sub>i</sub></strong>. This strategy ensures we don't prematurely cut off portions of the graph from future traversal.</p><p><strong>Step 4 - Vertex Transition:</strong> Let <strong>w<sub>i+1</sub></strong> be the vertex adjacent to <strong>w<sub>i</sub></strong> via the edge <strong>e<sub>i+1</sub></strong>. This moves the current position to the next vertex in the trail.</p><p><strong>Step 5 - Trail Extension:</strong> Extend the trail by adding <strong>e<sub>i+1</sub></strong> and <strong>w<sub>i+1</sub></strong> to the sequence, and immediately remove the edge <strong>e<sub>i+1</sub></strong> from the graph. This prevents using the same edge twice in future iterations.</p><p><strong>Step 6 - Repetition:</strong> Repeat Steps 2 to 5 until all edges of the graph are removed. As we continue the algorithm, the remaining graph shrinks, and we systematically traverse every edge exactly once.</p><p><strong>Step 7 - Eulerian Circuit Result:</strong> The resulting sequence <strong>w<sub>0</sub>, e<sub>1</sub>, w<sub>1</sub>, e<sub>2</sub>, w<sub>2</sub>, …, e<sub>m</sub>, w<sub>m</sub></strong> forms an Eulerian circuit, where <strong>w<sub>0</sub> = w<sub>m</sub></strong> (since all vertices have even degree, we return to the starting vertex) and every edge is traversed exactly once. The algorithm guarantees the existence of an Eulerian circuit when the even-degree condition is satisfied.</p>",
        "nx": "expt9.py",
        "nn": "expt9NN.py"
    },
    10: {
        "title": "Hamiltonian Circuit",
        "aim": "To implement a method that determines whether a graph contains a Hamiltonian circuit that visits every vertex exactly once and returns to the start.",
        "date": "5/5/26",
        "theory": "<p><strong>Introduction to Hamiltonian Circuits:</strong> Let <strong>G = (V, E)</strong> be a finite, connected, undirected graph, where <strong>V</strong> is the set of vertices and <strong>E</strong> is the set of edges. A Hamiltonian circuit is a special type of closed cycle that has the fundamental property of visiting every vertex in the graph exactly once before returning to the starting vertex. Hamiltonian circuits are among the most important concepts in graph theory due to their numerous real-world applications, from logistics and transportation planning to DNA sequencing and computer network design. The study of Hamiltonian circuits is central to understanding combinatorial optimization problems.</p><p><strong>Formal Definition of Hamiltonian Circuit:</strong> A Hamiltonian circuit in G is defined as a closed cycle represented by the sequence: <strong>v<sub>0</sub>, v<sub>1</sub>, v<sub>2</sub>, …, v<sub>n−1</sub>, v<sub>n</sub></strong> such that the following conditions are satisfied:</p><p><strong>1. Closed Loop Property:</strong> <strong>v<sub>0</sub> = v<sub>n</sub></strong>, which means the circuit starts and ends at the same vertex, forming a closed loop. This ensures that the traversal forms a complete cycle that returns to the origin.</p><p><strong>2. Edge Connectivity Between Consecutive Vertices:</strong> For each <strong>i = 1, 2, …, n</strong>, the vertices <strong>v<sub>i−1</sub></strong> and <strong>v<sub>i</sub></strong> are adjacent, meaning there exists an edge joining consecutive vertices in the sequence. This guarantees that the sequence represents a valid path through the graph where each step is supported by an edge.</p><p><strong>3. No Vertex Repetition:</strong> <strong>v<sub>i</sub> ≠ v<sub>j</sub></strong> for all <strong>0 ≤ i < j < n</strong>, which ensures that no vertex is repeated except the starting and ending vertex. This constraint is fundamental and distinguishes Hamiltonian circuits from general cycles or walks. Each vertex (except the start/end) appears exactly once in the traversal.</p><p><strong>4. Complete Vertex Coverage:</strong> <strong>{v<sub>0</sub>, v<sub>1</sub>, v<sub>2</sub>, …, v<sub>n−1</sub>} = V</strong>, which means every vertex of the graph is included exactly once in the circuit. If the graph contains <strong>n</strong> vertices, then the Hamiltonian circuit contains exactly <strong>n</strong> edges and <strong>n + 1</strong> vertices in the sequence: <strong>v<sub>0</sub>, v<sub>1</sub>, v<sub>2</sub>, …, v<sub>n</sub></strong>. The number of edges equals the number of vertices because each vertex must be visited exactly once and we return to the start.</p><p><strong>Definition of Hamiltonian Graphs:</strong> A graph G is said to be <strong>Hamiltonian</strong> if it contains a Hamiltonian circuit. The property of being Hamiltonian is an important structural characteristic that determines whether efficient traversals visiting all vertices are possible. Not all connected graphs are Hamiltonian; determining whether a graph is Hamiltonian is a computationally difficult problem known to be NP-complete.</p><p><strong>Main Objective and Contrast with Eulerian Circuits:</strong> The main objective of a Hamiltonian circuit is to traverse every vertex of the graph exactly once and finally return to the starting vertex. This is fundamentally different from Eulerian circuits, which focus on visiting every <strong>edge</strong> exactly once. While Eulerian circuits have an efficient characterization (the even-degree condition), determining whether a Hamiltonian circuit exists in a general graph is computationally intractable. In a Hamiltonian circuit, revisiting vertices is not allowed because the purpose is to complete a cycle that passes through all vertices without repetition. The only repeated vertex is the starting vertex, which appears again at the end to complete the circuit.</p><p><strong>Practical Applications:</strong> Hamiltonian circuits are widely used in practical applications such as routing problems, scheduling, computer networks, DNA sequencing, and optimization problems. One of the most famous applications is the <strong>Travelling Salesman Problem (TSP)</strong>, where a salesman must visit each city exactly once and return to the starting city while minimizing the total distance travelled. Other important applications include printed circuit board drilling optimization, vehicle routing in logistics, job scheduling in manufacturing, and protein folding in computational biology. The NP-completeness of the Hamiltonian circuit problem makes these applications computationally challenging, driving research into efficient approximation algorithms and heuristic methods.</p>",
        "nx": "expt10.py",
        "nn": "expt10NN.py"
    },
    11: {
        "title": "Graph Coloring",
        "aim": "To implement a graph coloring algorithm that assigns colors to vertices such that no two adjacent vertices share the same color, aiming for the minimum chromatic number.",
        "date": "12/5/26",
        "theory": "<p><strong>Introduction to Graph Coloring:</strong> Graph coloring is a fundamental method in graph theory used to assign colors to the vertices of a graph such that no two adjacent vertices have the same color. This technique has numerous practical applications in scheduling, register allocation in compilers, frequency assignment in wireless networks, map coloring, and solving various constraint satisfaction problems. The elegance of graph coloring lies in its simplicity of definition combined with its profound computational difficulty in finding optimal colorings.</p><p><strong>Formal Definition of Vertex Coloring:</strong> Let a graph be represented as <strong>G = (V, E)</strong>, where <strong>V</strong> is the set of vertices and <strong>E</strong> is the set of edges. A vertex coloring of a graph is a function: <strong>C : V → {1, 2, 3, ..., k}</strong> such that <strong>C(u) ≠ C(v)</strong> for all <strong>(u, v) ∈ E</strong>. This formal definition ensures that if two vertices are connected by an edge, they must be assigned different colors from the available set of <strong>k</strong> colors. The function C maps each vertex to one of the k available colors, and the coloring constraint guarantees that no edge connects two vertices of the same color.</p><p><strong>Chromatic Number:</strong> The minimum number of colors required to color a graph is called the <strong>Chromatic Number</strong> of the graph and is denoted by <strong>χ(G)</strong> (chi of G). Formally, <strong>χ(G) = min { k : G can be colored using k colors }</strong>. Finding the chromatic number of a general graph is an NP-hard problem, meaning there is no known polynomial-time algorithm to solve it optimally for all graphs. However, the chromatic number provides a measure of the graph's complexity and has implications for its structural properties. For example, the chromatic number of a complete graph <strong>K<sub>n</sub></strong> is <strong>n</strong>, while the chromatic number of a bipartite graph is at most 2.</p><p><strong>Overview of Greedy Graph Coloring Algorithm:</strong> The Greedy Coloring Algorithm is a practical heuristic method that assigns colors to vertices one by one following a specific order. While the greedy approach does not always produce an optimal coloring (i.e., using the minimum possible number of colors), it provides a quick and efficient approximation that works well in many practical cases. The algorithm's effectiveness depends heavily on the order in which vertices are selected, which is why smart vertex selection strategies are crucial.</p><p><strong>Vertex Selection Strategy:</strong> The algorithm employs a sophisticated vertex selection criterion to improve the quality of the coloring. In this method: (1) The vertex having the highest <strong>saturation degree</strong> is selected first. The saturation degree of a vertex is the number of different colors already used by its adjacent vertices. This criterion helps avoid situations where a vertex cannot be colored with many colors because its neighbors already use those colors. (2) If saturation degrees are equal between multiple vertices, the vertex with the highest ordinary degree (the total number of edges connected to it) is selected. The ordinary degree serves as a tiebreaker and generally helps prioritize vertices that have more constraints.</p><p><strong>Greedy Graph Coloring Algorithm Steps:</strong></p><p><strong>Step 1 - Initialization:</strong> Start with all vertices uncolored. Initialize an empty set to track which colors have been assigned to each vertex, and prepare a color assignment map for all vertices in the graph.</p><p><strong>Step 2 - Vertex Selection:</strong> Select a vertex following the saturation degree criterion: choose the vertex with the highest saturation degree (number of different colors used by its neighbors). If there is a tie, select the vertex with the highest ordinary degree (total number of adjacent vertices). This greedy selection ensures we prioritize vertices that are most constrained.</p><p><strong>Step 3 - Color Assignment:</strong> Assign the smallest possible color that is not used by any adjacent vertex to the selected vertex. Check all colors in the sequence 1, 2, 3, ... and assign the first color that doesn't appear among the vertex's neighbors. This ensures the coloring constraint is satisfied while minimizing color usage.</p><p><strong>Step 4 - Update Saturation Degrees:</strong> Update the saturation degree of all neighboring vertices of the newly colored vertex. Since we have introduced a new color to the neighborhood, each adjacent vertex's saturation degree may increase. This update is essential for the next iteration of vertex selection to make informed decisions.</p><p><strong>Step 5 - Repetition:</strong> Repeat Steps 2 to 4 until all vertices are colored. Continue the process systematically, always selecting the next vertex according to the saturation degree criterion and assigning colors accordingly. The algorithm terminates when every vertex in the graph has been assigned a color.</p><p><strong>Step 6 - Result Reporting:</strong> Count the total number of colors used. After all vertices have been colored, examine the color assignments to determine the total number of distinct colors employed in the coloring. This final count represents the number of colors needed by this particular greedy algorithm, though it may not be the chromatic number (optimal coloring) of the graph.</p><p><strong>Complexity and Optimality:</strong> The greedy coloring algorithm has a time complexity of <strong>O(V + E)</strong> in its implementation, making it very efficient even for large graphs. However, the solution quality depends on the vertex ordering strategy. The saturation degree-based selection typically provides better results than random or arbitrary orderings, often producing near-optimal colorings in practice. Despite its limitations, the greedy approach remains one of the most widely used coloring algorithms due to its simplicity, efficiency, and reasonable performance on real-world graphs.</p>",
        "nx": "expt11_1.py",
        "nn": None
    }
}

# ---------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------

def load_and_run_experiment(file_path):
    try:
        spec = importlib.util.spec_from_file_location("experiment", file_path)
        module = importlib.util.module_from_spec(spec)

        old_stdout = sys.stdout
        sys.stdout = StringIO()

        plt.close('all')

        spec.loader.exec_module(module)

        output = sys.stdout.getvalue()

        sys.stdout = old_stdout

        figs = []
        for num in plt.get_fignums():
            figs.append(plt.figure(num))

        return {
            "success": True,
            "output": output,
            "figures": figs
        }

    except Exception as e:
        sys.stdout = old_stdout

        return {
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }

def display_code(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        return f"Error loading file: {e}"

# ---------------------------------------------------
# COOL SIDEBAR MENU
# ---------------------------------------------------

st.sidebar.markdown("# Experiments")

experiment_options = [
    f"{i:02d} · {experiments[i]['title']}"
    for i in experiments
]

selected_label = st.sidebar.radio(
    "Select Experiment",
    experiment_options
)

selected_exp = int(selected_label.split(" ")[0].split("·")[0])

st.sidebar.markdown("---")

st.sidebar.markdown("""
### Dashboard Features
- NetworkX Algorithms
- Manual Algorithms
- Live Execution
- Graph Visualization
- Code Viewer
""")

total_experiments = len(experiments)

st.markdown(f"""
<div class="sticky-header">
    <div class="header-content">
        <div class="header-left">
            <div class="main-title">
                Graph Theory Laboratory Lab
            </div>
        </div>
        <div class="header-right">
            <p class="header-count">Experiment {selected_exp:02d} of {total_experiments}</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# MAIN SECTION
# ---------------------------------------------------

exp = experiments[selected_exp]

st.markdown(f"""
<div class="card">
<h2>Experiment {selected_exp}: {exp['title']}</h2>
<p><span class="field-label">DATE</span>{exp['date']}</p>
<p><span class="field-label">AIM</span>{exp['aim']}</p>
<p><span class="field-label">THEORY</span></p>
<div>{exp['theory']}</div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# EXPERIMENT 11
# ---------------------------------------------------

if selected_exp == 11:

    variant_files = [
        "expt11_1.py",
        "expt11_2.py",
        "expt11_3.py"
    ]

    for idx, variant in enumerate(variant_files, 1):

        variant_path = os.path.join(exp_dir, variant)

        st.markdown(f"""
        <div class="card-tight">
        <h3>Variant {idx}</h3>
        </div>
        """, unsafe_allow_html=True)

        tabs = st.tabs(["Code", "Output"])

        with tabs[0]:
            code = display_code(variant_path)
            st.code(code, language="python")

        with tabs[1]:

            if st.button("Execute", key=f"exec_variant_{idx}"):

                with st.spinner("Running experiment..."):

                    result = load_and_run_experiment(variant_path)

                if result["success"]:

                    if result["figures"]:
                        for fig in result["figures"]:
                            st.pyplot(fig)

                    if result["output"]:
                        st.markdown(
                            f'<div class="output-box">{result["output"].strip()}</div>',
                            unsafe_allow_html=True
                        )

                else:
                    st.error(result["error"])
                    st.code(result["traceback"])

# ---------------------------------------------------
# NORMAL EXPERIMENTS
# ---------------------------------------------------

else:

    col1, col2 = st.columns(2)

    # ---------------- NETWORKX ----------------

    with col1:

        st.markdown("""
        <div class="card-tight">
        <h3>NetworkX Implementation</h3>
        </div>
        """, unsafe_allow_html=True)

        nx_file = os.path.join(exp_dir, exp["nx"])

        tabs1 = st.tabs(["Code", "Output"])

        with tabs1[0]:

            code = display_code(nx_file)
            st.code(code, language="python")

        with tabs1[1]:

            if st.button("Execute", key=f"exec_nx_{selected_exp}"):

                with st.spinner("Running NetworkX implementation..."):

                    result = load_and_run_experiment(nx_file)

                if result["success"]:

                    if result["figures"]:
                        for fig in result["figures"]:
                            st.pyplot(fig)

                    if result["output"]:
                        st.markdown(
                            f'<div class="output-box">{result["output"].strip()}</div>',
                            unsafe_allow_html=True
                        )

                else:
                    st.error(result["error"])
                    st.code(result["traceback"])

    # ---------------- MANUAL ----------------

    with col2:

        if exp["nn"]:

            st.markdown("""
            <div class="card-tight">
            <h3>Manual Implementation</h3>
            </div>
            """, unsafe_allow_html=True)

            nn_file = os.path.join(exp_dir, exp["nn"])

            tabs2 = st.tabs(["Code", "Output"])

            with tabs2[0]:

                code = display_code(nn_file)
                st.code(code, language="python")

            with tabs2[1]:

                if st.button("Execute", key=f"exec_manual_{selected_exp}"):

                    with st.spinner("Running manual implementation..."):

                        result = load_and_run_experiment(nn_file)

                    if result["success"]:

                        if result["figures"]:
                            for fig in result["figures"]:
                                st.pyplot(fig)

                        if result["output"]:
                            st.markdown(
                                f'<div class="output-box">{result["output"].strip()}</div>',
                                unsafe_allow_html=True
                            )

                    else:
                        st.error(result["error"])
                        st.code(result["traceback"])

        else:

            st.markdown("""
            <div class="card">
            <h3>Manual Version Not Available</h3>
            <p>This experiment only includes the NetworkX implementation.</p>
            </div>
            """, unsafe_allow_html=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.markdown("""
<div style="
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: rgba(15, 12, 41, 0.95);
    color: #c4b5fd;
    text-align: center;
    padding: 8px;
    border-top: 1px solid rgba(139, 92, 246, 0.3);
    z-index: 9999;
    font-size: 13px;
    backdrop-filter: blur(10px);
    font-family: 'Inter', sans-serif;
    letter-spacing: 0.3px;
">
    <strong style="color:#a78bfa;">Chetana Chodankar</strong> &nbsp;|&nbsp; Roll No: 24B-CO-082 &nbsp;|&nbsp; Semester: 4
</div>
""", unsafe_allow_html=True)
