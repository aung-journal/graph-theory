from collections import defaultdict

import networkx as nx
import matplotlib.pyplot as plt

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

def create(graph):
    # Create a graph object
    G = nx.Graph()

    # Add nodes and edges to the graph object
    for node in graph:
        G.add_node(node)
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    return G


def visualize(graph):
    # Create a directed graph object
    G = nx.Graph()

    # Add nodes and edges to the graph object
    for node in graph:
        G.add_node(node)
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    # Draw the graph
    pos = nx.spring_layout(G)  # Positions for all nodes
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray", linewidths=1, font_color="black")

    # Display the plot
    plt.title("Graph Visualization")
    plt.show()