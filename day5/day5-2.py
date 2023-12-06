def is_in_range(start, end, nb):
    return start <= nb <= end


def find_destination(map, nb):
    if is_in_range(map[1], map[1] + map[2], nb):
        return map[0] + abs(nb - map[1])
    return None


def find_seed(nb, map_blocks):
    for maps in reversed(map_blocks):

        for map in maps.split("\n")[1:]:
            dest_start, source_start, range_length = map.split()

            dest = find_destination((int(source_start), int(dest_start), int(range_length)), nb)
            if dest:
                nb = dest
                break

    return nb

def soil_has_seed(soil, seed_ranges):
    for i in range(1, len(seed_ranges), 2):
        if is_in_range(seed_ranges[i - 1], seed_ranges[i - 1] + seed_ranges[i], soil):
            return True
    return False


def parse(blocks):
    seeds_block = blocks[0]
    map_blocks = blocks[1:]

    seed_ranges = [int(seed) for seed in seeds_block.split(":")[-1].strip().split()]

    location_ranges = []
    for location in map_blocks[-1].split("\n")[1:]:
        dest_start, source_start, range_length = [int(nb) for nb in location.split()]
        location_ranges.append((source_start, dest_start, range_length))

    i = 0
    while True:
        soil = find_seed(i, map_blocks)
        if soil_has_seed(soil, seed_ranges):
            return i
        print(i)
        i += 1


with open("day5.txt", 'r') as f:
    lines = f.read()
    blocks = lines.split("\n\n")

    total = parse(blocks)

    print(f"Day 5-2: {total}")
