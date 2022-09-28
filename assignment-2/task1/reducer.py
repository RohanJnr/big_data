#!/usr/bin/env python3
import sys
from pathlib import Path

w_path = sys.argv[1]

p = Path(w_path)

current = None
nodes = list()

with p.open(mode="w") as f:
    for line in sys.stdin:
        key, value = map(int, line.strip().split())
        if not current:
            current = key

        if current != key:
            print(f"{current}\t{nodes}")
            f.write(f"{current},1\n")
            current = key
            nodes.clear()

        nodes.append(value)

    print(f"{current}\t{nodes}")
    f.write(f"{current},1\n")
