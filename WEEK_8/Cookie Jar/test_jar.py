from jar import Jar
import pytest

def test_init():
    jar = Jar(5)
    assert jar.capacity == 5


def test_str():
    jar = Jar(5)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.number_in_jar == 3
    with pytest.raises(ValueError):
        jar.deposit(3)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.number_in_jar == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)
