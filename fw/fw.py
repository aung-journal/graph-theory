from setup import nx, bf_edges_1
import time

g = nx.DiGraph()
for u, v, w in bf_edges_1:
    g.add_edge(u, v, weight=w)

n = g.number_of_nodes()
dp = [[] for _ in range(n)]
next = [[None] for _ in range(n)]

def setup(m: nx.Graph):
    #do a deep copy of the input matrix and setup
    #the 'next' matrix for path reconstruction
    for i in range(n):
        for j in range(n):
            dp[i][j] = m[i][j]
            if m[i][j] != float('inf'):
                next[i][j] = j

def propagateNegativeCycles(dp: list[list[int]], n: int):
    #Execute FW ASAP algorithm a second time but
    #this time if the dist can be improved
    #set the optimal dist to be -infinity.
    #every edge (i, j) is marked with -infinit is either
    #part of or reaches into a neg cycle.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = float('-inf')
                    next[i][j] = -1

def floydWarshall(m: nx.Graph):
    setup(m)

    #Execute FW all pairs shortest path algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    next[i][j] = next[i][k]

    #Detect and propagate negative cycles
    #This is an optional 
    propagateNegativeCycles(dp, n)

def reconstructPath(s, e):
    path = []
    #Check if there exists a path between the start
    #and end node
    if dp[s][e] == float('inf'): return path

    at = s
    # Reconstruct path from the next matrix
    while at != e:
        at = next[at][e]
        #the start node is trapped in negative cycle
        if at == -1: return None
        path.append(at)
    
    if next[at][e] == -1: return None
    path.append(e)
    return path

def main():

    start_time = time.time()
    floydWarshall(g)
    print("The time taken to create ASAP is --- {} seconds ---\n".format(time.time() - start_time))

    quit = False
    while not quit:
        start = int(input("Enter the start number you want to use dijkstra for (1 - {}) : ".format(g.number_of_nodes())))
        end = int(input("Enter the end number you want to use dijkstra for (1 - {}) : ".format(g.number_of_nodes())))

        start_time = time.time()
        print(f'The shortest path from {start} to {end} is ' + '[' + ', '.join([str(i) for i in reconstructPath(g, start, end)]) + ']')
        print("The time taken is --- {} seconds ---".format(time.time() - start_time))
        quit = input('Do you want to quit(Y/N): ').lower() == 'y'

if __name__ == '__main__':
    main()