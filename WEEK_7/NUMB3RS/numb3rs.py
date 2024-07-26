import re
import sys

def main():
    ip = input("IPv4 Address: ")
    ipvalid = validate(ip)
    if not ipvalid:
        sys.exit(1)
    print(ipvalid)


def validate(ip):
    numbers = ip.split(".")
    if len(numbers) != 4:
        return False
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        for number in numbers:
            number = int(number)
            if not 0 <= number <= 255:
                return False
        else :
                return True

if __name__ == "__main__":
    main()
