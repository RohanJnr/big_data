#!/usr/bin/env python3
import sys

for line in sys.stdin:
    if not line.startswith("#"):
        k, v = map(int, line.strip().split())
        print(k, v)
