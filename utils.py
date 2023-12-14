
def levenshtein(str1, str2):
    """
    https://rosettacode.org/wiki/Levenshtein_distance#Python
    License: GFDL
    """
    m = len(str1)
    n = len(str2)
    d = [[i] for i in range(1, m + 1)]
    d.insert(0, list(range(0, n + 1)))
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                substitutionCost = 0
            else:
                substitutionCost = 1
            d[i].insert(j, min(d[i - 1][j] + 1,
                               d[i][j - 1] + 1,
                               d[i - 1][j - 1] + substitutionCost))
    return d[-1][-1]
