groceries = []
while True:
    try:
        grocery = input("").upper()
        groceries.append(grocery)
    except EOFError:
        break
groceries.sort()

word_count = {}
for word in groceries:
    if word not in word_count:
        word_count[word] = 1
    elif word in word_count:
        word_count[word] += 1
for word, count in word_count.items():
    print(count, word)
