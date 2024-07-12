from setup import nx, create_dag, visualize_graph, dag_edges_1
from topsort import topsort

# Create and visualize the DAG
G = create_dag(dag_edges_1)
visualize_graph(G)

def dagShortestPath(graph: nx.DiGraph, start: int):
    N = graph.number_of_nodes()
    Topsort = topsort(graph)
    
    # Initialize distances
    dist = {node: float('inf') for node in graph.nodes()}
    dist[start] = 0

    for nodeIndex in Topsort:
        if dist[nodeIndex] != float('inf'):
            for neighbor in graph.neighbors(nodeIndex):
                edgeWeight = graph[nodeIndex][neighbor]['weight']
                newDist = dist[nodeIndex] + edgeWeight
                if newDist < dist[neighbor]:
                    dist[neighbor] = newDist
                else:
                    dist[neighbor] = min(dist[neighbor], newDist)

    return dist

# Test the function with the start node 1
def main():
    print(dagShortestPath(G, 1))

if __name__ == '__main__':
    main()
