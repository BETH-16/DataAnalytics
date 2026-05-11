# taxes.py

# Ask user for monthly salary
salary = float(input("Enter your monthly salary: "))

# Calculate federal taxes (23%)
taxes = salary * 0.23

# Display results (no partial cents)
print(f"Federal taxes withheld: ${taxes:.2f}")