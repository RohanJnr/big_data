import sys
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("task1").getOrCreate()
df_path, df_out = sys.argv[1:]

df = spark.read.csv(df_path, header=True)

avg_fine_df = df.groupBy("RP State Plate").agg({"Fine amount": "avg"})

df = df.filter(df.Color == "WH")

joined_df = df.join(avg_fine_df, on="RP State Plate", how="left")
joined_df = joined_df.filter(joined_df["Fine amount"] > joined_df["avg(Fine amount)"])
joined_df = joined_df.dropna()
joined_df = joined_df.drop_duplicates()
joined_df = joined_df.sort("Ticket number")

res = joined_df.select("Ticket number")
res.write.csv(df_out)