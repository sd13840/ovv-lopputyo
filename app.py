language = input("Valitse kieli (fi/en): ").lower()

if language == "en":
    name = input("What is your name? ")
    print(f"Welcome {name}!")
else:
    name = input("Mikä sinun nimesi on? ")
    print(f"Tervetuloo {name}!")
