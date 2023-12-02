max_values = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def parse_cube_set(cube_set):
    color_values = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for color_part in cube_set.split(","):
        _, count, color = color_part.split(" ")
        color_values[color] = int(count)
    return color_values

# def parse_line(line):
#     game_part, cubes_part = line.split(':')
#     game_id = game_part.split(' ')[-1]
#     cube_sets = cubes_part.split(";")
#
#     totals = {
#         'red': 0,
#         'blue': 0,
#         'green': 0
#     }
#     for cube_set in cube_sets:
#         color_counts = parse_cube_set(cube_set)
#         for color, count in color_counts.items():
#             totals[color] += count
#
#     if totals["red"] > max_values["red"] or totals["blue"] > max_values["blue"] or totals["green"] > max_values["green"]:
#         return 0
#     return int(game_id)

def parse_line(line):
    game_part, cubes_part = line.split(':')
    game_id = game_part.split(' ')[-1]
    cube_sets = cubes_part.split(";")

    totals = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    for cube_set in cube_sets:
        color_counts = parse_cube_set(cube_set)
        for color, count in color_counts.items():
            totals[color] = max(totals[color], count)

    return totals["red"] * totals["blue"] * totals["green"]

with open("day2.txt", 'r') as f:
    lines = f.read().splitlines()

    total = 0
    for line in lines:
        total += parse_line(line)

    print(f"Day 2-1: {total}")