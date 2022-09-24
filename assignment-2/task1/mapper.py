import sys

for line in sys.stdin:
    if not line.startswith("#"):
        print(line.strip())