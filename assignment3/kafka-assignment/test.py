from collections import defaultdict


def sample():
    return {
        "min": 0,
        "max": 0
    }

x = defaultdict(sample)


print(x[1])

print(dict(x))