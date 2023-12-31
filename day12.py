from pathlib import Path
from functools import cache

text = Path('./data/12.txt').read_text()

rows, rles = [], []
for row in text.splitlines():
    s, r = row.split()
    rows.append(s)
    rles.append(''.join(r.split(',')))

# Guessing brute force will work for part 1 but not part 2
@cache
def get_rle(row):
    this = ''
    rl = 0
    row += '.'
    for s1, s2 in zip(row, row[1:]):
        if s1 == '#':
            rl += 1 
            if s2 == '.':
                this += str(rl)
        else:
            rl = 0
    return this

@cache
def permutations(row):
    perms = [row]
    while any('?' in p for p in perms):
        perm = perms.pop(0)
        for c in '.#':
            perms.append(perm.replace('?', c, 1))
    return perms

arrs = []
for row, rle in zip(rows, rles):

    matches = [(get_rle(5*perm) == 5*rle) for perm in permutations(5*row)]
    n = len([m for m in matches if m])
    arrs.append(n)

print(sum(arrs))
