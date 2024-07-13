#https://www.youtube.com/watch?v=09_LlHjoEiY&ab_channel=freeCodeCamp.org

from collections import defaultdict

import networkx as nx
import matplotlib.pyplot as plt

from typing import Union

import random

# Example graph adjacency list
graph = defaultdict(list)

# Add edges
edges = [(1, 2), (1, 3), (2, 4), (3, 5)]

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # Assuming it's an undirected graph

# graph = {
#     1: [2, 3],
#     2: [1, 4],
#     3: [1, 5],
#     4: [2],
#     5: [3]
# }

complex_graph = {
    0: [1],
    1: [2, 3, 6],
    2: [1, 4, 5],
    3: [1, 7, 8],
    4: [2, 9, 10],
    5: [2, 11, 12],
    6: [1, 13, 14],
    7: [3, 15, 16],
    8: [3, 17, 18],
    9: [4],
    10: [4],
    11: [5],
    12: [5],
    13: [6],
    14: [6],
    15: [7],
    16: [7],
    17: [8],
    18: [8]
}

tree = {
    0: [1, 2],
    1: [3, 4, 5],
    2: [6, 7],
    3: [8],
    4: [],
    5: [9, 10],
    6: [11],
    7: [],
    8: [],
    9: [12],
    10: [13, 14],
    11: [],
    12: [],
    13: [],
    14: []
}

complex_rooted_tree = {
    0: [1, 2, 3],
    1: [4, 5],
    2: [6],
    3: [7, 8],
    4: [9, 10],
    5: [],
    6: [11, 12],
    7: [13],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [14, 15],
    13: [16],
    14: [],
    15: [],
    16: []
}

dag_edges = [
    (0, 1, 5),
    (0, 2, 3),
    (1, 3, 6),
    (1, 2, 2),
    (2, 4, 4),
    (2, 5, 2),
    (2, 3, 7),
    (3, 5, 1),
    (3, 4, -1),
    (4, 5, -2),
    (4, 6, 2),
    (5, 6, 1)
]

dag_edges_1 = [
    (1, 2, 7),
    (1, 3, 9),
    (1, 6, 14),
    (2, 3, 10),
    (2, 4, 15),
    (3, 4, 11),
    (3, 6, 2),
    (4, 5, 6),
    (6, 5, 9)
]

dag_edges_2 = [
    (0, 1, 5),
    (0, 2, 3),
    (1, 3, 6),
    (1, 2, 2),
    (2, 4, 4),
    (2, 5, 2),
    (3, 4, 1),
    (3, 5, 2),
    (4, 5, 3)
]

undirected_edges = [
    (1, 2, {'weight': 3}),
    (1, 3, {'weight': 4}),
    (2, 3, {'weight': 1}),
    (2, 4, {'weight': 2}),
    (3, 4, {'weight': 5}),
    (3, 5, {'weight': 6}),
    (4, 5, {'weight': 7})
]

# Generate 30 nodes
num_nodes = 30

# Generate random edges with weights
undirected_edges_1 = []
for i in range(1, num_nodes):
    for j in range(i + 1, num_nodes + 1):
        weight = random.randint(1, 20)  # Random weight between 1 and 20
        edges.append((i, j, {'weight': weight}))

undirected_edges_2 = [
    (1, 2, {'weight': 7}),
    (1, 3, {'weight': 12}),
    (1, 5, {'weight': 9}),
    (2, 3, {'weight': 8}),
    (2, 4, {'weight': 5}),
    (2, 6, {'weight': 10}),
    (3, 4, {'weight': 6}),
    (3, 5, {'weight': 4}),
    (4, 6, {'weight': 11}),
    (5, 6, {'weight': 3}),
    (7, 8, {'weight': 7}),
    (7, 9, {'weight': 5}),
    (7, 10, {'weight': 8}),
    (8, 9, {'weight': 3}),
    (8, 11, {'weight': 6}),
    (9, 10, {'weight': 4}),
    (9, 11, {'weight': 9}),
    (10, 12, {'weight': 7}),
    (11, 12, {'weight': 5}),
    (13, 14, {'weight': 6}),
    (13, 15, {'weight': 10}),
    (13, 16, {'weight': 4}),
    (14, 15, {'weight': 8}),
    (14, 17, {'weight': 9}),
    (15, 16, {'weight': 3}),
    (15, 18, {'weight': 5}),
    (16, 17, {'weight': 11}),
    (16, 18, {'weight': 7}),
    (17, 19, {'weight': 6}),
    (17, 20, {'weight': 10}),
    (18, 19, {'weight': 8}),
    (18, 21, {'weight': 9}),
    (19, 20, {'weight': 3}),
    (19, 21, {'weight': 5}),
    (20, 22, {'weight': 11}),
    (21, 22, {'weight': 7}),
    (23, 24, {'weight': 6}),
    (23, 25, {'weight': 9}),
    (23, 26, {'weight': 8}),
    (24, 25, {'weight': 4}),
    (24, 27, {'weight': 10}),
    (25, 26, {'weight': 5}),
    (25, 28, {'weight': 7}),
    (26, 27, {'weight': 3}),
    (26, 28, {'weight': 11}),
    (27, 29, {'weight': 9}),
    (27, 30, {'weight': 6}),
    (28, 29, {'weight': 8}),
    (28, 30, {'weight': 10}),
    (29, 30, {'weight': 4})
]

undirected_edges_3 = [
    (1, 2, {'weight': 5}),
    (1, 3, {'weight': 8}),
    (1, 4, {'weight': 3}),
    (2, 3, {'weight': 2}),
    (2, 4, {'weight': 7}),
    (3, 4, {'weight': 6}),
    (4, 5, {'weight': 4}),
    (5, 6, {'weight': 9}),
    (5, 7, {'weight': 5}),
    (6, 7, {'weight': 3})
]

# Direction vectors
def grid_neighbors(r, c, R, C):
    dr = [-1 , 1, 0, 0]
    dc = [0, 0, 1, -1]
    neighbors = []

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        #Skip invalid cells. Assume R and C for the number
        #of rows and columns
        if rr < 0 or cc < 0: continue
        if rr >= R or cc >= C: continue
        neighbors.append((rr, cc))
    return neighbors

def create(graph: dict[int:list]):
    # Create a graph object
    G = nx.Graph()

    # Add nodes and edges to the graph object
    for node in graph:
        G.add_node(node)
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    return G

def create_dag(edges):
    G = nx.DiGraph()
    # Add nodes
    nodes = set()
    for u, v, w in edges:
        nodes.add(u)
        nodes.add(v)
    G.add_nodes_from(nodes)

    # Add weighted edges
    G.add_weighted_edges_from(edges)

    return G

def visualize_graph(G: Union[nx.Graph, nx.DiGraph]):
    if isinstance(G, nx.Graph):
        # Draw the graph
        pos = nx.spring_layout(G)  # Positions for all nodes
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray", linewidths=1, font_color="black")

        # Display the plot
        plt.title("Graph Visualization")
        plt.show()
    else:
        # Draw the graph
        pos = nx.spring_layout(G)  # positions for all nodes

        plt.figure(figsize=(12, 8))
        edges = G.edges(data=True)
        edge_labels = {(u, v): d['weight'] for u, v, d in edges}

        nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, font_weight="bold", edge_color="gray")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
        plt.title("Complex Rooted Weighted Tree Visualization", fontsize=20)
        plt.show()

def visualize(graph: dict[int:list]):
    G = create(graph)
    visualize_graph(G)