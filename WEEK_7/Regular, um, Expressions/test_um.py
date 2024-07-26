from um import count
import pytest

def test_chaine_vide():
    assert count(" ") == 0

def test_um_seul():
    assert count("um") == 1

def test_um_plus():
    assert count("um um um") == 3

def test_majuscule():
    assert count("UM um Um") == 3

def test_mot():
    assert count("yummy") == 0
