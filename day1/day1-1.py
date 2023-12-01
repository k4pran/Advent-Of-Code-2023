with open("day1.txt", 'r') as f:
    lines = f.read().splitlines()

    total = 0
    for line in lines:
        digits = [i for i in line if str.isdigit(i)]
        number = digits[0] + digits[-1]
        total += int(number)

    print(f"Day 1-1: {total}")