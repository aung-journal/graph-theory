#This is python implementation of Bellman-Ford(BF) algorithm
from setup import nx, bf_edges_2

g = nx.DiGraph()
g.add_edges_from(bf_edges_2)

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

    return dist

def main():
    start = 0
    dist = bellmanFord(g, start)

    for i in range(g.number_of_nodes()):
        print(f"The cost to get from node {start} from {i} is {dist[i]:.2f}.")

if __name__ == '__main__':
    #This code won't run if this file is imported
    main()
