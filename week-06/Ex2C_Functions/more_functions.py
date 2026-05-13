
# Description: This script practices defining and calling custom functions


def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state} {zip}")

def add_numbers(*args):
    result = sum(args)
    equation = " + ".join(str(n) for n in args)
    print(f"{equation} = {result}")

def display_receipt(total_due, amount_paid):
    print(f"Total Due:    ${total_due:.2f}")
    print(f"Amount Paid:  ${amount_paid:.2f}")
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due:   ${change:.2f}")
    else:
        balance = total_due - amount_paid
        print(f"Remaining balance to be paid: ${balance:.2f}")

#  Call display_mailing_label twice

print("=== Mailing Labels ===")
display_mailing_label('Betty Smith', '123 Maple Street', 'Atlanta', 'GA', '30301')
print()
display_mailing_label('Jordan Rivera', '456 Oak Avenue', 'Miami', 'FL', '33101')

# calling add_numbers

print("\n=== Add Numbers ===")
add_numbers(5)
add_numbers(10, 20)
add_numbers(3, 7, 12, 8, 5)

# calling display_receipt

print("\n=== Receipt 1: Overpay ===")
display_receipt(50.00, 60.00)

print("\n=== Receipt 2: Exact Payment ===")
display_receipt(75.00, 75.00)

print("\n=== Receipt 3: Underpay ===")
display_receipt(100.00, 80.00)

# Bonus a — display_mailing_label_v2

def display_mailing_label_v2(name, address1, city, state, zip, address2=''):
    print(name)
    print(address1)
    if address2:
        print(address2)
    print(f"{city}, {state} {zip}")

 # Bonus b — display_receipt_v2   
 
def display_receipt_v2(amount_paid, *balances):
    total_due = sum(balances)
    print(f"Total Due:    ${total_due:.2f}")
    print(f"Amount Paid:  ${amount_paid:.2f}")
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due:   ${change:.2f}")
    else:
        balance = total_due - amount_paid
        print(f"Remaining balance to be paid: ${balance:.2f}")

        print("\n=== BONUS: Multiple Balances ===")
display_receipt_v2(100.00, 30.00, 25.00, 20.00)