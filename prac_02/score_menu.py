"""
CP1404 - Practical 02 - Functions, Git Version Control
Student Name: Arshdeep Kaur
"""
MAX_SCORE = 100
MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""


def main():
    score = MAX_SCORE
    print(MENU)
    choice = input("Enter your choice:  ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Enter score: ", 0, 100)
        elif choice == "P":
            grades = determine_status(score)
            print(f"Your score ({score}/100) is {grades}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input("Enter your choice:  ").upper()
    print("Farewell")


def get_valid_score(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def determine_status(score):
    """Determine the status of a given score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print stars according to your score."""
    if score >= 90:
        stars = 5
    elif score >= 50:
        stars = 3
    else:
        stars = 1
    print('*' * stars)


main()
