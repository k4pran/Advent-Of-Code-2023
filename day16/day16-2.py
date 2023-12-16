from collections import OrderedDict


def remove_item(boxes, box_hash, label):
    if not box_hash in boxes:
        return
    box = boxes[box_hash]
    if not label in box:
        return
    del box[label]
def as_grid(lines):
    return [[col for col in row] for row in lines]


def is_in_grid(grid, pos):
    if pos[0] < 0 or pos[0] >= len(grid):
        return False
    return 0 <= pos[1] <= len(grid[0]) - 1


def reflect_right_mirror(direction):
    # /
    row, col = direction
    if col != 0:
        return -col, row
    if row != 0:
        return col, -row


def reflex_left_mirror(direction):
    # \
    row, col = direction
    return col, row


def follow_beam(grid, beam, energized=None):
    if energized is None:
        energized = set()
    if is_in_grid(grid, beam[0]):
        energized.add(beam)
    while True:
        new_pos = (beam[0][0] + beam[1][0], beam[0][1] + beam[1][1])
        if not is_in_grid(grid, new_pos):
            return energized

        grid_element = grid[new_pos[0]][new_pos[1]]
        if grid_element == '\\':
            beam = (new_pos, tuple(reflex_left_mirror(beam[1])))

        elif grid_element == '/':
            beam = (new_pos, tuple(reflect_right_mirror(beam[1])))

        # new beams
        elif beam[1][0] != 0 and grid_element == '-':
            follow_beam(grid, (new_pos, tuple(reflex_left_mirror(beam[1]))), energized)
            follow_beam(grid, (new_pos, tuple(reflect_right_mirror(beam[1]))), energized)

        elif beam[1][1] != 0 and grid_element == '|':
            follow_beam(grid, (new_pos, tuple(reflex_left_mirror(beam[1]))), energized)
            follow_beam(grid, (new_pos, tuple(reflect_right_mirror(beam[1]))), energized)
        else:
            beam = (new_pos, beam[1])
        if beam in energized:
            return energized

        energized.add(beam)


def draw_energized(lines, energized):
    grid = [["." for col in row] for row in lines]
    for e in set([i[0] for i in energized]):
        grid[e[0]][e[1]] = "#"

    for row in grid:
        for col in row:
            print(col, end="")
        print()


def get_starting_beams(grid):
    beams = []
    # Left column
    for row in range(len(grid)):
        beams.append(((row, -1), (0, 1)))

    # Right column
    for row in range(len(grid), -1, -1):
        beams.append(((row, len(grid[0])), (0, -1)))

    # Top row
    for col in range(len(grid[0])):
        beams.append(((-1, col), (1, 0)))

    for col in range(len(grid[0]), -1, -1):
        beams.append(((len(grid), col), (-1, 0)))

    return beams

def parse(lines):
    grid = as_grid(lines)

    beams = get_starting_beams(grid)
    # beams = [((-1, 3), (1, 0))]
    largest_energized = {}
    largest_energized_count = 0
    for beam in beams:
        energized = follow_beam(grid, beam)
        energized_tile_count = len(set([i[0] for i in energized]))
        if energized_tile_count > largest_energized_count:
            largest_energized_count = energized_tile_count
            largest_energized = energized
    draw_energized(lines, largest_energized)
    return len(set([i[0] for i in largest_energized]))



with open("day16.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 16-1: {total}")

    # 8406 too high
    # 8354 too low
