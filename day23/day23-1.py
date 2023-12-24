import sys

slopes = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

sys.setrecursionlimit(10000)

def as_grid(lines):
    return [[col for col in row] for row in lines]


def visualize(grid, steps):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in steps:
                print("O", end="")
            else:
                print(grid[row][col], end="")
        print()

def get_neighbours(grid, loc):
    row, col = loc
    grid_height = len(grid)
    grid_width = len(grid[0])

    neighbours = []

    if grid[loc[0]][loc[1]] in slopes:
        slope = slopes[grid[loc[0]][loc[1]]]
        new_loc = (row + slope[0], col + slope[1])
        if 0 <= new_loc[0] < grid_height and 0 <= new_loc[1] < grid_width and grid[new_loc[0]][new_loc[1]] != "#":
            return [new_loc]
        return []

    for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        if 0 <= r < grid_height and 0 <= c < grid_width and grid[r][c] != "#":
            neighbours.append((r, c))

    return neighbours


def find_start(grid):
    return (0, grid[0].index("."))

longest_path = [[]]

junctions = []

def dfs(grid, start, visited, path):
    visited.add(start)
    path.append(start)

    if start[0] == len(grid) - 1 and len(path) > len(longest_path[0]):
        longest_path[0] = list(path)
    else:
        for neighbour in get_neighbours(grid, start):
            if neighbour not in visited:
                dfs(grid, neighbour, visited, path)

    path.pop()
    visited.remove(start)

def solve(lines):
    grid = as_grid(lines)
    visited = set()
    path = []
    dfs(grid, find_start(grid), visited, path)

    visualize(grid, longest_path[0])
    print(longest_path)
    return len(longest_path[0]) - 1


with open("day23.txt", 'r') as f:
    lines = f.read().splitlines()

    total = solve(lines)

    print(f"Day 23-1: {total}")