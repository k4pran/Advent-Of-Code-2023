import itertools

import numpy as np

def expand_universe(lines):
    mat = []

    empty_galaxy_rows = set(i for i in range(len(lines)))
    empty_galaxy_cols = set(i for i in range(len(lines[0])))
    for i, row in enumerate(lines):
        new_row = []
        for j, col in enumerate(row):
            new_row.append(col)
            if col == "#":
                empty_galaxy_rows.discard(i)
                empty_galaxy_cols.discard(j)
        mat.append(new_row)

    inc = 0
    for row in empty_galaxy_rows:
        mat.insert(row + inc, list(mat[row + inc]))
        inc += 1


    inc = 0
    for col in empty_galaxy_cols:
        for row in mat:
            row.insert(col + inc, row[col + inc])
        inc += 1

    # yuk
    galaxies = []
    for i, row in enumerate(mat):
        for j, col in enumerate(row):
            if col == "#":
                galaxies.append((i, j))

    return mat, galaxies

def manhattan_dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def find_path_total(lines):
    mat, galaxies, = expand_universe(lines)

    total_dist = 0
    for pairing in itertools.combinations(galaxies, 2):
        dist = manhattan_dist(pairing[0], pairing[1])
        total_dist += dist
        print(str(pairing) + " -- " + str(dist))
    return total_dist


with open("day11.txt", 'r') as f:
    lines = f.read().splitlines()

    total = find_path_total(lines)

    print(f"Day 11-1: {total}")
