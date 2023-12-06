def is_in_range(start, end, nb):
    return start <= nb <= end


def find_destination(mappings, nb):
    for mapping in mappings:
        if is_in_range(mapping[0], mapping[0] + mapping[2], nb):
            return mapping[1] + abs(nb - mapping[0])
    return nb

def parse(blocks):
    seeds_block = blocks[0]
    map_blocks = blocks[1:]

    seeds = [int(seed) for seed in seeds_block.split(":")[-1].strip().split()]

    # mapped_values = seeds
    mapped_values = [82]
    for maps in map_blocks:
        mappings = []
        for map in maps.split("\n")[1:]:
            dest_start, source_start, range_length = map.split()
            mappings.append((int(source_start), int(dest_start), int(range_length)))

        next_mapped = []
        for v in mapped_values:
            next_mapped.append(find_destination(mappings, v))

        mapped_values = next_mapped
    return min(mapped_values)


with open("day5.txt", 'r') as f:
    lines = f.read()
    blocks = lines.split("\n\n")

    total = parse(blocks)

    print(f"Day 5-1: {total}")
