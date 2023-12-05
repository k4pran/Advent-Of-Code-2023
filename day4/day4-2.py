import math

def init_scratch_dict(nb):
    d = {}
    for i in range(nb):
        d[str(i + 1)] = 1
    return d


def parse(lines):
    total = 0
    scratch_cards = init_scratch_dict(len(lines))
    for line in lines:
        card_nb, cards = line.split(":")
        card_nb = card_nb.split(" ")[-1]


        my_nbs, win_nbs = cards.split("|")
        my_nbs = set(s for s in my_nbs.strip().split(" ") if s)
        win_nbs = set(s for s in win_nbs.strip().split(" ") if s)
        winners = my_nbs & win_nbs

        for card in range(scratch_cards[card_nb]):
            for i in range(len(winners)):
                new_card_nb = str(i + 1)
                if new_card_nb not in scratch_cards:
                    continue
                scratch_cards[str(int(card_nb) + i + 1)] += 1
                total += 1

    return sum(scratch_cards.values())

with open("day4.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 4-1: {total}")
