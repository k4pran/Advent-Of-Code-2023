from sympy import symbols, solve

def get_hailstones(lines):
    hailstones = []
    for line in lines:
        p, v = line.replace(" ", "").split("@")
        p = [int(pos) for pos in p.split(",")]
        v = [int(vel) for vel in v.split(",")]
        hailstones.append((p, v))
    return hailstones

def find_intersection(lines):
    hailstones = get_hailstones(lines)

    px, py, pz, vx, vy, vz = symbols("px, py, pz, vx, vy, vz")
    equations = []
    for i, (pos, vel) in enumerate(hailstones):

        equations.append((px - pos[0]) * (vel[1] - vy) - (py - pos[1]) * (vel[0] - vx))
        equations.append((py - pos[1]) * (vel[2] - vz) - (pz - pos[2]) * (vel[1] - vy))

        if i == 0:
            continue

        solution = [soln for soln in solve(equations) if all(x % 1 == 0 for x in soln.values())]

        if solution:
            return sum([v for v in solution[0].values()][:len(pos)])

    return -1

with open("day24.txt", 'r') as f:
    lines = f.read().splitlines()

    total = find_intersection(lines)

    print(f"Day 24-2: {total}")