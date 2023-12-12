import itertools


def get_groups(springs):
    groups = []

    next_group = ""
    for i, spring in enumerate(springs):
        if spring == ".":
            groups.append(next_group)
            next_group = ""
        else:
            next_group += spring

    if next_group != "":
        groups.append(next_group)
    return groups

def count_arrangements(springs, group_counts):
    spring_1 = springs.replace("?", "#")
    spring_2 = springs.replace("?", ".")

    match_count = 0
    for combination in set([i for i in itertools.product(*zip(spring_1, spring_2))]):
        groups = get_groups(combination)
        if tuple(len(group) for group in groups if len(group)) == group_counts:
            match_count += 1
    return match_count

def parse(lines):
    total = 0
    for i, line in enumerate(lines):
        print("Line " + str(i))
        springs, groups = line.split()
        total += count_arrangements(springs, tuple([int(i) for i in groups.split(",")]))
    return total


with open("day12.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 12-1: {total}")
