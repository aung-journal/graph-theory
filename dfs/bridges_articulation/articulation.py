from setup import complex_graph, create

# Create the graph
g = create(complex_graph)
n = g.number_of_nodes()

ids = [0] * n
low = [0] * n
visited = [False] * n
isArt = [False] * n
id = 0

# Perform DFS to find articulation points
# at = current node, parent = previous node.
def dfs(root: int, at: int, parent: int):
    global id  # Declare id as global to modify the outer variable
    global outEdgeCount
    if parent == root:
        outEdgeCount += 1
    visited[at] = True
    id += 1
    low[at] = ids[at] = id

    # For each edge from node 'at' to node 'to'
    for to in g.neighbors(at):
        if to == parent:
            continue
        if not visited[to]:
            dfs(root, to, at)
            low[at] = min(low[at], low[to])
            # Check if it's an articulation point
            if parent != root and ids[at] <= low[to]:
                isArt[at] = True
        else:
            low[at] = min(low[at], ids[to])

def findArtPoints():
    global outEdgeCount
    for i in range(n):
        if not visited[i]:
            outEdgeCount = 0
            dfs(i, i, -1)
            isArt[i] = outEdgeCount > 1
    #return the nodes number
    return [i for i, val in enumerate(isArt) if val]

print(findArtPoints())
