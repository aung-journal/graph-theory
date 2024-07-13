from setup import create, visualize, complex_graph
from queue import Queue
import time

G = create(complex_graph)
visualize(complex_graph)
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

def main():
    quit = False

    while not quit:
        start = int(input("Enter the start number you want to use BFS for (1 - {}) : ".format(G.number_of_nodes())))
        end = int(input("Enter the end number you want to use BFS for (1 - {}) : ".format(G.number_of_nodes())))

        start_time = time.time()
        print(f'The prev array for {start} is ' + '[' + ', '.join([str(i) for i in solve(start)]) + ']')
        print(f'The shortest path from {start} to {end} is ' + '[' + ', '.join([str(i) for i in bfs(start, end)]) + ']')
        print("The time taken is --- {} seconds ---".format(time.time() - start_time))
        quit = input('Do you want to quit(Y/N): ').lower() == 'y'

if __name__ == '__main__':
    #This code won't run if this file is imported
    main()