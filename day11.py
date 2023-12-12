from pathlib import Path

text = Path('./data/11.txt').read_text()

# Find the empty columns.
galaxies = []
for y, row in enumerate(text.split('\n')):
    for x, c in enumerate(row):
        if c == '#':
            galaxies.append(complex(x, y))

maxc = int(max(g.real for g in galaxies))

empty_cols = []
for c in range(maxc):
    if not any(g.real==c for g in galaxies):
        empty_cols.append(c)

# Now re-parse and adjust the coordinates.
factor = 1_000_000

galaxies = []
yadj = 0
for y, row in enumerate(text.split('\n')):
    xadj = 0
    if '#' not in row:
        yadj += factor - 1
        continue
    for x, c in enumerate(row):
        if x in empty_cols:
            xadj += factor - 1
        if c == '#':
            galaxies.append(complex(x+xadj, y+yadj))

# L1 norm between all pairs
dists = []
while galaxies:
    g1 = galaxies.pop()
    for g2 in galaxies:
        dist = abs(g1.real-g2.real) + abs(g1.imag-g2.imag)
        dists.append(int(dist))

print(sum(dists))
