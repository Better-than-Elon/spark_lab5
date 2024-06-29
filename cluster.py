import os
import findspark
from spark_builder import SparkBuilder
from data_processing import DataProcessing
from pyspark.sql.functions import explode, split, col

import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

if __name__ == '__main__':
    spark = SparkBuilder({'spark.app.name': 'Clustering'}).getSession()

    processing = DataProcessing(spark)

    dataset = processing.load()
    vec_dataset = processing.vectorize(dataset)
    scaled_dataset = processing.scale(vec_dataset)
    score = processing.cluster(scaled_dataset)

    spark.stop()