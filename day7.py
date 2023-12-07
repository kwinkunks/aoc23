from pathlib import Path
from collections import Counter

text = Path('./data/7.txt').read_text()
data = [row.split() for row in text.split('\n')]
hands = {a: int(b) for a, b in data}

# Score hands.
def get_type(hand):
    counts = Counter(hand).values()
    g = str(max(counts))
    if max(counts) == 3 and min(counts) == 2:
        g = 'f'  # Full house.
    if max(counts) == 2 and len(set(hand)) == 3:
        g = 't'  # Two pair.
    return g

# Rely on order, low to high type.
TYPES = '12t3f45'
def typeset(hands):
    typesets = {t: list() for t in TYPES}
    for hand in hands:
        typesets[get_type(hand)].append(hand)
    return typesets

# Ordering closure to use as sort key.
STRENGTHS = "AKQJT98765432"
def strength(wild=''):
    def f(hand):
        strengths = STRENGTHS.replace(wild, '') + wild
        return tuple(strengths.find(c) for c in hand)
    return f

# Rank.
def rank(typesets, wild=''):
    all_hands = []
    for _, group in typesets.items():
        sort = sorted(group, key=strength(wild), reverse=True)
        all_hands.extend(sort)
    return all_hands

# Count winnings.
winnings = 0
for i, hand in enumerate(rank(typeset(hands))):
    winnings += (i + 1) * hands[hand]

# Part 1.
print(winnings)

# Part 2.
def best_permutation(hand, wild=''):
    perms = []
    for s in STRENGTHS.replace(wild, ''):
        perms.append(hand.replace(wild, s, 1))
    return rank(typeset(perms))[-1]

new_hands = {}
for hand, bid in hands.items():
    hand_ = hand
    for _ in range(hand.count('J')):
        hand_ = best_permutation(hand_, wild='J')
    new_hands[hand] = hand_ 
    # Annoying but has to be this way around.

# Well, this is horrific.
all_hands = []
wild_hands = new_hands.values()
for _, group in typeset(wild_hands).items():
    true_hands = []
    for wild_hand in group:  # Oh...
        for hand, hand_ in new_hands.items():  # my...
            if wild_hand == hand_:  # god...
                true_hands.append(hand)
                new_hands.pop(hand)  # sob.
                break
    sort = sorted(true_hands, key=strength(wild='J'), reverse=True)
    all_hands.extend(sort)

winnings = 0
for i, hand in enumerate(all_hands):
    winnings += (i + 1) * hands[hand]

print(winnings)