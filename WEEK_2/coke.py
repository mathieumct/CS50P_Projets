amountdue = 50
remaining = amountdue

while True:
    getcoins = int(input(f"Amount Due: {remaining}\nInsert Coins: "))
    if getcoins == 25 or getcoins == 10 or getcoins == 5:
        remaining = remaining - getcoins
        if remaining < 0:
            diff = abs(remaining)
            print(f"Change Owed: {diff}")
            break
        elif remaining == 0:
            print("Change Owed: 0")
            break

