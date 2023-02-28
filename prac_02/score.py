"""
CP1404 - Practical 02 - Functions, Git Version Control
Student Name: Arshdeep Kaur
Fixed program to determine score status, with function
"""
import random


def main():
    """Get a numeric score and display its status."""
    # Part 1
    score = get_valid_score("Enter score: ", 0, 100)
    print(determine_status(score))

    # Part 2
    number_of_students = int(input("Number of students: "))
    for i in range(number_of_students):
        score = random.randint(0, 100)
        print(f"Your score ({score}/100) is {determine_status(score)}")


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


main()
