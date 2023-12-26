def find_mirrors(block):
    for i in range(1, len(block)):
        top_rows = block[:i][::-1]
        bottom_rows = block[i:]

        total_mismatches = 0
        for x, y in zip(top_rows, bottom_rows):
            for a, b in zip(x, y):
                total_mismatches += 0 if a == b else 1
        if total_mismatches == 1:
            return i

    return 0


def parse(blocks):
    total = 0
    for block in blocks.split("\n\n"):
        split_block = block.split("\n")
        row = find_mirrors(split_block)
        total += row * 100

        col = find_mirrors(list(zip(*split_block)))
        total += col
    return total


with open("day13.txt", 'r') as f:
    puzzle_input = f.read()

    total = parse(puzzle_input)

    print(f"Day 13-2: {total}")
    # 240900 - too high
    # 192300 - too high
