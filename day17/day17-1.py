import heapq
import sys
from collections import deque


def as_grid(lines):
    return [[int(col) for col in row] for row in lines]

def get_cost_grid(lines):
    return [[sys.maxsize for _ in row] for row in lines]


def get_neighbours(grid, loc, paths):
    row, col = loc
    grid_height = len(grid)
    grid_width = len(grid[0])

    # neighbours = [(r, c) for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    #               if 0 <= r < grid_height and 0 <= c < grid_width]

    neighbours = []
    for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        if 0 <= r < grid_height and 0 <= c < grid_width:
            recent_path_line = [p for p in paths[loc][len(paths[loc]) - 3:]]
            if len(recent_path_line) < 3:
                neighbours.append((r, c))
                continue
            if (not all([r == recent_p[0] for recent_p in recent_path_line]) and
                    not all([c == recent_p[1] for recent_p in recent_path_line])):
                neighbours.append((r, c))

    return neighbours


def print_grid(grid):
    for row in grid:
        for col in row:
            if col == sys.maxsize:
                print("-", end="   ")
            else:
                print(col, end="   ")
        print()

def get_cost(costs, loc):
    row, col = loc
    return costs[row][col]


def update_cost(costs, loc, new_cost):
    row, col = loc
    costs[row][col] = new_cost


def find_path(grid, costs, start):
    visited = set()
    update_cost(costs, start, 0)

    unvisited = []
    heapq.heappush(unvisited, (start, 0))
    paths = {start: [start]}

    while unvisited:

        current, current_node_cost = heapq.heappop(unvisited)
        if current in visited:
            continue

        for neighbour in get_neighbours(grid, current, paths):
            if neighbour in visited:
                continue

            neighbour_cost = get_cost(grid, neighbour)
            new_cost = current_node_cost + neighbour_cost
            if new_cost < get_cost(costs, neighbour):
                update_cost(costs, neighbour, new_cost)
                paths[neighbour] = paths[current] + [neighbour]
                heapq.heappush(unvisited, (neighbour, new_cost))

        visited.add(current)
    return paths

def parse(lines):
    grid = as_grid(lines)
    costs = get_cost_grid(lines)

    find_path(grid, costs, (0, 0))
    print_grid(costs)


with open("day17.txt", 'r') as f:
    text = f.read().splitlines()

    total = parse(text)

    print(f"Day 17-1: {total}")
