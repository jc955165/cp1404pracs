import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# These results are observed based on 10 observations (running 10 times)

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# Ans. Smallest number: 5 and Largest number: 19

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Ans. Smallest number: 3 and Largest number: 9
# Could line 2 have produced a 4?
# Ans. NO

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# Ans. Smallest number: 2.5031496902577994 and Largest number: 5.435336852325856

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(0, 100))
# randint(a, b) method of random.Random instance, Return random integer in range [a, b], including both end points.
