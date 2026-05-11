# Example values
savings = 1000
interest_rate = 6  # percent

# Rule of 72 calculation
years = 72 / interest_rate

# Doubled savings
doubled_savings = savings * 2

# Convert interest rate to decimal for percentage formatting
interest_rate_decimal = interest_rate / 100

# Output
print(f"Your current savings is {savings}.")
print(f"At a {format(interest_rate_decimal, '.0%')} interest rate, your savings account will be")
print(f"worth {format(doubled_savings, '.2f')} in {format(years, '.1f')} years")
# Your current savings is 1000.
# At a 6% interest rate, your savings account will be
# worth 2000.00 in 12.0 years