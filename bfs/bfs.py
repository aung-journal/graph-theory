from setup import create, visualize, complex_graph
from queue import Queue

G = create(complex_graph)
#visualize(complex_graph)
n = G.number_of_nodes()

def solve(s):
    q = Queue(n + 1) # size of n + 1 (0 - n)
    q.put(s) #enqueue

    visited = [False] * (n + 1)
    visited[s] = True

    prev = [None] * (n + 1) # tracks who the parent of node i
    while not q.empty():
        node = q.get() #dequeue
        neighbors = G.neighbors(node)

        for next in neighbors:
            if not visited[next]:
                q.put(next)
                visited[next] = True
                prev[next] = node
    return prev

def reconstructPath(s, e, prev):

    # Reconstruct path going backwards from e
    path = []
    at = e
    while at is not None:
        path.append(at)
        at = prev[at]

    path.reverse()

    #If s and e are connected return the path
    if path[0] == s:
        return path
    return [] #the case for disjointed nodes

# s = start node, e = end node, and 0 <= e, s < n
def bfs(s, e):

    # Do a BFS starting at node s
    prev = solve(s)

    # Return reconstructed path from s -> e
    return reconstructPath(s, e, prev)

print(bfs(0, 18))