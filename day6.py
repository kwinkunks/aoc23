from pathlib import Path

text = Path('./data/6.txt').read_text()

_, *times = text.split('\n')[0].split()
_, *recs = text.split('\n')[1].split()

# Part 1.
count, prod = 0, 1
for time, rec in zip(times, recs):
    time, rec = int(time), int(rec)
    for sec in range(time):
        count += 1 if sec * (time - sec) > rec else 0
    prod *= count

print(prod)

# Part 2.
time = int(''.join(times))
rec = int(''.join(recs))

count = 0
for sec in range(time):
    count += 1 if sec * (time - sec) > rec else 0

print(count)

# Well, that was easy.