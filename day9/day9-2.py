def all_zeros(seq):
    return all([element == 0 for element in seq])

def extrapolate_val(seq):
    sequences = [seq]
    while not all_zeros(seq):
        new_seq = []
        for i in range(1, len(seq)):
            new_seq.append(seq[i] - seq[i - 1])
        sequences.append(new_seq)
        seq = new_seq

    val = 0
    prev_val = 0
    for i in reversed(range(0, len(sequences))):
        prev_val = (sequences[i][0] - prev_val)
        val += prev_val
    return prev_val


def parse(lines):
    total = 0
    for line in lines:
        total += extrapolate_val([int(i) for i in line.split()])
    return total


with open("day9.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 9-2: {total}")
