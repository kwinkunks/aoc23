from pathlib import Path

text = Path('./data/14.txt').read_text()

text_ = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

blocks, spheres = [], []
for y, row in enumerate(text.split('\n')):
    for x, c in enumerate(row):
        if c == '#':
            blocks.append(complex(x, y))
        elif c == 'O':
            spheres.append(complex(x, y))

all_cycles = 1_000_000_000
cycles = 50

def score(spheres, y):
    return sum((y + 1 - s.imag) for s in spheres)

# print(spheres)

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
    # score_basis = max(s.imag for s in blocks)
    print('.', end='')
    scores.append(score(spheres, y))

print(scores)
print(score(spheres, y))
# if False:
#     for i in range(10):
#         for j in range(10):
#             x = '.'
#             if complex(j, i) in spheres:
#                 x = 'O'
#             if complex(j, i) in blocks:
#                 x = '#'
#             print(x, end='')
#         print('\n')

# print(spheres, y)
import matplotlib.pyplot as plt
plt.plot(scores)
plt.show()
# 3968064