import inflect
p = inflect.engine()

adieu = []

while True:
    try:
        name = input("Name: ")
        adieu.append(name)
    except EOFError:
        break

if len(adieu) >= 1:
        adieu = p.join(adieu)
        print("\nAdieu, adieu, to", adieu)
