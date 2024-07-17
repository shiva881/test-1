import sys  # Import the sys module
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Define your schema
schema = StructType([
    StructField("column1", StringType(), True),
    StructField("column2", IntegerType(), True)
])

# Start the Spark context and initialize GlueContext
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

job.init(args['JOB_NAME'], args)

# Read data from S3 using your defined schema
df = spark.read.format("csv").option("header", "true").schema(schema).load("s3://my-shiva881/data/")

# Example transformation: Filter data
filtered_df = df.filter(df['column1'] == 'value')

# Write transformed data to S3
filtered_df.write.format("parquet").mode("overwrite").save("s3://my-shiva881/output/")

job.commit()
