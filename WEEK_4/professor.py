import random


def main():
    score = 0
    question = get_level()
    for i in range (10):
        integer_one = generate_integer(question)
        integer_two = generate_integer(question)
        for each_try in range(3):
            try:
                text = int(input(str(integer_one) + " + " + str(integer_two) + " = "))
            except ValueError:
                print("EEE")
                continue
            calcul = (integer_one + integer_two)
            if text == calcul:
                score += 1
                break
            elif text != calcul:
                print("EEE")
                if each_try == 2:
                    print(str(integer_one) + " + " + str(integer_two) + " = " + str( calcul ))
    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            print("EEE")
            continue
        if level != 1 and level != 2 and level != 3:
            continue
        else:
            return level


def generate_integer(level):
    if level == 1:
        number_one = random.randint(0, 9)
        return number_one
    elif level == 2:
        number_two = random.randint(10, 99)
        return number_two
    elif level == 3:
        number_three = random.randint(100, 999)
        return number_three
    else:
        raise ValueError


if __name__ == "__main__":
    main()
