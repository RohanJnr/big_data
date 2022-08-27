#!/usr/bin/env python3
import json
import math
import sys
from typing import Callable


def task_2_condition(data: dict) -> bool:
    query_distance, latitude, longitude = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    

    data_lat = data["lat"]
    data_lon = data["lon"]

    distance = math.sqrt(
        (latitude-data_lat)**2 + (longitude-data_lon)**2
    )
    if (
        distance <= query_distance and
        48 < data["humidity"] < 54 and
        20 < data["temperature"] < 24 
    ):
        return True
    return False

def mapper(condition_func: Callable) -> None:
    for line in sys.stdin:
        data = json.loads(line)

        if "NaN" in (data["location"], data["sensor_id"], data["pressure"], data["humidity"], data["temperature"]):
            continue

        if (
            condition_func(data)
        ):
            print(f"{data['timestamp']},1")


mapper(task_2_condition)
