from project import mma_brief, brief_resume, categorie_poids, different_arts, glossaire_mma
from pyfiglet import Figlet

def test_mma_brief():
    expected_output = "\n1 -- Un bref résumé\n2 -- Vue d'ensemble des disciplines martiales du MMA\n3 -- Quitter\n"
    assert mma_brief() == expected_output

def test_brief_resume():
    expected_paragraph =  ["MMA (Mixed Martial Arts)",
                           "Le MMA est un sport de combat complet qui combine différentes formes d’arts martiaux",
                           "Les combattants de MMA sont en mesure d’utiliser un large éventail de compétences pour s’adapter à différentes situations de combats.",
                           "Il est important de souligner que ce sport est régi par des règles strictes afin d’assurer la sécurité des combattants."
                           ]
    assert brief_resume() == expected_paragraph

def test_categorie_poids():
    f = Figlet(font="standard")
    expected_output = f.renderText("POIDS")
    assert categorie_poids() == expected_output

def test_different_arts():
    output = different_arts()
    assert "Karaté" in output
    assert "Boxe anglaise" in output
    assert "Boxe pieds-poings" in output
    assert "🥊 " in output

def test_glossaire_mma():
    result, cles_liste = glossaire_mma('a', [])
    expected_result = [(1, "Achille hold", "Compression du tendon d'Achille"),
                       (2, "Americana", "Clef de bras fléchi en étant au dessus de son adversaire"),
                       (3, "Ankle lock", "Clef de cheville en hypertension"),
                       (4, "Armlock", "Clef de bras")]
    assert result == expected_result

