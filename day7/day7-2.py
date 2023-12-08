from collections import Counter
from functools import cmp_to_key

card_values = {"j": 0,
               "2": 2,
               "3": 3,
               "4": 4,
               "5": 5,
               "6": 6,
               "7": 7,
               "8": 8,
               "9": 9,
               "T": 10,
               "J": 11,
               "Q": 12,
               "K": 13,
               "A": 14}


def get_hand_strength(hand):
    tally = Counter(hand)
    most_common = tally.most_common()[0][1]
    if most_common == 5:
        return 6
    if most_common == 4:
        return 5
    if 2 in tally.values() and 3 in tally.values():
        return 4
    if most_common == 3:
        return 3
    if most_common == 2:
        if Counter(tally.values()).most_common()[0][1] == 2:
            return 2
        return 1
    return 0


def sort_ranks(hand_1, hand_2):
    if hand_1[2] != hand_2[2]:
        if hand_1[2] < hand_2[2]:
            return -1
        if hand_1[2] > hand_2[2]:
            return 1
    cards_1 = hand_1[0]
    cards_2 = hand_2[0]

    for i in range(len(cards_1)):
        if cards_1[i] != cards_2[i]:
            card_1_val = card_values[cards_1[i]]
            card_2_val = card_values[cards_2[i]]

            if card_1_val < card_2_val:
                return -1
            if card_1_val > card_2_val:
                return 1
    return 0


def get_winnings(hands):
    winnings = 0
    for i, hand in enumerate(hands):
        print(f"{int(hand[1])} * {(i + 1)}")
        winnings += int(hand[1]) * (i + 1)
    return winnings

def parse(lines):

    total = 0
    card_tuples = []
    for line in lines:
        hand, bid = line.split()
        rank = get_hand_strength(hand)

        card_tuples.append((hand, bid, rank))

    sorted_hands = sorted(card_tuples, key=cmp_to_key(sort_ranks))

    return get_winnings(sorted_hands)


with open("day7.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 7-1: {total}")
