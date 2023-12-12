def parse(lines):
    total = 0


with open("day12.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 12-2: {total}")