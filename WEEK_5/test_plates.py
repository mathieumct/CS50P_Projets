from plates import is_valid

def test_twoletters():
    assert is_valid("50") == False

def test_sixchar():
    assert is_valid("OUTATIME") == False

def test_onechar():
    assert is_valid("H") == False

def test_middle():
    assert is_valid("CS50P") == False

def test_middlezero():
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("PI3.14") == False
