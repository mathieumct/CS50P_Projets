import random

while True:
    level = input("Level: ")
    if level.isdigit():
        level = int(level)
        if level >= 1:
            random_number = random.randint(1, level)
            break

while True:
    guess = input("Guess: ")
    if guess.isdigit():
        guess = int(guess)
        if guess >= 1:
            if guess > random_number:
                print("Too large!")
            elif guess < random_number:
                print("Too small!")
            elif guess == random_number:
                print("Just right!")
                break

