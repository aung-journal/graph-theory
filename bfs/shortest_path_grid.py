from queue import Queue

#grid information
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
target = (4, 4)

R, C = len(grid[0]) ,len(grid)
m = grid
sr, sc = 0, 0
rq, cq = Queue(), Queue()

# Variables used to track the number of steps taken
move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

reached_end = False

visited = [[False for _ in range(C)] for _ in range(R)]
dr = [-1 , 1, 0, 0]
dc = [0, 0, 1, -1]

def explore_neighbours(r, c):
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        #Skip invalid cells. Assume R and C for the number
        #of rows and columns
        if rr < 0 or cc < 0: continue
        if rr >= R or cc >= C: continue

        #Skip visited locations or blocked cells
        if visited[rr][cc]: continue
        if m[rr][cc] == 1: continue

        rq.put(rr)
        cq.put(cc)
        visited[rr][cc] = True
        nodes_in_next_layer+=1

def solve():
    rq.put(sr)
    cq.put(sc)
    visited[sr][sc] = True
    while rq.qsize() > 0 or cq.qsize() > 0:
        r = rq.get()
        c = cq.get()
        if r == target[0] and c == target[1]:
            reached_end = True
            break
        explore_neighbours(r, c)
        # number of steps to get to the dungeon
        nodes_left_in_layer-=1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count+=1
    if reached_end:
        return move_count
    return -1