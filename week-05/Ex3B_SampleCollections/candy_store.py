# Description: This script practices working with tuples and sets
# Step 2: Create two tuples
# ─────────────────────────────────────────────
candy_types = ("Gummy Bears", "Lollipop", "Hard Candy", "Taffy")
fruity_flavors = ("Strawberry", "Watermelon", "Mango", "Peach")

# ─────────────────────────────────────────────
# Step 3: Create a set of candy combinations
# ─────────────────────────────────────────────
candy_combinations = {
    candy_types[0] + " - " + fruity_flavors[1],   # Gummy Bears - Watermelon
    candy_types[0] + " - " + fruity_flavors[3],   # Gummy Bears - Peach
    candy_types[1] + " - " + fruity_flavors[0],   # Lollipop - Strawberry
    candy_types[1] + " - " + fruity_flavors[2],   # Lollipop - Mango
    candy_types[2] + " - " + fruity_flavors[3],   # Hard Candy - Peach
    candy_types[3] + " - " + fruity_flavors[0],   # Taffy - Strawberry
    candy_types[3] + " - " + fruity_flavors[1],   # Taffy - Watermelon
}

# ─────────────────────────────────────────────
# Step 4 & 5: Print the set multiple times
# ─────────────────────────────────────────────
print("Today's candy options include:")
print(candy_combinations)

print("\nToday's candy options include:")
print(candy_combinations)

print("\nToday's candy options include:")
print(candy_combinations)

# Notice: the order of items changes every time you run the script!
# That is because sets are unordered — Python does not guarantee
# any specific order when storing or printing set items.