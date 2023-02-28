"""
CP1404 - Practical 02 - Functions, Git Version Control
Student Name: Arshdeep Kaur
Temperature conversions
"""

MENU = """F - Convert Fahrenheit to Celsius
C - Convert Celsius to Fahrenheit
Q - Quit"""


def main():
    """Temperature conversion program."""
    print(MENU)
    choice = input("Enter operation to perform:  ").lower()
    while choice != "q":
        if choice == "f":
            fahrenheit = float(input("Enter temperature in Fahrenheit : "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Temperature: {celsius:.2f} C")
        elif choice == "c":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Temperature: {fahrenheit:.2f} F")
        else:
            print("Invalid option")
        print(MENU)
        choice = input("Enter operation to perform:  ").lower()


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


main()
