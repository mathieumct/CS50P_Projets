text = (input("Input: "))
voyelle = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

output = ""

for char in text:
    if char in voyelle:
        output = output + ""
    else:
        output = output + char

print("Output:", output)
