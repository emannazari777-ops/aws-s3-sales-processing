import boto3
import csv
from io import StringIO

# Connect to S3
s3 = boto3.client("s3")

# S3 bucket and file
bucket_name = "building-things-data-2026"
file_key = "raw/sales.csv"

# Read the file from S3
response = s3.get_object(
    Bucket=bucket_name,
    Key=file_key
)

content = response["Body"].read().decode("utf-8")

# Read CSV data
reader = csv.DictReader(StringIO(content))

# Calculate total sales
total_sales = 0

for row in reader:
    total_sales += int(row["amount"])

print("Total sales:", total_sales)

# Create a processed file locally
with open("sales_summary.csv", "w", encoding="utf-8") as file:
    file.write(f"total_sales,{total_sales}\n")