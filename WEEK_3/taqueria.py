sum = 0
item = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

while True :
     try:
        commande = input("Item: ")
        if commande.lower() in item:
            price = item[commande.lower()]
            sum = sum + price
            print(f"${sum:.2f}")

     except EOFError:
        print(end="\n")
        break
