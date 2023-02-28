TOTAL = 0
ask_user = int(input("Number of items: "))
while ask_user < 0:
    print("invalid number of items!")
    ask_user = int(input("Number of items: "))
for i in range(0, ask_user):
    item = float(input("Price of item: "))
    TOTAL = TOTAL + item
if TOTAL > 100:
    TOTAL = TOTAL - (TOTAL * 0.1)
print(f"Total price for 3 items is ${TOTAL:.2f}")
