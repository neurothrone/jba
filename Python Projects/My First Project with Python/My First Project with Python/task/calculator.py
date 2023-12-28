total_earned_dict = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80,
}

print("Earned amount:")
for item, amount in total_earned_dict.items():
    print(f"{item}: ${amount}")

total_sum = sum(total_earned_dict.values())
print(f"\nIncome: ${total_sum}")

staff_expenses = int(input("Staff expenses:\n"))
other_expenses = int(input("Other expenses:\n"))
net_income = total_sum - (staff_expenses + other_expenses)

print(f"Net income: ${net_income}")
