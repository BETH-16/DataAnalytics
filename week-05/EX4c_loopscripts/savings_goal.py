# Description: This script uses a while loop to simulate saving toward a goal
# Step 2: Starting variables
# ─────────────────────────────────────────────
balance = 200.00
savings_goal = 1000.00
weekly_savings = 75.00

treat_cost = 10.00  # cost of a little treat at 75% milestone

# ─────────────────────────────────────────────
# Step 3 & 4: While loop with milestone messages
# ─────────────────────────────────────────────
while balance < savings_goal:
    balance += weekly_savings

    halfway = savings_goal * 0.50
    almost = savings_goal * 0.75

    # Step 4b: 75% or more — buy a treat
    if balance >= almost:
        balance -= treat_cost
        print(f"So close! After treating myself, my balance is up to ${balance:.2f}")

    # Step 4a: more than halfway but under 75%
    elif balance >= halfway:
        print(f"Almost there! This week my balance is up to ${balance:.2f}")

    # Step 3: under halfway
    else:
        print(f"This week my balance increased to ${balance:.2f}")

# ─────────────────────────────────────────────
# Goal reached
# ─────────────────────────────────────────────
print (f"Goal met! My current balance is ${balance:.2f}")