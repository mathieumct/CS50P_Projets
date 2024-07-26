import re

def main():
    text = (input("Text: ")).strip()
    def_count = count(text)
    print(def_count)

def count(text):
    matches = re.findall(r"\bum\b", text, re.IGNORECASE)
    liste_longueur = len(matches)
    return liste_longueur

if __name__ == "__main__":
    main()
