from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

# Initialize Spark Session
spark = SparkSession.builder.appName("HashtagTrends").getOrCreate()

# Load posts data
posts_df = spark.read.option("header", True).csv("input/posts.csv")

# Split the Hashtags column into individual hashtags, count frequency, and sort descending
hashtag_counts = posts_df.select(explode(split(col("Hashtags"), ",")).alias("hashtag")) \
    .groupBy("hashtag") \
    .count() \
    .orderBy(col("count").desc())

# Save result
hashtag_counts.coalesce(1).write.mode("overwrite").csv("outputs/hashtag_trends.csv", header=True)
