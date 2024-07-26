def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ponctuation = set("!?,.-")
    if s[0:len(s)].isalpha() and 2 <= len(s) <= 6:
        return True
    if s[:2].isalpha() and 2 <= len(s) <= 6:
        for char in s:
            if char.isdigit():
                if char == "0":
                    return False
                break
        if not s[-1].isdigit():
            return False
        found_digit = False
        for char in s:
            if char.isdigit():
                found_digit = True
            elif found_digit and char.isalpha():
                return False
        for char in s:
            if char in ponctuation:
                return False
        else:
            return True

main()
