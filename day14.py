from pathlib import Path

text = Path('./data/14.txt').read_text()

blocks, spheres = [], []
for y, row in enumerate(text.split('\n')):
    for x, c in enumerate(row):
        if c == '#':
            blocks.append(complex(x, y))
        elif c == 'O':
            spheres.append(complex(x, y))

cycles = 180  # Captures cyclicity, then extrapolate.

def score(spheres, y):
    return sum((y + 1 - s.imag) for s in spheres)

scores = []
for cycle in range(cycles):
    for rot in range(4):
        edge = min(s.imag for s in blocks)
        moving = 1
        while moving:
            moving = 0
            for s, sphere in enumerate(spheres):
                arrived = sphere.imag == edge
                proposal = sphere + (0 - 1j)
                blocked = proposal in blocks
                sphered = proposal in spheres
                if not (arrived or blocked or sphered):
                    spheres[s] = proposal
                    moving += 1
        spheres = [s * 1j for s in spheres]
        blocks = [s * 1j for s in blocks]
    print('.', end='')
    scores.append(score(spheres, y))

print(scores)
print(score(spheres, y))
