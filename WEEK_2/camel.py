def main():
    text = get_text()

def get_text():
        name = (input("camelCase: "))
        match name:
            case "name":
                print("snake_case: name")
            case "firstName":
                print("snake_case: first_name")
            case "preferredFirstName":
                print("snake_case: preferred_first_name")
main()