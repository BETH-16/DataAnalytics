# Variables — change to test different scenarios
# ─────────────────────────────────────────────
pay_rate = 17.30
hours_worked = 45
filing_status = "single"  # "single" or "joint"

# ─────────────────────────────────────────────
# Step 2: Calculate weekly gross pay (from pay_rules.py)
# ─────────────────────────────────────────────
if hours_worked > 40:
    regular_pay = pay_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    weekly_gross = regular_pay + overtime_pay
else:
    weekly_gross = pay_rate * hours_worked

# Estimate annual gross pay (52 weeks in a year)
annual_gross = weekly_gross * 52

# ─────────────────────────────────────────────
# Step 3: Determine tax rate based on filing status
#
# Single filers:
#   under $12,000          →  5%
#   $12,000 - $24,999.99   → 10%
#   $25,000 - $74,999.99   → 15%
#   $75,000 and over       → 20%
#
# Joint filers:
#   under $12,000          →  0%
#   $12,000 - $24,999.99   →  6%
#   $25,000 - $74,999.99   → 11%
#   $75,000 and over       → 20%
# ─────────────────────────────────────────────
if filing_status == "single":
    if annual_gross < 12000:
        tax_rate = 0.05
    elif annual_gross < 25000:
        tax_rate = 0.10
    elif annual_gross < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filing_status == "joint":
    if annual_gross < 12000:
        tax_rate = 0.00
    elif annual_gross < 25000:
        tax_rate = 0.06
    elif annual_gross < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

else:
    print("Invalid filing status. Please use 'single' or 'joint'.")
    tax_rate = 0

# ─────────────────────────────────────────────
# Step 4: Calculate weekly tax withholding and net pay
# ─────────────────────────────────────────────
weekly_tax = weekly_gross * tax_rate
net_pay = weekly_gross - weekly_tax

# ─────────────────────────────────────────────
# Step 5: Print results
# ─────────────────────────────────────────────
print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${weekly_gross:.2f}")
print(f"Your estimated annual gross pay is ${annual_gross:.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax rate is {int(tax_rate * 100)}%")
print(f"Your tax withholding for the week is ${weekly_tax:.2f}")
print(f"Your net pay is ${net_pay:.2f}")