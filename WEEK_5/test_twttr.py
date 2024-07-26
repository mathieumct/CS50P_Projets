from twttr import shorten
import sys

def test_voyelle():
    assert shorten("TWITTER") == "TWTTR"

def test_maj():
    assert shorten("Twitter") == "Twttr"
    assert shorten("twitter") == "twttr"

def test_number():
    result = shorten("Un texte avec un 2")
    assert result == "n txt vc n 2"

def test_ponctuation():
    result = shorten("Un texte avec un point.")
    assert result == "n txt vc n pnt."
