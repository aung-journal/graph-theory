from setup import complex_graph, tree, create

# Create the graph
g = create(complex_graph)
n = g.number_of_nodes()

ids = [0] * n
low = [0] * n
visited = [False] * n
id = 0

# Perform DFS to find bridges
# at = current node, parent = previous node.
# The bridges list is always of even length and indexes (2*i, 2*i+1)
# form a bridge. For example, nodes at
# indexes (0, 1) are a bridge, (2, 3) is another etc...
def dfs(at: int, parent: int, bridges: list[int]):
    global id  # Declare id as global to modify the outer variable
    visited[at] = True
    id += 1
    low[at] = ids[at] = id

    # For each edge from node 'at' to node 'to'
    for to in g.neighbors(at):
        if to == parent:
            continue
        if not visited[to]:
            dfs(to, at, bridges)
            low[at] = min(low[at], low[to])
            if ids[at] < low[to]:
                bridges.append(at)
                bridges.append(to)
        else:
            low[at] = min(low[at], ids[to])

def findBridges():
    bridges = []
    for i in range(n):
        if not visited[i]:
            dfs(i, -1, bridges)
    return list(set(bridges))

print(findBridges())
