directions = dict(zip(['U', 'D', 'L', 'R'], [(0, 1), (0, -1), (-1, 0), (1, 0)]))

def visualize(perimeter):
    min_x = min(point[0] for point in perimeter)
    max_x = max(point[0] for point in perimeter)
    min_y = min(point[1] for point in perimeter)
    max_y = max(point[1] for point in perimeter)

    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if (x, y) in perimeter:
                print('#', end='')
            else:
                print('.', end='')
        print()


def calculate_lagoon_size(perimeter):
    sum_1 = 0
    sum_2 = 0
    nb_edges = len(perimeter)
    for i in range(0, nb_edges - 1):
        sum_1 += perimeter[i][0] * perimeter[i + 1][1]
        sum_2 += perimeter[i + 1][0] * perimeter[i][1]

    sum_1 += perimeter[nb_edges-1][0] * perimeter[0][1]
    sum_2 += perimeter[0][0] * perimeter[nb_edges - 1][1]

    return abs(sum_1 - sum_2) / 2



# FAILS for U shapes
# def calculate_lagoon_size(perimeter):
#     min_y = min(point[1] for point in perimeter)
#     max_y = max(point[1] for point in perimeter)
#
#     total_filled = 0
#     for y in range(max_y, min_y - 1, -1):
#         min_x = min(point[0] for point in perimeter if point[1] == y)
#         max_x = max(point[0] for point in perimeter if point[1] == y)
#         total_filled += (max_x - min_x) + 1
#     return total_filled


def dig(lines):
    pos = (0, 0)
    perimeter = []
    for line in lines:
        d, m, rgb = line.split()
        px, py = pos
        mx, my = directions[d]

        # interpolate
        for step in range(0, int(m) + 1):
            x_step = mx * step
            y_step = my * step
            pos = (px + x_step, py + y_step)
            if pos not in perimeter:
                perimeter.append(pos)

    # visualize(perimeter)
    print(perimeter)
    return (calculate_lagoon_size(perimeter) + (len(perimeter) / 2)) + 1


with open("day18.txt", 'r') as f:
    text = f.read().splitlines()

    total = dig(text)

    print(f"Day 18-1: {total}")


# 58960 too high