
def as_grid(lines):
    return [[col for col in row] for row in lines]


def fall(grid, rock_pos):
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


def parse(lines):
    grid = as_grid(lines)
    load = 0
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col == "O":
                new_height = fall(grid, (x, y))
                load += len(grid) - new_height

    for row in grid:
        print(row)
    return load

with open("day14.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 14-1: {total}")
