from pyspark.sql.types import DoubleType, StringType, LongType, StructType, StructField
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("YourAppName").getOrCreate()

# Define variables used in the code below
file_path = "/databricks-datasets/baskin_robbins/"
table_name = "baskin_robbins"
checkpoint_path = "/tmp/pipeline_get_started/_checkpoint/baskin_robbins"

schema = StructType(
  [
    StructField("Flavour", StringType(), True),
    StructField("Calories", LongType(), True),
    StructField("Total_Fat_g", DoubleType(), True),  # Renamed column
    StructField("Trans_Fat_g", DoubleType(), True),  # Renamed column
    StructField("Carbohydrates_g", LongType(), True),  # Renamed column
    StructField("Sugars_g", LongType(), True),  # Renamed column
    StructField("Protein_g", DoubleType(), True)  # Renamed column
  ]
)

(spark.readStream
  .format("cloudFiles")
  .schema(schema)
  .option("cloudFiles.format", "csv")
  .option("sep","\t")
  .load(file_path)
  .writeStream
  .option("checkpointLocation", checkpoint_path)
  .trigger(availableNow=True)
  .toTable(table_name)
)
