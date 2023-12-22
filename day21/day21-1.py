from collections import deque


def as_grid(lines):
    return [[col for col in row] for row in lines]

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_neighbours(grid, pos):
    row, col = pos
    grid_height = len(grid)
    grid_width = len(grid[0])
    neighbours = []
    for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        if 0 <= r < grid_height and 0 <= c < grid_width:
            if grid[r][c] != "#":
                neighbours.append((r, c))
    return neighbours


def get_start(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                return r, c


def visualize(grid, final_plots):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in final_plots:
                print("O", end="")
            else:
                print(grid[row][col], end="")
        print()


def solve(lines, steps=100):
    grid = as_grid(lines)
    start = get_start(grid)

    q = deque()
    q.append((start, steps))
    plots = dict()
    final_plots = set()

    for i in range(steps + 1):
        plots[i] = set()
    while q:

        pos, depth = q.popleft()

        if depth >= 0:
            for n in get_neighbours(grid, pos):
                if n not in plots[depth]:
                    q.append((n, depth - 1))
                    plots[depth].add(n)
                if depth == 1:
                    final_plots.add(n)

    visualize(grid, final_plots)
    return len(final_plots)



with open("day21.txt", 'r') as f:
    lines = f.read().splitlines()

    total = solve(lines)

    print(f"Day 20-1: {total}")
