from seasons import DateOfBirth, AgeCalculator, NumberToWordsConverter
import pytest

def test_good_date():
    dob = DateOfBirth("2023-02-06")
    assert dob.year == 2023
    assert dob.month == 2
    assert dob.day == 6

def test_number_converter():
    converter = NumberToWordsConverter("20")
    assert converter.get_converted_number() == "twenty"

