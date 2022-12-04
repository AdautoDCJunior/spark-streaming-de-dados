import os
from pyspark.sql import SparkSession, functions as f
from dotenv import load_dotenv, find_dotenv
from datetime import datetime

load_dotenv(find_dotenv())

host = os.getenv('HOST')
port = int(os.getenv('PORT'))

spark = SparkSession\
  .builder\
  .appName('SparkStreaming')\
  .getOrCreate()

lines = spark.readStream\
  .format('socket')\
  .option('host', host)\
  .option('port', port)\
  .load()

words = lines.select(f.explode(f.split(lines.value, ' ')).alias('word'))

wordCounts = words.groupBy('word').count()
query = wordCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()