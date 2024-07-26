def main():
    text = input("Entre ton texte ici : ")
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    print(text)

main()