# a).

for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b).

for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c).

ask_user = int(input("Number of stars: "))
for i in range(0, ask_user):
    print("*", end='')
print()

# d).
ask_user = int(input("Number of stars: "))
for i in range(0, ask_user):
    for j in range(0, i+1):
        print("*", end='')
    print()


