# Variables — change to test different combinations
# ─────────────────────────────────────────────
a = 42
b = 17
c = 85

# ─────────────────────────────────────────────
# Find the smallest number
# ─────────────────────────────────────────────
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# ─────────────────────────────────────────────
# Find the largest number
# ─────────────────────────────────────────────
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# ─────────────────────────────────────────────
# Print results
# ─────────────────────────────────────────────
print(f"The three numbers are: {a}, {b}, {c}")
print(f"The smallest number is: {smallest}")
print(f"The largest number is: {largest}")