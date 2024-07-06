from setup import create, visualize, complex_graph

G = create(complex_graph)
#visualize(complex_graph)
n = G.number_of_nodes()
visited = [False] * (n + 1)

def dfs(at):
    if visited[at]:
        return
    visited[at] = True

    # Use G.neighbors(at) to get neighbors in networkx
    neighbors = G.neighbors(at)
    for next_node in neighbors:
        dfs(next_node)

# Start DFS at node 0 (assuming node 0 exists in your graph)
start_node = 0
dfs(start_node)

# Print visited nodes
print("Visited nodes:", visited)
