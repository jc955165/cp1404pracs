"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        calculate_bonus = (sales * 10)/100
        print(f"You get a bonus of 10%: {calculate_bonus:.2f}")
    else:
        calculate_bonus = (sales * 15) / 100
        print(f"You get a bonus of 15%: {calculate_bonus:.2f}")
    sales = float(input("Enter sales: $"))
print("thank you")
