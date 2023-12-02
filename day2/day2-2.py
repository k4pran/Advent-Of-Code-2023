import functools


def init_color_dict(red=0, green=0, blue=0):
    return {
        "red": red,
        "green": green,
        "blue": blue
    }


def parse_cube_set(cube_set):
    color_values = init_color_dict()
    for color_part in cube_set.split(","):
        _, count, color = color_part.split(" ")
        color_values[color] = int(count)
    return color_values


def parse_line(line):
    game_part, cubes_part = line.split(':')
    cube_sets = cubes_part.split(";")

    max_values = init_color_dict()
    for cube_set in cube_sets:
        color_counts = parse_cube_set(cube_set)
        for color, count in color_counts.items():
            max_values[color] = max(max_values[color], count)

    return functools.reduce(lambda x, y: x * y, max_values.values(), 1)


with open("day2.txt", 'r') as f:
    lines = f.read().splitlines()

    total = 0
    for line in lines:
        total += parse_line(line)

    print(f"Day 2-2: {total}")