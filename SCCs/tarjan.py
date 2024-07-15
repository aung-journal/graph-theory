from setup import nx, SCC_edges
from collections import deque

UNVISITED = -1
g = nx.DiGraph()
g.add_edges_from(SCC_edges)
n = g.number_of_nodes()

id = 0  # used to give each node an id
sccCount = 0

ids = [UNVISITED] * n
low = [0] * n
onStack = [False] * n
stack = deque()

def dfs(at):
    global id, sccCount
    stack.append(at)  # same as push operation
    onStack[at] = True
    ids[at] = low[at] = id
    id += 1

    # Visit all neighbours & min low-link on callback
    for neighbor in g.neighbors(at):
        if ids[neighbor] == UNVISITED:
            dfs(neighbor)
            low[at] = min(low[at], low[neighbor])
        elif onStack[neighbor]:
            low[at] = min(low[at], ids[neighbor])

    # After having visited all the neighbours of 'at'
    # if we're at the start of a SCC empty the seen
    # stack until we're back to the start of the SCC.
    if ids[at] == low[at]:
        while True:
            node = stack.pop()
            onStack[node] = False
            low[node] = ids[at]
            if node == at:
                break
        sccCount += 1

def findSccs():
    for i in range(n):
        ids[i] = UNVISITED
    for i in range(n):
        if ids[i] == UNVISITED:
            dfs(i)
    return low

print(findSccs())
