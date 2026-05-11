# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

# ─────────────────────────────────────────────
# Step 2: Define variables
# ─────────────────────────────────────────────
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# ─────────────────────────────────────────────
# Step 4: Print each variable and its type
# ─────────────────────────────────────────────
print("=== Original Variables ===")
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# ─────────────────────────────────────────────
# Step 5a: Cast as integer using int()
# ─────────────────────────────────────────────
print("\n=== Cast as int() ===")

# a = " 101.1 " → cannot cast directly, has decimal and spaces → ValueError
# int(a)  # ValueError: invalid literal for int() with base 10

# b = '55' → works fine, clean numeric string
b_int = int(b)
print(b_int, type(b_int))

# c = "402 Stevens" → cannot cast, has letters → ValueError
# int(c)  # ValueError: invalid literal for int() with base 10

# d = 'Number 5 ' → cannot cast, has letters → ValueError
# int(d)  # ValueError: invalid literal for int() with base 10

# ─────────────────────────────────────────────
# Step 5b: Cast as float using float()
# ─────────────────────────────────────────────
print("\n=== Cast as float() ===")

# a = " 101.1 " → works! float() handles leading/trailing spaces
a_float = float(a)
print(a_float, type(a_float))

# b = '55' → works fine
b_float = float(b)
print(b_float, type(b_float))

# c = "402 Stevens" → cannot cast, has letters → ValueError
# float(c)  # ValueError: could not convert string to float

# d = 'Number 5 ' → cannot cast, has letters → ValueError
# float(d)  # ValueError: could not convert string to float

# ─────────────────────────────────────────────
# Step 5c: For variable a, cast float then int
# ─────────────────────────────────────────────
print("\n=== int(float(a)) ===")

# First converts " 101.1 " to 101.1 (float handles spaces),
# then truncates decimal → 101
a_float_then_int = int(float(a))
print(a_float_then_int, type(a_float_then_int))

# ─────────────────────────────────────────────
# Step 5d: Slicing to extract numeric portion
# ─────────────────────────────────────────────
print("\n=== Slicing ===")

# a = " 101.1 " → numeric portion is at index 1:6 → "101.1", cast as float
a_sliced = float(a[1:6])
print(a_sliced, type(a_sliced))

# b = '55' → entire string is numeric, cast as int
b_sliced = int(b[0:2])
print(b_sliced, type(b_sliced))

# c = "402 Stevens" → numeric portion is at index 0:3 → "402", cast as int
c_sliced = int(c[0:3])
print(c_sliced, type(c_sliced))

# d = 'Number 5 ' → numeric portion is at index 7 → "5", cast as int
d_sliced = int(d[7])
print(d_sliced, type(d_sliced))

# ─────────────────────────────────────────────
# Step 5e: Use .strip() to remove leading/trailing spaces
# ─────────────────────────────────────────────
print("\n=== .strip() ===")

# a = " 101.1 " → strip removes spaces on both sides
print(a.strip())

# d = 'Number 5 ' → strip removes trailing space
print(d.strip())