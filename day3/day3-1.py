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


def find_parts_total(mat):

    padded_mat = np.pad(mat, pad_width=1, mode='constant', constant_values=0)

    valid_symbols = string.punctuation.replace(".", "")
    total = 0
    for col in range(1, len(padded_mat) - 1):
        current_nb = ""
        is_part = False
        for row in range(1, len(padded_mat[0]) - 1):
            c = padded_mat[col][row]
            if c.isdigit():
                current_nb += c
                if has_adjacent_symbol(padded_mat, row, col, valid_symbols):
                    is_part = True
            else:
                if is_part:
                    total += int(current_nb)
                current_nb = ""
                is_part = False
        if is_part:
            total += int(current_nb)
    return total


with open("day3.txt", 'r') as f:
    lines = f.read().splitlines()

    mat = as_matrix(lines)
    total = find_parts_total(mat)

    print(f"Day 3-1: {total}")
