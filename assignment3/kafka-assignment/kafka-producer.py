import json
import sys
from time import sleep
from kafka import KafkaProducer
import time
from collections import OrderedDict


topic_name = sys.argv[1]
print(topic_name)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# for line in sys.stdin:
#     try:
#         state, *_, min_price, max_price, _ = line.split(",")
#     except ValueError:
#         if line.strip() == "EOF":
#             producer.send(topic_name, {
#                 "state": "EOF"
#             })
#     data = {
#         "state": state,
#         "Min": min_price,
#         "Max": max_price
#     }
#     result = producer.send(topic_name, value=data)
#     result.get()
#     print("Sent")

                        
data = {}
for line in sys.stdin:
	if line.strip()=='EOF':
		break
	temp = line.split(',')
	
	st,min,max = (temp[0],temp[-3],temp[-2])
	if st in data:
		data[st]['Min'].append(float(min))
		data[st]['Max'].append(float(max)) 
	else:
		data[st] = {'Min':list(),'Max':list()}
		data[st]['Min'].append(float(min))
		data[st]['Max'].append(float(max))
		
for i in data.keys():
	data[i]['Min'] = round(sum(data[i]['Min'])/len(data[i]['Min']), 2)
	data[i]['Max'] = round(sum(data[i]['Max'])/len(data[i]['Max']), 2)
        
result = dict(OrderedDict(sorted(data.items())))
print(result)

r = producer.send(topic_name, result)
r.get()