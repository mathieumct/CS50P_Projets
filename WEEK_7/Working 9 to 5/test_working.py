from working import convert
import pytest

def test_heure1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
def test_heure2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_minute1():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
def test_minute_error():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")
def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")
