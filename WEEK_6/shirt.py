import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
extension1 = os.path.splitext(sys.argv[1])[1].lower()
extension2 = os.path.splitext(sys.argv[2])[1].lower()
if extension1 not in [".jpg", ".jpeg", ".png"] or extension2 not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid output")
if extension1 != extension2:
    sys.exit("Input and output have different extensions")

for arg in sys.argv[1:]:
    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as e:
            newphoto = ImageOps.fit(e, size=shirt.size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
            mask = shirt.split()[3]
            newphoto.paste(shirt, (0, 0), mask)
            filename, _ = os.path.splitext(sys.argv[1])
            output_filename = filename + "_out.jpg"
            newphoto.save(output_filename)
    except FileNotFoundError:
        sys.exit("Input does not exist")
