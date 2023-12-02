def init_color_dict(red=0, green=0, blue=0):
    return {
        "red": red,
        "green": green,
        "blue": blue
    }


max_values = init_color_dict(12, 13, 14)


def parse_cube_set(cube_set):
    color_values = init_color_dict()
    for color_part in cube_set.split(","):
        _, count, color = color_part.split(" ")
        color_values[color] = int(count)
    return color_values


def parse_line(line):
    game_part, cubes_part = line.split(':')
    game_id = game_part.split(' ')[-1]
    cube_sets = cubes_part.split(";")

    for cube_set in cube_sets:
        color_counts = parse_cube_set(cube_set)
        for color, count in color_counts.items():
            if count > max_values[color]:
                return 0
    return int(game_id)


with open("day2.txt", 'r') as f:
    lines = f.read().splitlines()

    total = 0
    for line in lines:
        total += parse_line(line)

    print(f"Day 2-1: {total}")
