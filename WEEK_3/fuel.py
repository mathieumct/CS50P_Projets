while True:
    try:
        x = input("Fraction: ")
        z, y = map(int, x.split("/"))
        if y == 0:
                continue
        if z > y:
                continue
        break
    except ValueError:
        pass

result = (z / y)
convert = result * 100

if convert > 1 and convert < 99:
    print(f"{round(convert)}", end="%\n")

if convert <= 1:
    print("E")
elif convert >= 99:
    print("F")
