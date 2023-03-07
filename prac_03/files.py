"""
CP1404 - Practical 3
Quick file opening/writing/reading exercises
"""

# Program 1 - Write code that asks the user for their name, then opens a file called "name.txt" and writes that
# name to it. Remember to close your file.
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# Program 2 - (In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the
# name (as above) then prints, "Your name is Bob" (or whatever the name is in the file).
with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print("Your name is", name)

# Program 3 - Write code that opens "numbers.txt", reads only the first two numbers and adds them together then
# prints the result, which should be... 59.
in_file = open("numbers.txt", "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(first_number + second_number)

# Program 4 - Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any
# number of numbers.
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(f"Total of all numbers in file is {total}")
