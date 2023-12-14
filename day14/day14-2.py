import hashlib


def as_grid(lines):
    return [[col for col in row] for row in lines]


def north_load(grid):
    load = 0
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col == "O":
                load += len(grid) - x
    return load


def fall_north(grid, rock_pos):
    height = rock_pos[0]
    col = rock_pos[1]
    while height != 0:
        next_tile = grid[height - 1][col]
        if next_tile != ".":
            grid[height][col] = "O"
            return height
        grid[height][col] = "."
        height -= 1
    grid[height][col] = "O"
    return height


def fall_east(grid, rock_pos):
    row = rock_pos[0]
    width = rock_pos[1]
    while width != len(grid[0]) - 1:
        next_tile = grid[row][width + 1]
        if next_tile != ".":
            grid[row][width] = "O"
            return row
        grid[row][width] = "."
        width += 1
    grid[row][width] = "O"
    return row


def fall_south(grid, rock_pos):
    height = rock_pos[0]
    col = rock_pos[1]
    while height != len(grid) - 1:
        next_tile = grid[height + 1][col]
        if next_tile != ".":
            grid[height][col] = "O"
            return height
        grid[height][col] = "."
        height += 1
    grid[height][col] = "O"
    return height


def fall_west(grid, rock_pos):
    row = rock_pos[0]
    width = rock_pos[1]
    while width != 0:
        next_tile = grid[row][width - 1]
        if next_tile != ".":
            grid[row][width] = "O"
            return row
        grid[row][width] = "."
        width -= 1
    grid[row][width] = "O"
    return row


def grid_to_state(grid):
    hasher = hashlib.sha256()
    for row in grid:
        for col in row:
            hasher.update(str(col).encode())
    return hasher.hexdigest()


def perform_cycle(grid):
    # fall north
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col == "O":
                fall_north(grid, (x, y))

    # fall west
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col == "O":
                fall_west(grid, (x, y))

    # fall south
    for x in range(len(grid) - 1, -1, -1):
        for y, col in enumerate(grid[x]):
            if col == "O":
                fall_south(grid, (x, y))

    # # fall east
    for x, row in enumerate(grid):
        for y in range(len(grid[0]) - 1, -1, -1):
            if row[y] == "O":
                fall_east(grid, (x, y))


def parse(lines):
    grid = as_grid(lines)

    cache = set()
    cycles = 1000000000
    hash_first_seen = {}
    for i in range(cycles):
        perform_cycle(grid)
        current_hash = grid_to_state(grid)

        if current_hash in cache:
            cycle_start = hash_first_seen[current_hash]
            cycle_length = i - cycle_start

            remaining = (cycles - i - 1) % cycle_length

            for cycle in range(remaining):
                perform_cycle(grid)

            load = north_load(grid)
            print(f"Cycle found at {cycle_start} with cycle size {cycle_length} and load -- {load}")
            return load

        cache.add(current_hash)
        hash_first_seen[current_hash] = i

    for row in grid:
        print(row)


with open("day14.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 14-2: {total}")