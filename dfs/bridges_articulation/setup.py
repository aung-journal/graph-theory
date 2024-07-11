from collections import defaultdict

import networkx as nx
import matplotlib.pyplot as plt

from typing import Union

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
    (0, 1, -1),
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
    # Draw the graph
    pos = nx.spring_layout(G)  # Positions for all nodes
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray", linewidths=1, font_color="black")

    # Display the plot
    plt.title("Graph Visualization")
    plt.show()

def visualize(graph: dict[int:list]):
    G = create(graph)
    visualize_graph(G)