import sys
import os
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
nom = sys.argv[1]
if not nom.endswith(".csv"):
    print("Not a CSV file")
    sys.exit
if not os.path.isfile(nom):
    sys.exit("Could not read invalid_file.csv")

with open(nom, "r") as file:
    reader = csv.DictReader(file)
    writer = None
    with open(sys.argv[2], "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
    csvfile = open(sys.argv[2], "a")
    for row in reader:
        try:
            writer = csv.DictWriter(csvfile, fieldnames=["first", "last", "house"])
            name = row["name"].replace('"', '')
            last, first = name.split(",")
            first = first.strip()
            last = last.strip()
            writer.writerow({"first": first, "last": last, "house": row["house"]})
        except ValueError:
            print(f"Error processing line: {row}")
            sys.exit()

csvfile.close()

