import math
from collections import deque

adjacent_incs = (-1, 0), (0, 1), (1, 0), (0, -1)

def as_mat(rows):
    return [[row for row in col] for col in rows]


def get_starting_point(mat):
    for i, row in enumerate(mat):
        for j, col in enumerate(row):
            if col == "S":
                return i, j


def is_inside_mat(mat, p):
    rows = len(mat)
    if rows == 0:
        return False
    cols = len(mat[0])

    x, y = p
    return 0 <= x < rows and 0 <= y < cols


def is_connecting(p, adjacent_p, p_start_type, adj_square_type):
    if adj_square_type == ".":
        return False
    if adj_square_type == "|":
        return p[0] != adjacent_p[0]
    if adj_square_type == "-":
        return p[1] != adjacent_p[1]
    if adj_square_type == "L":
        return (p[1] > adjacent_p[1] and p_start_type in ["-", "J", "7", "S"]) or (p[0] < adjacent_p[0] and p_start_type in ["|", "7", "F", "S"])
    if adj_square_type == "J":
        return (p[1] < adjacent_p[1] and p_start_type in ["-", "L", "F", "S"]) or (p[0] < adjacent_p[0] and p_start_type in ["|", "7", "F", "S"])
    if adj_square_type == "7":
        return (p[1] < adjacent_p[1] and p_start_type in ["-", "L", "F", "S"]) or (p[0] > adjacent_p[0] and p_start_type in ["|", "L", "J", "S"])
    if adj_square_type == "F":
        return (p[1] > adjacent_p[1] and p_start_type in ["-", "J", "7", "S"]) or (p[0] > adjacent_p[0] and p_start_type in ["|", "L", "J", "S"])
    return True

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

def get_adjacent_squares(mat, p):
    adjacent_squares = []
    for adj_inc in adjacent_incs:
        adjacent_p = (p[0] + adj_inc[0], p[1] + adj_inc[1])
        if is_inside_mat(mat, adjacent_p) and is_connecting(p, adjacent_p, mat[p[0]][p[1]], mat[adjacent_p[0]][adjacent_p[1]]):
            adjacent_squares.append(adjacent_p)
    return adjacent_squares


def manhattan_dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def traverse_pipes(mat, start, distance_mat, visited=None, path_length=0):
    if visited is None:
        visited = set()
    # if path is None:
    #     path = []

    visited.add(start)
    # path.append(start)

    for adj in get_adjacent_squares(mat, start):
        if adj not in visited:
            distance_mat[adj[0]][adj[1]] = len(visited)
            traverse_pipes(mat, adj, distance_mat, visited, path_length + 1)

    print(path_length)
    return visited, distance_mat

def get_farthest_dist(mat):
    start = get_starting_point(mat)

    zeros_mat = [[0 for _ in col] for col in mat]
    visited, distance_mat = traverse_pipes(mat, start, zeros_mat)
    for row in distance_mat:
        print(row)

    return len(visited)


with open("day10.txt", 'r') as f:
    lines = f.read().splitlines()

    mat = as_mat(lines)
    dist = get_farthest_dist(mat)

    # print(f"Day 10-1: {dist}")
