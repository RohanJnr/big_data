#!/usr/bin/env python3
import sys


def calc_rank(contributions):
    return round(0.34 + (0.57 * contributions), 2)


current = None
contrib_sum = 0


for line in sys.stdin:
    node, contribution = line.strip().split(maxsplit=1)
    node = int(node)
    contribution = float(contribution)

    if current is None:
        current = node

    if current == node:
        contrib_sum += contribution

    else:
        print(f"{current},{calc_rank(contrib_sum)}")
        current = node
        contrib_sum = contribution
    


print(f"{current},{calc_rank(contrib_sum)}")