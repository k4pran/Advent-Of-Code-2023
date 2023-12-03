import string
import numpy as np

def as_matrix(lines):
    mat = []
    for line in lines:
        row = []
        for c in line:
            row.append(c)
        mat.append(row)
    return np.array(mat)


def has_adjacent_symbol(mat, row, col, valid_symbols):
    # Top left
    if mat[col - 1][row - 1] in valid_symbols:
        return True
    # Top
    if mat[col - 1][row] in valid_symbols:
        return True
    # Top Right
    if mat[col - 1][row + 1] in valid_symbols:
        return True
    # Right
    if mat[col][row + 1] in valid_symbols:
        return True
    # Bottom Right
    if mat[col + 1][row + 1] in valid_symbols:
        return True
    # Bottom
    if mat[col + 1][row] in valid_symbols:
        return True
    # Bottom Left
    if mat[col + 1][row - 1] in valid_symbols:
        return True
    # Left
    if mat[col][row - 1] in valid_symbols:
        return True
    return False

def get_adjacent_indices(col, row):
    return [(col - 1, row - 1),
            (col - 1, row),
            (col - 1, row + 1),
            (col, row + 1),
            (col + 1, row + 1),
            (col + 1, row),
            (col + 1, row - 1),
            (col, row - 1)]


def find_parts_indices(padded_mat):
    valid_symbols = string.punctuation.replace(".", "")
    parts_indices = []
    for col in range(1, len(padded_mat) - 1):
        current_nb_indices = []
        is_part = False
        for row in range(1, len(padded_mat[0]) - 1):
            c = padded_mat[col][row]
            if c.isdigit():
                current_nb_indices.append((col, row))
                if has_adjacent_symbol(padded_mat, row, col, valid_symbols):
                    is_part = True
            else:
                if is_part:
                    parts_indices.append(current_nb_indices)
                current_nb_indices = []
                is_part = False
        if is_part:
            parts_indices.append(current_nb_indices)
    return parts_indices


def get_adjacent_parts_count(parts_indices, gear_index):
    adjacent_indices = get_adjacent_indices(gear_index[0], gear_index[1])
    adjacent_parts = set()
    for adj in adjacent_indices:
        for part_indices in parts_indices:
            part_match_found = False
            for part_index in part_indices:
                if part_index == adj:
                    part_match_found = True
                    break
            if part_match_found:
                adjacent_parts.add(tuple(part_indices))
                continue
    return list(adjacent_parts)


def get_number_from_indices(mat, indices):
    nb = ""
    for index in indices:
        nb += mat[index[0], index[1]]
    return int(nb)


def calculate_gears(mat, parts_indices):
    total = 0
    for col in range(1, len(padded_mat) - 1):
        for row in range(1, len(padded_mat[0]) - 1):
            c = padded_mat[col][row]
            if c != '*':
                continue
            adjacent_parts = get_adjacent_parts_count(parts_indices, (col, row))
            if len(adjacent_parts) == 2:
                gear_ratio = get_number_from_indices(mat, adjacent_parts[0]) * get_number_from_indices(mat, adjacent_parts[1])
                total += gear_ratio
    return total


with open("day3.txt", 'r') as f:
    lines = f.read().splitlines()

    mat = as_matrix(lines)
    padded_mat = np.pad(mat, pad_width=1, mode='constant', constant_values=0)

    parts_indices = find_parts_indices(padded_mat)
    total = calculate_gears(padded_mat, parts_indices)

    print(f"Day 3-1: {total}")
