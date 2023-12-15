from pathlib import Path
from collections import defaultdict

text = Path('./data/15.txt').read_text()
steps = text.split(',')

def HASH(s):
    H = 0
    for c in s:
        H += ord(c)
        H *= 17
        H %= 256
    return H

# Part 1.
print(sum(HASH(step) for step in steps))

# Part 2.
boxes = defaultdict(list)
lenses = {}
for step in steps:
    if '-' in step:
        lens = step[:-1]
        box = HASH(lens)
        if box in boxes and lens in boxes[box]:
            boxes[box].remove(lens)
    else:
        lens, fl = step.split('=')
        lenses[lens] = int(fl)
        box = HASH(lens)
        if lens not in boxes.get(box, []):
            boxes[box].append(lens)

def get_power(boxes, lenses):
    power = 0
    for box, slots in boxes.items():
        for s, lens in enumerate(slots):
            power += (box + 1) * (s + 1) * lenses[lens]
    return power

print(get_power(boxes, lenses))