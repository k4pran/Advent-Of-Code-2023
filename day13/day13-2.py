import itertools


def find_mirrors_in_reverse(block):
    total = 0
    reflection_line = None
    for i in range(1, len(block)):
        top_rows = block[:i]
        bottom_rows = block[i:len(top_rows) + i]

        match_found = True
        for j in range(min(len(top_rows), len(bottom_rows))):
            if top_rows[-(j + 1)] != bottom_rows[j]:
                match_found = False

        if match_found:
            total += len(block) - i
            reflection_line = len(top_rows)

    return total, reflection_line


def find_mirrors(block):
    total = 0
    reflection_line = None
    for i in range(1, len(block)):
        top_rows = block[:i]
        bottom_rows = block[i:len(top_rows) + i]

        match_found = True
        for j in range(min(len(top_rows), len(bottom_rows))):
            if top_rows[-(j + 1)] != bottom_rows[j]:
                match_found = False

        if match_found:
            total += i
            reflection_line = len(top_rows)

    return total, reflection_line


def find_smudge(block, reverse=False):

    for i in range(1, len(block)):
        top_rows = block[:i]
        bottom_rows = block[i:len(top_rows) + i]

        diffs = []
        for j in range(min(len(top_rows), len(bottom_rows))):
            top_line = top_rows[-(j + 1)]
            bottom_line = bottom_rows[j]
            for k in range(len(top_line)):
                if top_line[k] != bottom_line[k]:
                    diffs.append((len(top_rows) - (j + 1), k))


        if len(diffs) == 1:
            block_copy = block.copy()
            smudge_row = diffs[0][0]
            smudge_col = diffs[0][1]
            to_change = block_copy[smudge_row]
            new_row = ""
            for l, col in enumerate(to_change):
                if l == smudge_col:
                    if col == "#":
                        new_row += "."
                    else:
                        new_row += "#"
                else:
                    new_row += col
            block_copy[smudge_row] = new_row

            if reverse:
                old_mirrors, old_line = find_mirrors_in_reverse(block)
                new_mirrors, new_line = find_mirrors_in_reverse(block_copy)
                if old_line != new_line:
                    return new_mirrors
            else:
                old_mirrors, old_line = find_mirrors(block)
                new_mirrors, new_line = find_mirrors(block_copy)
                if old_line != new_line:
                    return new_mirrors


def transpose(block):
    list(map(list, zip(*block)))
    return list(map(list, itertools.zip_longest(*block, fillvalue=None)))

def parse(puzzle_input):
    blocks = puzzle_input.split("\n\n")
    total = 0
    for block in blocks:
        split_block = block.split("\n")
        count = find_smudge(split_block)

        multiplier = 1
        if not count:
            count = find_smudge([i for i in reversed(split_block)], True)

        if not count:
            count = find_smudge(transpose(split_block))

        if not count:
            count = find_smudge([i for i in reversed(transpose(split_block))], True)

        total += count * 100

        # total += find_mirrors(fixed_block) * 100

        # transposed_block = transpose(split_block)
        # total += find_mirrors(transposed_block)

        # else:
        #     fixed_block = find_smudge(transpose(split_block))
        #     total += find_mirrors(fixed_block)
        #     total += find_mirrors(transpose(fixed_block)) * 100

    return total

with open("day13.txt", 'r') as f:
    puzzle_input = f.read()

    total = parse(puzzle_input)

    print(f"Day 13-2: {total}")
