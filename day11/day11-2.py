import itertools


def expand_space(galaxies, empty_space, dimension, expansion_size):
    galaxies = sorted(galaxies, key=lambda x: x[dimension])
    for i, empty_col in enumerate(empty_space):
        for j, galaxy in enumerate(galaxies):
            if galaxy[dimension] > empty_col:
                for galaxy_to_update in galaxies[j:]:
                    galaxy_to_update[dimension] += expansion_size
                for k, empty_galaxy_col in enumerate(empty_space[i + 1:]):
                    empty_space[k + i + 1] += expansion_size
                break


def expand_universe(lines, expansion=1000000 - 1):
    empty_galaxy_rows = set(i for i in range(len(lines)))
    empty_galaxy_cols = set(i for i in range(len(lines[0])))

    galaxies = []
    for i, row in enumerate(lines):
        new_row = []
        for j, col in enumerate(row):
            new_row.append(col)
            if col == "#":
                empty_galaxy_rows.discard(i)
                empty_galaxy_cols.discard(j)
                galaxies.append([i, j])

    empty_galaxy_cols = sorted([i for i in empty_galaxy_cols])
    empty_galaxy_rows = sorted([i for i in empty_galaxy_rows])

    expand_space(galaxies, empty_galaxy_cols, 1, expansion)
    expand_space(galaxies, empty_galaxy_rows, 0, expansion)

    return galaxies


def manhattan_dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def find_path_total(lines):
    galaxies = expand_universe(lines)

    total_dist = 0
    for pairing in itertools.combinations(galaxies, 2):
        dist = manhattan_dist(pairing[0], pairing[1])
        total_dist += dist
    return total_dist


with open("day11.txt", 'r') as f:
    lines = f.read().splitlines()

    total = find_path_total(lines)

    print(f"Day 11-2: {total}")