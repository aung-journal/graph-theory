from setup import undirected_edges, undirected_edges_3, nx, plt
from queue import PriorityQueue, Queue
from indexed_priority_queue import IndexedPriorityQueue
#from d_heap import MinHeap
from Daryheap import DaryHeap
import time

def visualize_undirected_weight_graph(G: nx.Graph):
    # Draw the graph
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray', width=2, style='dotted')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.show()

g = nx.Graph()
g.add_edges_from(undirected_edges_3)

#visualize_undirected_weight_graph(g)

#s means start node (0 <= s < n), n means number of nodes in g
def dijkstra(g: nx.Graph, s):
    n = g.number_of_nodes()
    vis = [False] * (n + 1)
    prev = [None] * (n + 1)
    dist = [float('inf') for _ in range(n + 1)]
    dist[s] = 0
    pq = Queue() #Queue and Priority Queue are interchangeable here
    pq.put((s, 0))
    while pq.qsize() != 0:
        index, minVal = pq.get()
        vis[index] = True
        if dist[index] < minVal: continue
        for neighbour in g.neighbors(index):
            if vis[neighbour]:  continue
            edgeWeight = g[index][neighbour]['weight']
            newDist = dist[index] + edgeWeight
            if newDist < dist[neighbour]:
                prev[neighbour] = index
                dist[neighbour] = newDist
                pq.put((neighbour, newDist))
    return (dist, prev)

def eager_dijkstra(g: nx.Graph, s):
    n = g.number_of_nodes()
    vis = [False] * (n + 1)
    prev = [None] * (n + 1)
    dist = [float('inf') for _ in range(n + 1)]
    dist[s] = 0
    ipq = IndexedPriorityQueue()
    ipq.push(s, 0)
    while ipq.__len__() != 0:
        index, minVal = ipq.pop()
        vis[index] = True
        if dist[index] < minVal: continue
        for neighbour in g.neighbors(index):
            if vis[neighbour]:  continue
            edgeWeight = g[index][neighbour]['weight']
            newDist = dist[index] + edgeWeight
            if newDist < dist[neighbour]:
                prev[neighbour] = index
                dist[neighbour] = newDist
                if not ipq.__contains__(neighbour):
                    ipq.push(neighbour, newDist)
                else:
                    ipq.update(neighbour, newDist)
    return (dist, prev)

def d_heap_dijkstra(g: nx.Graph, s, e):
    n = g.number_of_nodes()
    edgeCount = g.number_of_edges()
    degree = edgeCount / n
    ipq = DaryHeap(degree)
    ipq.push(s, 0)
    vis = [False] * (n + 1)
    prev = [None] * (n + 1)
    dist = [float('inf') for _ in range(n + 1)]
    dist[s] = 0
    
    while ipq.__len__() != 0:
        index, minVal = ipq.pop()
        vis[index] = True
        if dist[index] < minVal: continue
        for neighbour in g.neighbors(index):
            if vis[neighbour]:  continue
            edgeWeight = g[index][neighbour]['weight']
            newDist = dist[index] + edgeWeight
            if newDist < dist[neighbour]:
                prev[neighbour] = index
                dist[neighbour] = newDist
                if not ipq.__contains__(neighbour):
                    ipq.push(neighbour, newDist)
                else:
                    ipq.decrease_key(neighbour, newDist)
        if index == e: return (dist[e], prev)
    return (float('inf'), [])

def reconstructPath(g: nx.Graph, s, e):
    n = g.number_of_nodes()
    if e < 0 or e > n: raise Exception('Invalid node index')
    if s < 0 or s > n: raise Exception('Invalid node index')
    path = []
    dist, prev = d_heap_dijkstra(g, s, e)
    if dist == float('inf'): return path

    at = e
    while at is not None:
        path.append(at)
        at = prev[at]

    path.reverse()
    return path

#e is the index of end node (0 <= e < n)
def findShortestPath(g, s, e):
    dist, prev = eager_dijkstra(g, s)
    path = []
    #reachable
    if dist[e] == float('inf'):
        return path
    
    at = e
    while at is not None:
        path.append(at)
        at = prev[at]

    path.reverse()
    return path

def main():
    quit = False

    while not quit:
        start = int(input("Enter the start number you want to use dijkstra for (1 - {}) : ".format(g.number_of_nodes())))
        end = int(input("Enter the end number you want to use dijkstra for (1 - {}) : ".format(g.number_of_nodes())))

        start_time = time.time()
        print(f'The shortest path from {start} to {end} is ' + '[' + ', '.join([str(i) for i in reconstructPath(g, start, end)]) + ']')
        print("The time taken is --- {} seconds ---".format(time.time() - start_time))
        quit = input('Do you want to quit(Y/N): ').lower() == 'y'

if __name__ == '__main__':
    #This code won't run if this file is imported
    main()
