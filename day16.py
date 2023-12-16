from pathlib import Path
from collections import deque, defaultdict

text = Path('./data/16.txt').read_text()

instruments = defaultdict(list)
for r, row in enumerate(text.split()):
    for c, char in enumerate(row):
        instruments[char].append(complex(c, r))

DLS = lambda dir: -1j if dir.real else 1j
DRS = lambda dir: 1j if dir.real else -1j

def trace(start, dir):
    paths = deque([(start, dir)])
    visited, history = set(), set()
    while paths:
        pos, dir = paths.popleft()
        # Discard
        if pos.real < 0 or pos.imag < 0: continue
        if pos.real > c or pos.imag > r: continue
        if (pos, dir) in history: continue
        # Record
        visited.add(pos)
        history.add((pos, dir))
        # Move
        if pos in instruments['#']:
            dir *= DRS(dir)
        elif pos in instruments['/']:
            dir *= DLS(dir)
        elif dir.real and pos in instruments['|']:
            dir *= DLS(dir)
            paths.append((pos-dir, -dir))
        elif dir.imag and pos in instruments['-']:
            dir *= DLS(dir)
            paths.append((pos-dir, -dir))
        paths.append((pos+dir, dir))
    return visited

# Part 1.
visited = trace(complex(0, 0), complex(1, 0))
print(len(visited))

# Part 2.
energies = []
for x in range(c):
    for y in (0, r):
        visited = trace(complex(x, y), complex(0, -1 if y else 1))
        energies.append(len(visited))
for x in (0, c):
    for y in range(r):
        visited = trace(complex(x, y), complex(-1 if x else 1, 0))
        energies.append(len(visited))
print(max(energies))
