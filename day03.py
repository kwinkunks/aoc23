from collections import defaultdict
from pathlib import Path

text = Path('./data/03.txt').read_text()

numbers = defaultdict(str)  # tuple: str (then int)
parts = {}    # tuple: str
mapping = {}
npos = 0

for r, row in enumerate(text.split()):
    for c, char in enumerate(row):
        if char.isdigit() and npos:
            numbers[npos] += char
        elif char.isdigit():
            npos = complex(c, r)
            numbers[npos] += char
        elif char != '.':
            parts[complex(c, r)] = char
            npos = 0
        elif npos:
            npos = 0
        else:
            pass # npos is 0 already

offsets = [-1-1j, 0-1j, 1-1j, -1, 1, -1+1j, 0+1j, 1+1j]

def neighbours(pos, n) -> set:
    positions = set()
    for i, c in enumerate(n):
        for o in offsets:
            positions.add(pos+i+o)
    # print(positions)
    return positions

# Assuming that a given label only ever has one part adjacent to it,
# can iterate over labels and get the position of its part, then
# keep a dict of part location : labels with that part location.
part_map = defaultdict(list)
for pos, n in numbers.items():
    for neighbour in neighbours(pos, n):
        if neighbour in parts:
            part_map[neighbour].append(pos)

# Part 1
values = []
for part, labels in part_map.items():
    if len(labels) == 2:
        a, b = labels
        values.append(int(numbers[a]) + int(numbers[b]))
    else:
        values.append(int(numbers[labels[0]]))
print(sum(values))

# Part 2
ratios = []
for part, labels in part_map.items():
    if len(labels) == 2:
        a, b = labels
        ratios.append(int(numbers[a]) * int(numbers[b]))
print(sum(ratios))
