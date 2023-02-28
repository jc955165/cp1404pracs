"""
CP1404- Practical
Pseudocode for temperature conversion

MENU = C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
display MENU
get choice
while choice not equal to Q
    if choice equal to C
        get celsius
        fahrenheit = celsius * 9.0 / 5 + 32
        display result
    else if choice == "F":
        get fahrenheit
        celsius = 5 / 9 * (fahrenheit - 32)
        display result
    else:
        display invalid option
    display menu
    get choice
print("Thank you.")

"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} F")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
