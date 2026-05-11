# Department code variable — change to test
# ─────────────────────────────────────────────
dept_code = 18

# ─────────────────────────────────────────────
# if/elif/else to determine department name
# ─────────────────────────────────────────────
if dept_code == 1:
    dept_name = "Marketing"
elif dept_code == 5:
    dept_name = "Human Resources"
elif dept_code == 10:
    dept_name = "Accounting"
elif dept_code == 12:
    dept_name = "Legal"
elif dept_code == 18:
    dept_name = "IT"
elif dept_code == 20:
    dept_name = "Customer Relations"
else:
    dept_name = "Unknown Department"

print(f"Department code {dept_code} = {dept_name}")

# Department code variable — change to test
# ─────────────────────────────────────────────
dept_code = 18

# ─────────────────────────────────────────────
# match/case to determine department name
# ─────────────────────────────────────────────
match dept_code:
    case 1:
        dept_name = "Marketing"
    case 5:
        dept_name = "Human Resources"
    case 10:
        dept_name = "Accounting"
    case 12:
        dept_name = "Legal"
    case 18:
        dept_name = "IT"
    case 20:
        dept_name = "Customer Relations"
    case _:
        dept_name = "Unknown Department"

print(f"Department code {dept_code} = {dept_name}")