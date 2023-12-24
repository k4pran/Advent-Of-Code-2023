def get_hailstones(lines):
    hailstones = []
    for line in lines:
        p, v = line.replace(" ", "").split("@")
        p = [int(pos) for pos in p.split(",")]
        v = [int(vel) for vel in v.split(",")]
        hailstones.append((p, v))
    return hailstones

def is_in_bounds(pos, lower_bound, upper_bound):
    x, y = pos
    return lower_bound <= x <= upper_bound and lower_bound <= y <= upper_bound


def find_intersections(hailstones, lower_bound=200000000000000, upper_bound=400000000000000):
    total = 0
    for i in range(len(hailstones)):
        for j in range(i + 1, len(hailstones)):
            intersection = get_intersection(hailstones[i], hailstones[j])
            if intersection and is_in_bounds(intersection, lower_bound, upper_bound):
                print(intersection)
                total += 1
    return total

def solve(lines):
    hailstones = get_hailstones(lines)
    return find_intersections(hailstones)


with open("day24.txt", 'r') as f:
    lines = f.read().splitlines()

    total = solve(lines)

    print(f"Day 24-2: {total}")