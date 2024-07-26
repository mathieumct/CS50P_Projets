import requests
import sys
import json

try:
    if len(sys.argv) < 2 :
        print("Missing command-line argument")
        sys.exit(1)
    convert = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    rate = response.json()["bpi"]["USD"]["rate_float"]
    total_coast = rate * convert
    print(f"${total_coast:,.4f}")

except requests.RequestException:
    sys.exit(1)
