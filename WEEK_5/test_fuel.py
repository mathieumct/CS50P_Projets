from fuel import convert, gauge
import pytest

def test_zero():
    assert gauge(0) == "E"

def test_convert():
    assert convert("3/4") == 75

def test_vide():
    assert gauge(99) == "F"

def test_errorzero():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_digit():
    with pytest.raises(ValueError):
        convert("three/four")

def test_onepercent():
    assert gauge(1) == "E"

def test_pourcentage():
    result = gauge(50)
    assert "%" in result
