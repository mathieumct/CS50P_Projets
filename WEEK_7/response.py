import validators

email_address = input("What's your email address? ")
if validators.email(email_address):
    print("Valid")
else:
    print("Invalid")
