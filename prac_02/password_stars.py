"""
CP1404 - Practical 02 - Functions, Git Version Control
Student Name: Arshdeep Kaur
Get a password with minimum length and display asterisks
"""

MINIMUM_LENGTH = 6


def main():
    """Get and print password using functions."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password of valid size, that meets the minimum_length requirement."""
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Invalid Password! Please enter again")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password


def print_asterisks(sequence):
    """Print as many asterisks as long as the word."""
    print('*' * len(sequence))


main()
