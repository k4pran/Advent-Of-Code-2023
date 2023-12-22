from collections import deque


def visualize_infinite_grid(grid_pattern, nodes):
    # Determine the dimensions based on the nodes
    r_values, c_values = zip(*nodes)
    min_r, max_r = min(r_values), max(r_values)
    min_c, max_c = min(c_values), max(c_values)

    grid_height, grid_width = (max_r - min_r + 1), (max_c - min_c + 1)
    grid_pattern_height = len(grid_pattern)
    grid_pattern_width = len(grid_pattern[0])

    # Convert nodes list to a set for faster lookup
    nodes_set = set(nodes)

    # Create an empty grid
    grid = []
    for r in range(grid_height):
        row = []
        for c in range(grid_width):
            if c != 0 and c % grid_pattern_width == 0:
                row.append(" ")
            if (r + min_r, c + min_c) in nodes_set:
                row.append('O')
            else:
                col = grid_pattern[r % grid_pattern_height][c % grid_pattern_width]
                row.append(col)
        if r % grid_pattern_width == 0:
            grid.append([" " for _ in range(grid_pattern_width)])
        grid.append(row)

    # Convert grid to string and print
    grid_string = '\n'.join(' '.join(row) for row in grid)
    print(f"Grid visualization:\n{grid_string}")


def as_grid(lines):
    return [[col for col in row] for row in lines]

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_neighbours(grid, pos):
    row, col = pos
    grid_height = len(grid)
    grid_width = len(grid[0])
    neighbours = []
    for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        if grid[r % grid_height][c % grid_width] != "#":
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


def cache_state(cache, depth, grid, nodes, steps):
    if len(nodes) == 0:
        return
    grid_height = len(grid)
    grid_width = len(grid[0])
    state = set()
    for node in nodes:
        normalized_node = (node[0] % grid_height, node[1] % grid_width)
        state.add(normalized_node)

    state = sorted(state)
    # print(state)
    state = hash(tuple(state))
    if state in cache:
        print(f"Matching state found at depth {steps - depth}: nb_nodes {len(nodes)}. Matches depth {cache[state]}")
        visualize_infinite_grid(grid, nodes)
        cache = dict()
        # exit(0)
    else:
        cache[state] = steps - depth


def solve(lines, steps=1000):
    grid = as_grid(lines)
    start = get_start(grid)

    q = deque()
    q.append((start, steps))
    final_plots = set()

    plots = dict()
    depth_counts = dict()
    for i in range(steps + 1):
        plots[i] = set()
        depth_counts[i] = 0

    cache = dict()
    current_depth = steps
    while q:

        pos, depth = q.popleft()

        if depth != current_depth and depth != steps and depth >= 0:
            cache_state(cache, current_depth, grid, plots[current_depth], steps)
            current_depth = depth

        if depth >= 0:
            for n in get_neighbours(grid, pos):
                if n not in plots[depth]:
                    q.append((n, depth - 1))
                    plots[depth].add(n)
                    depth_counts[depth] += 1
                if depth == 1:
                    final_plots.add(n)

        if depth >= 0:
            depth_counts[depth] -= 1
            # if depth_counts[depth] <= 1 and depth >= 0:
            # print(f"plots at depth{depth} -- {len(plots[depth])}")


    # for depth, ps in plots.items():
    #     print(f"plots at depth{depth} -- {len(plots[depth])}")
    visualize(grid, final_plots)
    return len(final_plots)



with open("day21.txt", 'r') as f:
    lines = f.read().splitlines()

    total = solve(lines)

    print(f"Day 20-1: {total}")
