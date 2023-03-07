"""
CP1404 - Practical
Answer the following questions:
1. When will a ValueError occur?
Ans. When you assign the wrong value to an object, you will get a ValueError.
2. When will a ZeroDivisionError occur?
Ans. ZeroDivisionError occurs when attempting to divide a number by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
