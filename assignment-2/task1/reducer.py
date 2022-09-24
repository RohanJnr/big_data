import sys
from pathlib import Path

from collections import defaultdict

w_path = sys.argv[1]

p = Path(w_path)

current = None
nodes = set()

with p.open(mode="w") as f:
    for line in sys.stdin:
        key, value = line.strip().split()

        if not current:
            current = key

        if current != key:
            print(f"{current}\t{list(nodes)}")
            f.write(f"{current},1\n")
            current = key
            nodes.clear()

        nodes.add(value)

    print(f"{current}\t{list(nodes)}")
    f.write(f"{current},1\n")

