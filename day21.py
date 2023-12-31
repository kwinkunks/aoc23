from pathlib import Path

text = Path('./data/21.txt').read_text()

rocks = set()
for r, row in enumerate(text.split()):
    for c, char in enumerate(row):
        if char == '#':
            rocks.add(complex(c, r))
        if char == "S":
            start = complex(c, r)
from functools import cache
from collections import defaultdict
steps = defaultdict(set)
steps[start].add(0)
STEPS = -1, 1, -1j, 1j

@cache
def check(pos):
    ok = []
    for step in STEPS:
        if (q := pos + step) not in rocks:
            ok.append(q)
    return ok

for i in range(1, 65):
    sources = [p for p, v in steps.items() if i-1 in v]
    for p in sources:
        for q in check(p):
            steps[q].add(i)

print(len([s for s,v in steps.items() if 64 in v]))

steps = set()
steps.add(start)
STEPS = -1, 1, -1j, 1j

@cache
def check(pos):
    ok = []
    for step in STEPS:
        q = pos + step
        if complex(q.real%132, q.imag%132) not in rocks:
            ok.append(q)
    return ok

states = []
for i in range(1, 600):
    this = set()
    for p in steps:
        this.update(check(p))
    states.append(len(this))
    steps = this

print(len(steps))

print(states)