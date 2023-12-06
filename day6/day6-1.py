def nb_winnables_count(time, record):
    winnables = 0
    for i in range(time):
        distance = i * (time - i)
        if distance > record:
            winnables += 1
    return winnables

def parse(lines):
    time = int(lines[0].split(":")[-1].strip().replace(" ", ""))
    record = int(lines[1].split(":")[-1].strip().replace(" ", ""))

    return nb_winnables_count(time, record)

with open("day6.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 6-1: {total}")
