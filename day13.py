from pathlib import Path
from utils import levenshtein

text = Path('./data/13.txt').read_text()

def match(r1, r2, diff=0):
    return levenshtein(''.join(r1), ''.join(r2)) == diff

def find(rows, diff=0):
    last, seens, hline = '', [], 0
    for r, row in enumerate(rows):
        if (row==last) or match(row, last, diff=diff):
            nexts = rows[r:min(len(rows),2*r)]
            seens_ = seens[-len(nexts):]
            if match(nexts, seens_[::-1], diff=diff):
                hline = r
                break
        seens.append(row)
        last = row
    return hline

for d in [0, 1]:  # Part 1, Part 2.
    hlines, vlines = [], []
    for pattern in text.split('\n\n'):
        rows = pattern.split()
        hlines.append(find(rows, d))
        cols = []
        for i in range(len(rows[0])):
            cols.append(''.join([row[i] for row in rows]))
        vlines.append(find(cols, d))

    scores = []
    for h, v in zip(hlines, vlines):
        scores.append(100*h + v)

    print(sum(scores))
