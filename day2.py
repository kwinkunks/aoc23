from pathlib import Path

text = Path('./data/2.txt').read_text()

class Game:

    def __init__(self, s):
        self.rgb = []
        for gamelet in s.split(';'):
            d = [0, 0, 0]
            if r := re.search(r"(\d+) r", gamelet):
                d[0] = int(r.groups(0)[0])
            if g := re.search(r"(\d+) g", gamelet):
                d[1] = int(g.groups(0)[0])
            if b := re.search(r"(\d+) b", gamelet):
                d[2] = int(b.groups(0)[0])
            self.rgb.append(tuple(d))

    def max(self):
        return [max(rgb[i] for rgb in self.rgb) for i in (0, 1, 2)]

    def power(self):
        max_ = self.max()
        return max_[0] * max_[1] * max_[2]

# Part 1
import re # so lazy

maxa = 12, 13, 14
total = 0
for i, game in enumerate(re.findall(r'Game \d+: (.+)', text)):
    maxx = Game(game).max()
    if not any(x > y for x, y in zip(maxx, maxa)):
        total += i+1
print(total)

# Part 2
total = 0
for i, game in enumerate(re.findall(r'Game \d+: (.+)', text)):
    total += Game(game).power()
print(total)
