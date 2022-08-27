#!/usr/bin/env python3
import json
import sys
from typing import Callable


def task_1_condition(data: dict) -> None:
    if (
        1700 < data["location"] < 2500 and
        data["sensor_id"] < 5000 and
        data["pressure"] >= 93500 and
        data["humidity"] >= 72 and
        data["temperature"] >= 12
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


mapper(task_1_condition)
