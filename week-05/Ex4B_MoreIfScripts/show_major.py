# Variables — change to test different students
# ─────────────────────────────────────────────
student_name = "Jordan Rivera"
student_major = "CSCI"

# ─────────────────────────────────────────────
# Lookup logic using match/case
# ─────────────────────────────────────────────
match student_major:
    case "BIOL":
        major_name = "Biology"
        office = "Science Bldg, Room 310"
    case "CSCI":
        major_name = "Computer Science"
        office = "Sheppard Hall, Room 314"
    case "ENG":
        major_name = "English"
        office = "Kerr Hall, Room 201"
    case "HIST":
        major_name = "History"
        office = "Kerr Hall, Room 114"
    case "MKT":
        major_name = "Marketing"
        office = "Westly Hall, Room 310"
    case _:
        major_name = "<unknown>"
        office = ""

# ─────────────────────────────────────────────
# Print results
# ─────────────────────────────────────────────
print(f"Student Name:  {student_name}")
print(f"Major Code:    {student_major}")
print(f"Major Name:    {major_name}")

if office:
    print(f"Dept. Office:  {office}")