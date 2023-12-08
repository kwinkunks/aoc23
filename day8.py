from pathlib import Path
import re
import math

text = Path('./data/8.txt').read_text()

turns, node_text = text.split('\n\n')

turns = [0 if t == 'L' else 1 for t in turns]
nodes = {}
for line in node_text.split('\n'):
    n, l, r = re.search(f'(\w+?) = \((\w+?), (\w+?)\)', line).groups()
    nodes[n] = (l, r)

# Part 1.
def atoz(node, is_target):
    done, steps = 0, 0
    while not done:
        for turn in turns:
            node = nodes[node][turn]
            steps += 1
            if is_target(node):
                done = True
                break
    return steps
    
print(atoz('AAA', lambda n: n=='ZZZ'))

# Part 2.
starts = ['AAA', 'MGA', 'DGA', 'TLA', 'RDA', 'DPA']
all_steps = [atoz(s, lambda n: n[-1]=='Z') for s in starts]

print(math.lcm(*all_steps))
