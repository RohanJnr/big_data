#!/bin/sh
CONVERGE=1
ITER=1
rm w w1 log*

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /task-* 

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-mapper "/home/pes1ug20me009/dev/big_data/assignment-2/task1/mapper.py" \
-reducer "/home/pes1ug20me009/dev/big_data/assignment-2/task1/reducer.py /home/pes1ug20me009/dev/big_data/assignment-2/task2/w"  \
-input /assignment-2/sample_input.txt \
-output /task-1-output


while [ "$CONVERGE" -ne 0 ]
do
	echo "############################# ITERATION $ITER #############################"
	$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-*streaming*.jar \
	-mapper "/home/pes1ug20me009/dev/big_data/assignment-2/task2/mapper.py /home/pes1ug20me009/dev/big_data/assignment-2/task2/w /home/pes1ug20me009/dev/big_data/assignment-2/task2/data/sample_page_embeddings.json" \
	-reducer "/home/pes1ug20me009/dev/big_data/assignment-2/task2/reducer.py" \
	-input /task-1-output/part-00000 \
	-output /task-2-output
	touch w1
	hadoop dfs -cat /task-2-output/part-00000 > "/home/pes1ug20me009/dev/big_data/assignment-2/task2/w1"
	CONVERGE=$(python3 /home/pes1ug20me009/dev/big_data/assignment-2/task2/check_conv.py $ITER>&1)
	ITER=$((ITER+1))
	hdfs dfs -rm -r /task-2-output/
	echo $CONVERGE
done
