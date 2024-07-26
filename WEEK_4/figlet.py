import sys
import random


from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage")
if len(sys.argv) == 3:
    text = sys.argv[2]
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    else:
        f = sys.argv[2]
        if f not in figlet.getFonts():
            sys.exit("Invalid usage")
        text = input("Input: ")
        figlet.setFont(font=f)

if len(sys.argv) == 1:
    text = input("Input: ")
    fonts = figlet.getFonts()
    random_font = random.choice(fonts)
    figlet.setFont(font=random_font)
print(figlet.renderText(text))
