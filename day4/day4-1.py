import math

def parse(lines):
    total = 0
    for line in lines:
        card_nb, cards = line.split(":")
        my_nbs, win_nbs = cards.split("|")
        my_nbs = set(s for s in my_nbs.strip().split(" ") if s)
        win_nbs = set(s for s in win_nbs.strip().split(" ") if s)
        winners = my_nbs & win_nbs

        total += int(math.pow(2, len(winners) - 1))
    return total




with open("day4.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 4-1: {total}")
