#!/usr/bin/env python3
import sys
from collections import defaultdict

def reducer():
    
    dates = defaultdict(int)

    for data in sys.stdin:
        data = data.strip()
        timestamp, count = data.rsplit(",", 1)
        count = int(count)
        dates[timestamp] += 1


    for timestamp, date_count in dates.items():
        print(timestamp, date_count)

reducer()
