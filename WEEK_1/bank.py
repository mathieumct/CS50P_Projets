message = (input("Greeting : "))

if message.strip().lower().startswith("hello"):
    print("$0")
elif message != ("hello") and message.strip().lower().startswith("h"):
    print("$20")
else:
    print("$100")