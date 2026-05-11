import math

# Given number of tourists
tourists = 38

# Each van holds 15 passengers
vans_needed = math.ceil(tourists / 15)

# Cost per van per day
van_cost = 250

# Total cost for all vans
total_cost = vans_needed * van_cost

# Cost per person
cost_per_person = total_cost / tourists

# Display results
print(f"Tourists: {tourists}")
print(f"Vans needed: {vans_needed}")
print(f"Total van cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")