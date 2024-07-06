import random

def dfs_maze(width, height):
    maze = [[0 for _ in range(width)] for _ in range(height)]
    stack = [(0, 0)]
    visited = set((0, 0))

    def neighbors(x, y):
        directions = [(x-2, y), (x+2, y), (x, y-2), (x, y+2)]
        random.shuffle(directions)
        return directions

    while stack:
        x, y = stack[-1]
        maze[x][y] = 1
        next_steps = [n for n in neighbors(x, y) if 0 <= n[0] < height and 0 <= n[1] < width and n not in visited]

        if next_steps:
            next_x, next_y = next_steps.pop()
            visited.add((next_x, next_y))
            maze[(x + next_x) // 2][(y + next_y) // 2] = 1
            stack.append((next_x, next_y))
        else:
            stack.pop()

    return maze

# Example usage
width, height = 10, 10  # dimensions must be odd
maze = dfs_maze(width, height)
for row in maze:
    print("".join(['#' if cell == 0 else '.' for cell in row]))
