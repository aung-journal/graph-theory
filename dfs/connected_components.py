from setup import create, visualize, complex_graph

G = create(complex_graph)
visualize(complex_graph)
n = G.number_of_nodes()
components = [False] * (n + 1)
visited = [False] * (n + 1)

def dfs(at):
    visited[at] = True
    components[at] = True
    
    neighbors = G.neighbors(at)
    for next in neighbors:
        if not visited[next]:
            dfs(next)

def findComponents():
    count = 0
    for i in range(n):
        if not visited[i]:
            count+=1
            dfs(i)
    return (count, components)

print(findComponents())