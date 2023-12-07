from pathlib import Path

text = Path('./data/7.txt').read_text()
data = [row.split() for row in text.split('\n')]
hands = [row[0] for row in data]
bids = list(map(int, (row[1] for row in data)))
game = {h:b for h, b in zip(hands, bids)}

# Group, then sort, then regroup.
from collections import Counter

# Rely on order, low to high type.
groups = {}
for type_ in ['h', 2, 't', 3, 'f', 4, 5]:
    groups[type_] = list()

# Score hands.
for hand in hands:
    c = Counter(hand)
    if max(c.values()) == 5:
        groups[5].append(hand)
    elif max(c.values()) == 4:
        groups[4].append(hand)
    elif max(c.values()) == 3:
        if min(c.values()) == 2:
            groups['f'].append(hand)
        else:
            groups[3].append(hand)
    elif max(c.values()) == 2:
        if len(set(hand)) == 3:
            groups['t'].append(hand)
        else:
            groups[2].append(hand)
    else:
        groups['h'].append(hand)

# Ordering function.
def strength(hand):
    strengths = "AKQJT98765432"
    return tuple(strengths.find(c) for c in hand)

# Rank.
all_hands = []
for _, group in groups.items():
    all_hands.extend(sorted(group, key=strength, reverse=True))

# Count winnings.
winnings = 0
for i, hand in enumerate(all_hands):
    winnings += (i + 1) * game[hand]

# Part 1.
print(winnings)
