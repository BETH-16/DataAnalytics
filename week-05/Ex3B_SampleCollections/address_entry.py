 # Step 1: Define contact_info dictionary
# ─────────────────────────────────────────────
contact_info = {
    "name": "Jordan Rivera",
    "address": "123 Maple Street",
    "city": "Atlanta",
    "state": "GA",
    "zip": "30301"
}

# ─────────────────────────────────────────────
# Step 2: Print formatted mailing address
# ─────────────────────────────────────────────
print("=== Mailing Address (Original) ===")
print(f"{contact_info['name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")

# ─────────────────────────────────────────────
# Step 3: Remove the name key:value pair
# ─────────────────────────────────────────────
del contact_info["name"]
print("\nAfter removing 'name' key:")
print(contact_info)

# ─────────────────────────────────────────────
# Step 4: Create full_name as a nested dictionary
# ─────────────────────────────────────────────
full_name = {
    "first name": "Jordan",
    "last name": "Rivera"
}

# ─────────────────────────────────────────────
# Step 5: Add honorific using .update()
# ─────────────────────────────────────────────
full_name.update({"honorific": "Dr."})
print("\nfull_name dictionary:")
print(full_name)

# ─────────────────────────────────────────────
# Step 6: Add full_name to contact_info using .update()
# ─────────────────────────────────────────────
contact_info.update({"full_name": full_name})
print("\nUpdated contact_info:")
print(contact_info)

# ─────────────────────────────────────────────
# Step 7: Print updated formatted mailing address
# ─────────────────────────────────────────────
print("\n=== Mailing Address (Updated) ===")
print(f"""{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")
