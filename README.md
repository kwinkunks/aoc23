# aoc23

No frills Python, no tests, docs, `if __name__ == '__main__`, etc.

**Spoilers follow.**

## Week 1

- **Day 1: Trebuchet?!** — Unusually hard for Day 1, especially Part 2 because of overlapping numeral names, e.g. `oneight`, where the `eight` is wanted but regex (say) picks up the `one`. Could easily refactor to avoid using regex. SLOC: 20.
- **Day 2: Cube Conundrum** — Fairly easy and quite enjoyable. Wrote a class, which made part 2 very easy to implement. SLOC: 32.
- **Day 3: Gear Ratios** — One of the classic grid problems, but a bit more interesting than usual with a many-to-one mapping of labels to symbols. I did not realize until afterwards that all the gears were `*` symbols; fortunately no other symbols had multiple labels. SLOC: 48.
- **Day 4: Scratchcards** — Fun problem, and thankfully all the special effects were only propagated forwards so a simple queue sufficed with no `while` loop needed. Used a class for a scratchcard and did not regret it. SLOC: 22.
- **Day 5: If You Give A Seed A Fertilizer** — The first of the "computationally intractable part 2" problems.  Considered trying to invert everything and work back through the maps, but in the end went with horribly hacky solution involving plotting ranges and extrapolating. Probably could be treated as an optimization problem with some random sampling, but I assume there's a smart solution. SLOC: 31 (but solution is not complete because it involved manual hacking).
- **Day 6: Wait For It** — Easy and (for me) very quick to solve. Part 2 seemed like it would be intractable but brute force did the trick in a few seconds. SLOC: 17.
- **Day 7: Camel Cards** — A simplified poker game (no straight or flush), with wild cards in Part 2. My solution for Part 1 was fairly fun and compact, but Part 2 blew up quite a bit when I realized that the hand type was from the 'wild' hand, but the rank was from the 'real' hand (with adjusted strength for the wild card). SLOC: 62.

Mostly fun so far. Weirdly this year I have only run my code on the given example once (and it passed, while the real data was not — classic).


## Week 2

- **Day 8: Haunted Wasteland** — Fun, not too hard graph problem. Part 2 was again the classic too-expensive problem, but after only a bit of flailing (thinking I could find a loop), I realized I could count each path separately and find the [lowest common multiple](https://en.wikipedia.org/wiki/Least_common_multiple). SLOC: 24.
