from pathlib import Path

text = Path('./data/01.txt').read_text()

numbers = []
for line in text.split('\n'):
    digits = [c for c in line if c.isdigit()]
    numbers.append(digits[0] + digits[-1])
print(sum(int(n) for n in numbers))

# Part 2
# Okay I give up... use re
import re

digits_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = {s:str(n+1) for s, n in zip(digits_list, range(len(digits_list)))}

pattern = re.compile(f"({'|'.join(digits_list)}|[1-9])")

numbers = []
for line in text.split('\n'):
    d1, *_ = pattern.findall(line)

    # Not so simple for d2 because of overlaps like oneight: regex catches one
    # but I want eight. So build the string backwards and check. Ugh...
    for i in range(len(line)):
        if (found := pattern.search(line[-(i+1):])):
            d2, = found.groups(0)
            break
    numbers.append(digits.get(d1, d1) + digits.get(d2, d2))
print(sum(int(n) for n in numbers))

# Re not that useful then, unless there's a way to scan backwards.
# Could refactor it out.
