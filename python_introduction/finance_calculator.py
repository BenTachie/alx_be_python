# This script calculates monthly savings and projects savings after one year with interest

# Prompt the user for monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Annual interest rate
interest_rate = 0.05

# Project savings after one year with simple interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)

# Output results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
