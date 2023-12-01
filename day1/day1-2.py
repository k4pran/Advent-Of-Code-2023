from typing import Callable

number_names = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]


def find_number(i: int, substring_indexing_fn: Callable):
    for number_name in number_names:
        if number_name in substring_indexing_fn(line, i):
            return str(number_names.index(number_name) + 1)


def get_boundary_number(line: str, index_range: [range, reversed], substring_indexing_fn: Callable):
    for i in index_range:
        if line[i].isdigit():
            return line[i]

        name_as_number = find_number(i, substring_indexing_fn)
        if name_as_number:
            return name_as_number


with open("day1.txt", 'r') as f:
    lines = f.read().splitlines()

    total = 0
    for line in lines:
        digits = [get_boundary_number(line, range(0, len(line)), lambda l, i: l[:i + 1]),
                  get_boundary_number(line, reversed(range(0, len(line))), lambda l, i: l[i:])]
        number = digits[0] + digits[-1]
        total += int(number)

    print(f"Day 1-2: {total}")