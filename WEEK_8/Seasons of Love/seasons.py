from datetime import date, datetime, timedelta
import sys
import inflect


def main():
    anniversaire = input("Date of Birth: ")
    dob = DateOfBirth(anniversaire)
    ac = AgeCalculator(dob)
    age = dob.get_age()
    total_minutes = ac.calculate_minutes()
    numbconverter_age = NumberToWordsConverter(total_minutes)
    result_converter_age = numbconverter_age.get_converted_number()
    numbconverter_minutes = NumberToWordsConverter(total_minutes)
    result_converter_minutes = numbconverter_minutes.get_converted_number()
    result_final_age = result_converter_age.capitalize().replace(" and ", " ")
    result_final_minutes = result_converter_minutes.capitalize().replace(" and ", " ")
    print(result_final_minutes, "minutes")

class DateOfBirth():
    def __init__(self, anniversaire):
        if not "-" in anniversaire:
            sys.exit("Invalid date")
        else:
            convert_date = datetime.strptime(anniversaire, "%Y-%m-%d").date()
            self.year = convert_date.year
            self.month = convert_date.month
            self.day = convert_date.day
    def get_date(self):
        return date(self.year, self.month, self.day)
    def get_age(self):
        current_date = date.today()
        birth_date = self.get_date()
        age = current_date.year - birth_date.year
        if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
            age -= 1
        return age


class AgeCalculator():
    def __init__(self, dob):
        self.dob = dob

    def calculate_minutes(self):
        current_date = date.today()
        diff = current_date - self.dob.get_date()
        total_minutes = diff.days * 24 * 60

        for year in range(self.dob.year, current_date.year):
            if year %4 == 0:
                if (year % 100 != 0) or (year % 400 == 0):
                    if self.dob.month < 2 or (self.dob.month == 2 and self.dob.day < 29):
                        total_minutes += 1440
        return total_minutes

class NumberToWordsConverter():
    def __init__(self, age):
        p = inflect.engine()
        self.convert_age = p.number_to_words(age)

    def get_converted_number(self):
        return self.convert_age

if __name__ == "__main__":
    main()
