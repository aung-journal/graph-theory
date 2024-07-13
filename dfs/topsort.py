from setup import nx, create, visualize, complex_graph, tree, complex_rooted_tree
from typing import Union
import time

start_time = time.time()

G = create(complex_graph)
T = create(tree)
RT = create(complex_rooted_tree)
#visualize(complex_rooted_tree)

def dfs(at: int, V: list, visitedNodes: set, graph: Union[nx.Graph, nx.DiGraph]):
    V[at] = True

    for neighbor in graph.neighbors(at):  # Traverse only the neighbors of the current node
        if not V[neighbor]:
            dfs(neighbor, V, visitedNodes, graph)
    
    visitedNodes.add(at)

def optimized_dfs(i: int, at: int, V: list, ordering: list, graph: Union[nx.Graph, nx.DiGraph]):
    V[at] = True

    for neighbor in graph.neighbors(at):  # Traverse only the neighbors of the current node
        if not V[neighbor]:
            i = optimized_dfs(i, neighbor, V, ordering, graph)
    
    ordering[i] = at
    return i - 1

# Input is networkx object
# This is an unoptimized version
def topsort(graph: Union[nx.Graph, nx.DiGraph]):
    N = graph.number_of_nodes()
    V = [False] * N  # No need for N + 1; indices are 0 to N-1
    ordering = [0] * N  # No need for N + 1; indices are 0 to N-1
    i = N - 1

    for at in range(N):
        if not V[at]:
            visitedNodes = set()  # Which I passed into dfs to add nodes
            dfs(at, V, visitedNodes, graph)
            for nodeId in visitedNodes:
                ordering[i] = nodeId
                i -= 1
    return ordering

#This is optimized version
def optimized_topsort(graph: Union[nx.Graph, nx.DiGraph]):
    N = graph.number_of_nodes()
    V = [False] * N  # No need for N + 1; indices are 0 to N-1
    ordering = [0] * N  # No need for N + 1; indices are 0 to N-1
    i = N - 1

    for at in range(N):
        if not V[at]:
            i = optimized_dfs(i, at, V, ordering, graph)
            
    return ordering

def main():
    print(topsort(RT))
    print(optimized_topsort(RT))

    end_time = time.time()
    print("--- {} seconds ---".format(end_time - start_time))

if __name__ == '__main__':
    main()
