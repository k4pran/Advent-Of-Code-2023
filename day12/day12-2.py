mem = dict()


def count_arrangements(springs, group_counts):
    key = (springs, group_counts)

    if key in mem:
        return mem[key]

    if springs == "":
        return 1 if group_counts == () else 0
    if group_counts == ():
        return 0 if "#" in springs else 1

    count = 0
    if springs[0] == "." or springs[0] == "?":
        count += count_arrangements(springs[1:], group_counts)

    if group_counts[0] > len(springs) or "." in springs[:group_counts[0]]:
        return count

    if springs[0] == "#" or springs[0] == "?":
        if group_counts[0] == len(springs) or springs[group_counts[0]] != "#":
            count += count_arrangements(springs[group_counts[0] + 1:], group_counts[1:])

    mem[key] = count
    return count


def parse(lines):
    total = 0
    for i, line in enumerate(lines):

        springs, groups = line.split()
        springs = "?".join([springs] * 5)

        groups = tuple([int(i) for i in groups.split(",")])
        groups *= 5

        total += count_arrangements(springs, groups)
    return total


with open("day12.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 12-2: {total}")
