import math


def score(x, y):
    dist = math.hypot(x, y)
    return 0 if dist > 10 else 1 if dist > 5 else 5 if dist > 1 else 10
