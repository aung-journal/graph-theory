#This is python implementation of Bellman-Ford(BF) algorithm
from setup import nx, bf_edges_1

edges_1 = [
    (0, 1, 2),
    (1, 2, -1),
    (2, 3, 3),
    (3, 4, 2),
    (4, 5, 1),
    (5, 6, 2),
    (6, 7, -3),
    (7, 8, 2),
    (8, 9, 1),
    (9, 10, 4),
    (10, 11, -2),
    (11, 12, 1),
    (12, 13, 3),
    (13, 14, 2),
    (14, 15, 1),
    (15, 16, -1),
    (16, 17, 2),
    (17, 18, 1),
    (18, 19, -2),
    (0, 2, 4),
    (2, 4, 2),
    (1, 3, 7),
    (3, 1, -2),
    (10, 0, -4),  # Ensures some connectivity in the graph
    (8, 15, 5)
]

g = nx.DiGraph()
for u, v, w in edges_1:
    g.add_edge(u, v, weight=w)

def bellmanFord(g: nx.DiGraph, s: int):
    V = g.number_of_nodes()
    dist = {node: float('inf') for node in g.nodes}
    dist[s] = 0

    # Apply relaxation for all edges V-1 times
    for _ in range(V - 1):
        for u, v, data in g.edges(data=True):
            weight = data['weight']
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Check for negative-weight cycles
    for u, v, data in g.edges(data=True):
        weight = data['weight']
        if dist[u] + weight < dist[v]:
            dist[v] = float('-inf')
            propagate_negative_infinity(g, v, dist)

    return dist

def propagate_negative_infinity(g: nx.DiGraph, start_node, dist):
    queue = [start_node]
    visited = set(queue)
    while queue:
        node = queue.pop(0)
        for neighbor in g.neighbors(node):
            if neighbor not in visited:
                dist[neighbor] = float('-inf')
                visited.add(neighbor)
                queue.append(neighbor)

def main():
    start = 0
    dist = bellmanFord(g, start)

    for node in g.nodes:
        print(f"The cost to get from node {start} to {node} is {dist[node]:.2f}.")

if __name__ == '__main__':
    #This code won't run if this file is imported
    main()
