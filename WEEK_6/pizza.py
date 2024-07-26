import sys
import os
import csv
from tabulate import tabulate

if not len(sys.argv) == 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) == 3:
    sys.exit("Too many commad-line arguments")
pizza = sys.argv[1]
if not pizza.endswith(".csv"):
    sys.exit("Not a CSV file")
if not os.path.isfile(pizza):
    sys.exit("File does not exist")

with open(pizza) as file:
    choix = csv.reader(file)
    print(tabulate(choix, headers="firstrow", tablefmt="grid"))
