from pyfiglet import Figlet

def main():
    # Main menu and function printout management

    print("\n1 -- Le MMA en bref")
    print("2 -- Connaître ma catégorie de poids")
    print("3 -- Glossaire technique")
    print("4 -- Quitter\n")
    while True:
        try:
            choix_menu_1 = int(input("MENU -- Entre ton choix: "))

            # Print management for the main_brief function
            if choix_menu_1 == 1:
                f = Figlet(font="standard")
                print(f.renderText("MIXED  MARTIAL ARTS"))
                print(mma_brief())
                choix_menu_2 = int(input("Entre ton choix: "))
                # Print management for the brief_resume function
                if choix_menu_2 == 1:
                    for phrase in brief_resume():
                        print(phrase)
                    break
                # Print management for the different_arts function
                elif choix_menu_2 == 2:
                    print(different_arts())
                    break
                elif choix_menu_2 == 3:
                    break
                else:
                    print("Un nombre est nécessaire")

            # Print management for the categorie_poids function
            elif choix_menu_1 == 2:
                print(categorie_poids())
                poids = int(input("Entre ton poids ici: "))
                if poids < 0:
                    print("Le poids ne peut pas être négatif.")
                    break
                if poids <= 58:
                    print("Poids mouche")
                elif poids <= 61:
                    print("Poids coq")
                elif poids <= 66:
                    print("Poids plume")
                elif poids <= 70:
                    print("Poids leger")
                elif poids <= 77:
                    print("Poids welter")
                elif poids <= 84:
                    print("Poids moyen")
                elif poids <= 93:
                    print("Poids mi-lourd")
                elif poids <= 120:
                    print("Poids lourd")
                else:
                    print("Poids super-lourd")
                    break

            # Print management for the glossaire_mma function
            elif choix_menu_1 == 3:
                favoris = []

                while True:
                    if choix_menu_1 == 3:
                        lettre = input("Entrez une lettre pour rechercher des termes: ").lower()
                        result, cles_liste = glossaire_mma(lettre, favoris)
                        found = False
                        for index, cles, definition in result:
                            print(f"{index} -- {cles}: {definition}")
                            found = True
                    if not found:
                        print("Ce mot ne se trouve pas encore dans notre glossaire")
                        continue

                    question_favoris = int(input("\nQuel terme associer à ta liste de favoris? "))
                    question_favoris -= 1
                    if 0 <= question_favoris < len(cles_liste):
                        favoris.append(cles_liste[question_favoris])
                    print("\nPour quitter le programme, effectuez un Ctrl+D\n")
                    print("1 -- Imprimer")
                    print("2 -- Ne pas imprimer")
                    imprimer_liste = int(input("\nVoulez-vous imprimer votre liste de favoris? "))
                    if imprimer_liste == 1:
                        print(favoris)
                        break
            elif choix_menu_1 == 4:
                break
            else:
                print("Choix invalide")
        except ValueError:
            print("Un nombre est demandé")

def mma_brief():
    # Menu with 3 user options
    sortie = "\n1 -- Un bref résumé"
    sortie += "\n2 -- Vue d'ensemble des disciplines martiales du MMA"
    sortie += "\n3 -- Quitter\n"
    return sortie


def brief_resume():
    # First option of the mma_brief function. A quick summary of the MMA
    paragraphe_brief = []
    paragraphe_brief.append("MMA (Mixed Martial Arts)")
    paragraphe_brief.append("Le MMA est un sport de combat complet qui combine différentes formes d’arts martiaux")
    paragraphe_brief.append("Les combattants de MMA sont en mesure d’utiliser un large éventail de compétences pour s’adapter à différentes situations de combats.")
    paragraphe_brief.append("Il est important de souligner que ce sport est régi par des règles strictes afin d’assurer la sécurité des combattants.")
    return paragraphe_brief

def different_arts():
    # Second option of the mma_brief function. A list of the different martial arts used in MMA
    titles = ["Frappe", "Lutte au corps à corps & projection", "Lutte au sol & soumission"]
    sublists = [
        ["Karaté", "Boxe anglaise", "Boxe pieds-poings\n"],
        ["Boxe thaïlandaise", "Judo", "Jiu-jitsu", "Lutte libre", "Lutte gréco-romaine", "sambo\n"],
        ["Judo", "Sambo", "Jiu-jitsu brésilien", "Grappling\n"]
    ]

    f = Figlet(font="standard")
    sortie_different_arts = ""
    for i, title in enumerate(titles):
        sortie_different_arts += f.renderText(title)
        for element in sublists[i]:
            sortie_different_arts +="\n" + "🥊 " + element + "\n"
    return sortie_different_arts

def categorie_poids():
    # Enables users to enter their weight and find out their weight category.
    f = Figlet(font="standard")
    sortie_categorie = f.renderText("POIDS")

    return sortie_categorie

def glossaire_mma(lettre, favoris):
    # A glossary allowing the user to search for a specific MMA term by simply entering the first letter of the word.
    # With the option of saving these words in a list of favorites that can be printed out later.
    f = Figlet(font="standard")
    print(f.renderText("GLOSSAIRE"))

    glossaire = {
        "Achille hold": "Compression du tendon d'Achille",
        "Americana": "Clef de bras fléchi en étant au dessus de son adversaire",
        "Ankle lock": "Clef de cheville en hypertension",
        "Armlock": "Clef de bras",
        "Back control": "Contrôle du dos, l'adversaire pris entre les jambes",
        "Choke": "Etranglement",
        "Clinch": "Phase de combat debout, avec saisie sur le haut du corps en envoyant coups de genoux ou coups de coudes",
        "Double leg takedown": "Amenée au sol par ramassement des deux jambes",
        "Grappling": "Discipline de lutte qui autorise toutes les techniques de préhension",
        "Ground-and-pound": "Phase de combat au sol dans laquelle l'un des combattants, en position supérieure, essaye de frapper son adversaire",
        "Half Guard": "Demi-garde, quand une jambe du combattant au-dessus est prise entre les deux jambes du combattant du dessous",
        "Heelhook": "Clef de talon",
        "Jab": "Direct du bras avant",
        "Kimura": "Technique de clef d'épaule avec torsion du bras dans le dos de l'adversaire",
        "Kneebar": "Clef en hyperextension du genou",
        "Leglock": "Clef de jambe",
        "Mount position": "Position montée, à cheval sur l'adversaire",
        "Omoplata": "Clef d'épaule effectuée avec les jambes",
        "Single leg": "Amenée au sol en saisissant une seule jambe",
        "Shoulder lock": "Clef d'épaule",
        "Sprawl": "Technique de défense en combat debout pour éviter une tentative de ramassement de jambes",
        "Takedown": "Projection ou amenée au sol par différentes techniques",
        "Toe hold": "Clef de cheville avec maintien des orteils",
        "Wristlock": "Clef de poignet",
    }

    result = []
    cles_liste = list(glossaire.keys())

    for index, cles in enumerate(glossaire.keys(), 1):
        if cles.lower().startswith(lettre):
            result.append((index, cles, glossaire[cles]))
    return result, cles_liste

if __name__ == "__main__":
    main()
