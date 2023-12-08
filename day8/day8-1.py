def parse(lines):
    directions = lines[0]

    elements = {}
    steps = 0
    for line in lines[2:]:
        key, value = line.replace(" ", "").replace("(", "").replace(")", "").split("=")
        elements[key] = tuple(value.split(","))


    current_element = "AAA"
    nb_directions = len(directions)
    while True:
        if directions[steps % nb_directions] == "L":
            current_element = elements[current_element][0]
        else:
            current_element = elements[current_element][1]
        steps += 1
        if current_element == "ZZZ":
            return steps


with open("day8.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 8-1: {total}")
