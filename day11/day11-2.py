import itertools


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

    galaxies = sorted(galaxies, key=lambda x: x[1])
    for i, empty_col in enumerate(empty_galaxy_cols):
        for j, galaxy in enumerate(galaxies):
            if galaxy[1] > empty_col:
                for galaxy_to_update in galaxies[j:]:
                    galaxy_to_update[1] += expansion
                for k, empty_galaxy_col in enumerate(empty_galaxy_cols[i + 1:]):
                    empty_galaxy_cols[k + i + 1] += expansion
                break

    galaxies = sorted(galaxies, key=lambda x: x[0])
    for i, empty_rows in enumerate(empty_galaxy_rows):
        for j, galaxy in enumerate(galaxies):
            if galaxy[0] > empty_rows:
                for galaxy_to_update in galaxies[j:]:
                    galaxy_to_update[0] += expansion
                for k, empty_galaxy_row in enumerate(empty_galaxy_rows[i + 1:]):
                    empty_galaxy_rows[k + i + 1] += expansion
                break

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