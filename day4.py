from pathlib import Path

text = Path('./data/4.txt').read_text()

class Card:
    def __init__(self, text, id):
        self.id = id
        self.winning = list(map(int, text[text.find(':')+1:text.find('|')].split()))
        self.numbers = list(map(int, text[text.find('|')+1:].split()))

    @property
    def matches(self):
        return len(set(self.numbers).intersection(self.winning))

    @property
    def score(self):
        return 2**(self.matches-1) if self.matches else 0

cards = [Card(line, i+1) for i, line in enumerate(text.split('\n'))]

print(sum(c.score for c in cards))

# Part 2
# Can get away with just adding, since we always add
# to cards ahead and process them when we get there.
quants = {c.id:1 for c in cards}

for cardid, quant in quants.items():
    card = cards[cardid - 1]
    for copy in range(quant ):
        for m in range(card.matches):
            quants[card.id + m + 1] += 1
    
print(sum(quants.values()))