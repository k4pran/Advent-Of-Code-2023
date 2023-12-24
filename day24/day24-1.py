def get_hailstones(lines):
    hailstones = []
    for line in lines:
        p, v = line.replace(" ", "").split("@")
        p = [int(pos) for pos in p.split(",")]
        v = [int(vel) for vel in v.split(",")]
        hailstones.append((p, v))
    return hailstones


def get_slope_intercept(p, v):
    px, py = p[:2]
    vx, vy = v[:2]

    slope = vy / vx
    intercept = py - slope * px
    return slope, intercept


def get_intersection(h1, h2):
    p1, v1 = h1
    p2, v2 = h2

    m1, b1 = get_slope_intercept(p1, v1)
    m2, b2 = get_slope_intercept(p2, v2)
    if m1 != m2:
        x_intercept = (b2 - b1) / (m1 - m2)
        y_intercept = m1 * x_intercept + b1
        t_intercept_1 = (x_intercept - p1[0]) / v1[0]
        t_intercept_2 = (x_intercept - p2[0]) / v2[0]
        if t_intercept_1 >= 0 and t_intercept_2 >= 0:
            return x_intercept, y_intercept


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

    print(f"Day 24-1: {total}")