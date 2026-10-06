language = input("Valitse kieli (fi/en): ").lower()

if language == "en":
    name = input("What is your name? ")
    print(f"Welcome {name}!")
    print("Have a nice day!")
else:
    name = input("Mikä sinun nimesi on? ")
    print(f"Tervetuloa {name}!")
    print("Mukavaa päivänjatkoa!")
