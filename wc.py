import os
import findspark
from spark_builder import SparkBuilder
from pyspark.sql.functions import explode, split, col

import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

if __name__ == '__main__':
    spark = SparkBuilder({'spark.app.name': 'Word-count'}).getSession()
    findspark.init()

    df = spark.read.text('input.txt')

    df_count = (
        df.withColumn('word', explode(split(col('value'), ' ')))
            .groupBy('word')
            .count()
            .sort('count', ascending=False)
    )

    df_count.show()

    spark.stop()
