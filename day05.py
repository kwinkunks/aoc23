from pathlib import Path

text = Path('./data/05.txt').read_text()

import re

# Get data.
pattern = re.compile(r":(.+?)\n\n", re.DOTALL)
seeds, *maps = pattern.findall(text)

# Iterate over seeds, iterating over maps for each.
dests = []
for seed in map(int, seeds.split()):
    for map_ in ((filter(None, m.split('\n'))) for m in maps):
        for dest, src, rng in (map(int, m.split()) for m in map_):
            if src <= seed < (src + rng):
                seed = dest + (seed - src)
                break

    dests.append(seed)

print(min(dests))

# Part 2.
seeds = list(map(int, seeds.split()))
maps = [list((filter(None, m.split('\n')))) for m in maps]

ranges = []
for start, rng in zip(seeds[::2], seeds[1::2]):
    ranges.append(range(start, start+rng))

# A lot of plotting of groups and ranges to eventually
# get to the 7th cohort, 12 million from the end... :(
min_dest = 1e30
for seeds in ranges[7:8]:            # Pick up a seed range...
    for seed in seeds[-12_000_000:-11_800_000]:    # Take one seed...
        for map_ in maps:       # Pick up a map...
            this_map = (map(int, m.split()) for m in map_)
            for dest, src, rng in this_map:
                          # Check every row in this map.
                if src <= seed < (src + rng):
                    seed = dest + (seed - src)
                    break
        if seed < min_dest:
            min_dest = seed

print(min_dest)
