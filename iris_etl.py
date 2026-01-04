import argparse
import requests
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
OUTPUT_TABLE = "default.bundle_demo_iris_species_counts"

def main(target: str) -> None:
    spark = SparkSession.builder.getOrCreate()

    # 1️⃣ Download CSV into memory (no filesystem)
    r = requests.get(DATA_URL, timeout=30)
    r.raise_for_status()

    pdf = pd.read_csv(pd.io.common.BytesIO(r.content))

    # 2️⃣ Convert Pandas → Spark DataFrame
    df = spark.createDataFrame(pdf)

    # 3️⃣ Transform
    out = (
        df.groupBy("species")
          .agg(F.count(F.lit(1)).alias("cnt"))
          .orderBy("species")
    )

    # ⚠️ Destructive overwrite (safe for demo)
    out.write.mode("overwrite").format("delta").saveAsTable(OUTPUT_TABLE)

    # 4️⃣ Log output
    print("Wrote table:", OUTPUT_TABLE)
    out.show(truncate=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", default="dev")
    args = parser.parse_args()
    main(args.target)
