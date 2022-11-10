import json
import sys
from kafka import KafkaConsumer
from collections import defaultdict

topic_name = sys.argv[1]


def default_state():
    return {
        "count": 1,
        "Min": 0,
        "Max": 0
    }

states_avg = defaultdict(default_state)

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value

    print(json.dumps(data, indent=2))

    break

    if data["state"] == "EOF":
        break

    # Computing avergae on the fly
    states_avg[data["state"]]["Min"] = states_avg[data["state"]]["Min"] + ((
        float(data["Min"]) - states_avg[data["state"]]["Min"])
        /
        (states_avg[data["state"]]["count"] + 1
    ))

    states_avg[data["state"]]["Max"] = states_avg[data["state"]]["Max"] + ((
        float(data["Max"]) - states_avg[data["state"]]["Max"])
        /
        (states_avg[data["state"]]["count"] + 1
    ))

    states_avg[data["state"]]["count"] += 1


# from kafka import KafkaConsumer
# from json import loads


# consumer = KafkaConsumer(
#     'numtest',
#      bootstrap_servers=['localhost:9092'],
#      auto_offset_reset='earliest',
#      enable_auto_commit=True,
#      group_id='my-group',
#      value_deserializer=lambda x: loads(x.decode('utf-8')))


# for message in consumer:
#     message = message.value
#     print(message)