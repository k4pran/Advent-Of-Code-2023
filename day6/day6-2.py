def nb_winnables_count(time, record):
    winnables = 0
    for i in range(time):
        distance = i * (time - i)
        if distance > record:
            winnables += 1
    return winnables

def parse(lines):
    times = [int(i) for i in lines[0].split(":")[-1].strip().split()]
    records = [int(i) for i in lines[1].split(":")[-1].strip().split()]

    total = 1
    for time, record in zip(times, records):
        total *= nb_winnables_count(time, record)
    return total

with open("day6.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 6-2: {total}")
