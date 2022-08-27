hadoop jar /home/pes1ug20me009/hadoop-3.3.3/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar \
-mapper "$PWD/mapper.py" \
-reducer "$PWD/reducer.py" \
-input /assignment-1/Air_Quality_2017.json \
-output /assignment-1/output_task1_2017
