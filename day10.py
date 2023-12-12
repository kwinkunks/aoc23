from pathlib import Path
import shapely

text = Path('./data/10.txt').read_text()

def parse(data):
    grid = {}
    for r, row in enumerate(data.splitlines()):
        for c, char in enumerate(row):
            if char == 'S':
                start = complex(c, r)
            grid[complex(c, r)] = char
    return grid, start


# Map step taken to next step for each pipe type.
STEPS = {
    "-": { -1: -1,  1: 1},
    "|": {-1j:-1j, 1j:1j},
    "F": { -1: 1j,-1j: 1},
    "L": { -1:-1j, 1j: 1},
    "J": {  1:-1j, 1j:-1},
    "7": {-1j: -1,  1:1j},
}

# Explore.
grid, start = parse(text)
curr, step, s = start, -1, 0
vertices = []
while (not vertices) or grid.get(curr) != 'S':
    vertices.append((curr.real, curr.imag))
    symb = grid.get(curr)
    step = STEPS.get(symb, {-1:-1})[step]  # Annoying hack.
    curr += step

# Part 1.
print(len(vertices) // 2)

# Part 2.
# Shoelace formula (sum cross products): way too high.
# Use shapely and get area of polygon. Now what?
# Check every point, sigh, so slow but it works!
# Wait, there's Pick's theorem...

P = shapely.Polygon(vertices)

# Pick's theorem
# https://en.wikipedia.org/wiki/Pick%27s_theorem
# A = i + b/2 - 1
# where b is points on boundary, which is my s
# and   i is integer points
# so    i = A + 1 - b/2

print(int(P.area + 1 - len(vertices)//2))

# It works!! Noice.
