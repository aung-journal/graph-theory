#This is python implementation of Bellman-Ford(BF) algorithm
from setup import nx, bf_edges_1

g = nx.DiGraph()
for u, v, w in bf_edges_1:
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
        print(f"The cost to get from node {start} from {node} is {dist[node]:.2f}.")

if __name__ == '__main__':
    #This code won't run if this file is imported
    main()
