from collections import deque

slopes = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}


def as_grid(lines):
    return [[col for col in row] for row in lines]


def visualize(grid, start, end, steps):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) == start:
                print("S", end="")
            elif (row, col) == end:
                print("E", end="")
            elif (row, col) in steps:
                print("O", end="")
            else:
                print(grid[row][col], end="")
        print()

def get_neighbours(grid, loc, previous_loc=None):
    row, col = loc
    grid_height = len(grid)
    grid_width = len(grid[0])

    neighbours = []

    for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        if 0 <= r < grid_height and 0 <= c < grid_width and grid[r][c] != "#":
            if previous_loc != (r, c) or previous_loc == None:
                neighbours.append((r, c))

    return neighbours


def find_start(grid):
    return (0, grid[0].index("."))


def find_junctions_and_deadends(grid):
    junctions = []
    dead_ends = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                continue
            neighbours = get_neighbours(grid, (row, col))
            if len(neighbours) == 0:
                dead_ends.append((row, col))
            elif len(neighbours) > 1:
                junctions.append((row, col))
    return junctions, dead_ends


longest_path = [[]]

def find_next_junction(grid, start, previous_pos=None):
    is_junction = False
    pos = start
    dist = 0
    while not is_junction:
        neighbours = get_neighbours(grid, pos, previous_loc=previous_pos)
        if len(neighbours) == 1:
            previous_pos = pos
            pos = neighbours[0]
            dist += 1
        else:
            return start, previous_pos, pos, dist


def find_longest(grid, start):

    q = deque()
    q.append((start, None, 0, set()))  # Each path has its own set of visited junctions
    longest_dist = 0
    mem = dict()
    states = set()
    while q:
        start, previous_pos, current_dist, junctions_visited = q.pop()
        if start in mem:
            previous_pos, junction, added_dist = mem[start]
        else:
            _, previous_pos, junction, added_dist = find_next_junction(grid, start, previous_pos=previous_pos)
            mem[start] = (previous_pos, junction, added_dist)

        if junction[0] == len(grid) - 1:
            updated_dist = current_dist + added_dist
            if updated_dist > longest_dist:
                longest_dist = updated_dist
                print(longest_dist)
            continue

        neighbours = get_neighbours(grid, junction, previous_loc=previous_pos)

        for neighbour in neighbours:
            if neighbour[0] == len(grid) - 1:
                updated_dist = current_dist + added_dist + 1
                if updated_dist > longest_dist:
                    longest_dist = updated_dist

            elif junction not in junctions_visited:
                state = neighbour, junction
                if state not in states:
                    updated_junctions_visited = junctions_visited.copy()
                    updated_junctions_visited.add(junction)
                    q.append((neighbour, junction, current_dist + added_dist + 1, updated_junctions_visited))
                else:
                    states.add(state)

    return longest_dist

def solve(lines):
    global longest_path
    grid = as_grid(lines)
    return find_longest(grid, find_start(grid))


with open("day23.txt", 'r') as f:
    lines = f.read().splitlines()

    total = solve(lines)

    print(f"Day 23-2: {total}")

    #6358 too low
    #6382 too low