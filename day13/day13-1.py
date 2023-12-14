import itertools


def find_mirrors(block):
    total = 0
    for i in range(1, len(block)):
        top_rows = block[:i]
        bottom_rows = block[i:len(top_rows) + i]

        match_found = True
        for j in range(min(len(top_rows), len(bottom_rows))):
            if top_rows[-(j + 1)] != bottom_rows[j]:
                match_found = False

        if match_found:
            total += i

    return total




def transpose(block):
    # short circuits at shortest nested list if table is jagged:
    list(map(list, zip(*block)))

    # discards no data if jagged and fills short nested lists with None
    return list(map(list, itertools.zip_longest(*block, fillvalue=None)))

def parse(puzzle_input):
    blocks = puzzle_input.split("\n\n")
    total = 0
    for block in blocks:
        split_block = block.split("\n")
        total += (find_mirrors(split_block) * 100)
        transposed_block = transpose(split_block)
        total += find_mirrors(transposed_block)
    return total

with open("day13.txt", 'r') as f:
    puzzle_input = f.read()

    total = parse(puzzle_input)

    print(f"Day 13-1: {total}")
