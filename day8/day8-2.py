from math import gcd


def parse(lines):
    directions = lines[0]

    elements = {}
    current_points = []
    for line in lines[2:]:
        key, value = line.replace(" ", "").replace("(", "").replace(")", "").split("=")
        elements[key] = tuple(value.split(","))

        if key.endswith("A"):
            current_points.append(key)

    nb_directions = len(directions)
    path_lengths = []
    for point in current_points:
        steps = 0
        while True:
            if directions[steps % nb_directions] == "L":
                point = elements[point][0]
            else:
                point = elements[point][1]
            steps += 1
            if point.endswith("Z"):
                path_lengths.append(steps)
                print(steps)
                break

    lcm = 1
    for i in path_lengths:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


with open("day8.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 8-2: {total}")
