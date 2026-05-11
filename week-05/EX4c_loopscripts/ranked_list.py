# Step 2: List of at least 5 items
# ─────────────────────────────────────────────
cities = ["Kyoto", "Cape Town", "Lisbon", "Cartagena", "Reykjavik", "Marrakech"]

# ─────────────────────────────────────────────
# Step 3 & 4: Numbered list using enumerate() starting at 1
# ─────────────────────────────────────────────
print("Cities I'd Love to Visit:")
for index, city in enumerate(cities, start=1):
    if index == 1:
        print(f"{index}. {city} <- top pick!")
    else:
        print(f"{index}. {city}")

# ─────────────────────────────────────────────
# BONUS: Print in reverse order, still numbered 1 through 6
# ─────────────────────────────────────────────
print("\nCities I'd Love to Visit (Reversed):")
for index, city in enumerate(reversed(cities), start=1):
    if index == 1:
        print(f"{index}. {city} <- top pick!")
    else:
        print(f"{index}. {city}")