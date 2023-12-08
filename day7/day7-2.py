from collections import Counter
from functools import cmp_to_key

card_values = {"2": 2,
               "3": 3,
               "4": 4,
               "5": 5,
               "6": 6,
               "7": 7,
               "8": 8,
               "9": 9,
               "T": 10,
               "J": 0,
               "Q": 12,
               "K": 13,
               "A": 14}


def handle_jacks(hand, strength):
    if "J" not in hand:
        return strength
    nb_jacks = hand.count("J")
    # 5 of a kind - strength doesn't change
    if strength == 6:
        return strength
    # 4 of a kind - always gets upgraded to 5 of a kind
    if strength == 5:
        return 6
    # full house - either 2 or 3 jacks - can always be upgraded to 5 of a kind
    if strength == 4:
        return 6
    # three of a kind - 2 jacks
    if strength == 3:
        if nb_jacks == 1 or nb_jacks == 3:
            return 5
        if nb_jacks == 2:
            return 6
    # two pair
    if strength == 2:
        if nb_jacks == 2:
            return 5
        if nb_jacks == 1:
            return 4
    # pair
    if strength == 1:
        if nb_jacks == 3:
            return 6
        if nb_jacks == 2 or nb_jacks == 1:
            return 3
    if strength == 0:
        if nb_jacks == 1:
            # pair
            return 1

def get_hand_strength(hand):
    tally = Counter(hand)
    most_common = tally.most_common()[0][1]
    if most_common == 5:
        return handle_jacks(hand, 6)
    if most_common == 4:
        return handle_jacks(hand, 5)
    if 2 in tally.values() and 3 in tally.values():
        return handle_jacks(hand, 4)
    if most_common == 3:
        return handle_jacks(hand, 3)
    if most_common == 2:
        if Counter(tally.values()).most_common()[0][1] == 2:
            return handle_jacks(hand, 2)
        return handle_jacks(hand, 1)
    return handle_jacks(hand, 0)


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
        # print(f"{int(hand[1])} * {(i + 1)}")
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
    for hand in reversed(sorted_hands):
        print(hand[0])

    return get_winnings(sorted_hands)


with open("day7.txt", 'r') as f:
    lines = f.read().splitlines()

    total = parse(lines)

    print(f"Day 7-1: {total}")
