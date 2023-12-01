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

def get_first_number(line: str):
    for i in range(0, len(line)):
        if line[i].isdigit():
            return line[i]
        for number_name in number_names:
            if number_name in line[0:i + 1]:
                return str(number_names.index(number_name) + 1)

def get_last_number(line: str):
    for i in reversed(range(0, len(line))):
        if line[i].isdigit():
            return line[i]
        for number_name in number_names:
            if number_name in line[i:]:
                return str(number_names.index(number_name) + 1)

with open("day1.txt", 'r') as f:
    lines = f.read().splitlines()

    total = 0
    for line in lines:
        digits = [get_first_number(line), get_last_number(line)]
        number = digits[0] + digits[-1]
        total += int(number)

    print(f"Day 1-2: {total}")