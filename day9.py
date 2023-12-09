from pathlib import Path

text = Path('./data/9.txt').read_text()

# text = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""

histories = [list(map(int, row.split())) for row in text.split('\n')]

def predict(history, prequel=False, f=sum):
    "f is cumulating function"
    X = [history[prequel-1]]
    while True:
        history = [j - i for i, j in zip(history, history[1:])]
        if not any(history): break
        X.append(history[prequel-1])
    return f(X)

print(sum(map(predict, histories)))

# Part 2.
def cumsub(X):
    "Cumulative subtraction"
    result = 0
    for xi in reversed(X):
        result = xi - result
    return result

preds = [predict(h, prequel=True, f=cumsub) for h in histories]

print(sum(preds))
