import csv

total_sales = 0

with open("sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_sales += int(row["amount"])

print("Total sales:", total_sales)