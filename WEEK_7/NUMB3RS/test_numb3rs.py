from numb3rs import validate

def test_letters():
    assert validate("cat") == False

def test_point():
    assert validate("255255255255") == False

def test_numbers():
    assert validate("1.2.3.1000") == False

def test_valid():
    assert validate("255.255.255.0") == True

def test_invalid_first():
    assert validate("256.255.255.255") == False

def test_invalid_second():
    assert validate("255.256.255.255") == False

def test_invalid_third():
    assert validate("255.255.256.255") == False

def test_invalid_fourth():
    assert validate("255.255.255.256") == False
