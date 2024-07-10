from setup import nx
import time

edges = [
    (0, 1, 2),
    (1, 2, -1),
    (2, 3, 3),
    (3, 4, 2),
    (4, 5, 1),
    (0, 2, 4),
    (2, 4, 2),
    (1, 3, 7),
    (3, 1, -2)  # This edge introduces a negative weight
]

edges_1 = [
    (0, 1, 2),
    (1, 2, -1),
    (2, 3, 3),
    (3, 4, 2),
    (4, 5, 1),
    (5, 6, 2),
    (6, 7, -3),
    (7, 8, 2),
    (8, 9, 1),
    (9, 10, 4),
    (10, 11, -2),
    (11, 12, 1),
    (12, 13, 3),
    (13, 14, 2),
    (14, 15, 1),
    (15, 16, -1),
    (16, 17, 2),
    (17, 18, 1),
    (18, 19, -2),
    (0, 2, 4),
    (2, 4, 2),
    (1, 3, 7),
    (3, 1, -2),
    (10, 0, -4),  # Ensures some connectivity in the graph
    (8, 15, 5)
]

g = nx.DiGraph()
for u, v, w in edges_1:
    g.add_edge(u, v, weight=w)

n = g.number_of_nodes()
dp = [[float('inf')] * n for _ in range(n)]
next_matrix = [[None] * n for _ in range(n)]

def setup(graph: nx.Graph):
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = 0
            elif graph.has_edge(i, j):
                dp[i][j] = graph[i][j]['weight']
                next_matrix[i][j] = j
            else:
                dp[i][j] = float('inf')
                next_matrix[i][j] = None

def propagateNegativeCycles():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = float('-inf')
                    next_matrix[i][j] = -1

def floydWarshall(graph: nx.Graph):
    setup(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    next_matrix[i][j] = next_matrix[i][k]

    propagateNegativeCycles()
    return dp

def reconstructPath(s, e):
    path = []
    if dp[s][e] == float('inf'):
        return path

    at = s
    while at != e:
        if at == -1:
            return None
        path.append(at)
        at = next_matrix[at][e]

    if next_matrix[at][e] == -1:
        return None
    path.append(e)
    return path

def main():
    start_time = time.time()
    floydWarshall(g)
    print("The time taken to create ASAP is --- {} seconds ---\n".format(time.time() - start_time))

    quit = False
    while not quit:
        start = int(input("Enter the start number you want to use Floyd-Warshall for (0 - {}) : ".format(n-1)))
        end = int(input("Enter the end number you want to use Floyd-Warshall for (0 - {}) : ".format(n-1)))

        start_time = time.time()
        path = reconstructPath(start, end)
        if path:
            print(f'The shortest path from {start} to {end} is ' + '[' + ', '.join([str(i) for i in path]) + ']')
        else:
            print(f'No path exists from {start} to {end}')
        print("The time taken is --- {} seconds ---".format(time.time() - start_time))
        quit = input('Do you want to quit (Y/N): ').lower() == 'y'

if __name__ == '__main__':
    main()
