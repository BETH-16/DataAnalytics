# Description: This script practices string cleaning techniques
# including case conversion, character replacement, and type casting
# Step 2: Define messy contact records
# ─────────────────────────────────────────────
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

# ─────────────────────────────────────────────
# Step 3: Convert all names to lowercase
# ─────────────────────────────────────────────
print("=== Lowercase ===")
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# ─────────────────────────────────────────────
# Step 4: Convert all names to title case
# ─────────────────────────────────────────────
print("\n=== Title Case ===")
print(name_1.title())
print(name_2.title())
print(name_3.title())

# ─────────────────────────────────────────────
# Step 5: Remove $ from salary strings using .replace()
# ─────────────────────────────────────────────
print("\n=== Remove $ from Salaries ===")
salary_1_clean = salary_1.replace("$", "")
salary_2_clean = salary_2.replace("$", "")

print(salary_1_clean)
print(salary_2_clean)

# Check data type — still a string even after removing $
print(type(salary_1_clean))  # <class 'str'>
print(type(salary_2_clean))  # <class 'str'>

# To perform math, we would also need to remove the comma
# and then cast to int() or float()

# ─────────────────────────────────────────────
# Step 6: Chain .replace() calls and int() in one line
# ─────────────────────────────────────────────
print("\n=== salary_1 as Integer ===")
salary_1_int = int(salary_1.replace("$", "").replace(",", ""))
print(salary_1_int)
print(type(salary_1_int))  # <class 'int'>