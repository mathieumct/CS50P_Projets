import sys
import os

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments")
text = sys.argv[1]
if not text.endswith(".py"):
    sys.exit("Not a Python file")
if not os.path.isfile(text):
    sys.exit("File does not exist")
with open(text) as file:
   lines = file.readlines()
   count = 0
   for line in lines:
        line = line.strip()
        if not line.startswith("#") and not line == "":
            count += 1
print(count)

