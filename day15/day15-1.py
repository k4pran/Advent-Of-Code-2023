def parse(text):
    total = 0
    for step in text.split(","):
        # for key, val in step.split("="):
        current_val = 0
        for c in step:
            current_val += ord(c)
            current_val *= 17
            current_val %= 256
        total += current_val
    return total


with open("day15.txt", 'r') as f:
    text = f.read()

    total = parse(text)

    print(f"Day 15-1: {total}")
