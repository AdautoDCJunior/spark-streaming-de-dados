import os
from pyspark.sql import SparkSession
from dotenv import load_dotenv, find_dotenv
import shutil

load_dotenv(find_dotenv())

for item in ['./check', './csv']:
  try:
    shutil.rmtree(item)
  except OSError as err:
    print(f'Aviso: {err.strerror}')

host = os.getenv('HOST')
port = int(os.getenv('PORT'))

spark = SparkSession\
  .builder\
  .appName('SparkStreaming')\
  .getOrCreate()

tweets = spark.readStream\
  .format('socket')\
  .option('host', host)\
  .option('port', port)\
  .load()

query = tweets \
    .writeStream \
    .outputMode("append") \
    .option('encoding', 'utf-8') \
    .format("csv") \
    .option('path', './csv') \
    .option('checkpointLocation', './check') \
    .start()

query.awaitTermination()