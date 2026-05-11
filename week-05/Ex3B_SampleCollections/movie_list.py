# Description: This script practices creating and manipulating lists
# Step 2: Create a list of favorite movies
# ─────────────────────────────────────────────
movie_list = [
    "The Lion King",
    "Interstellar",
    "Black Panther",
    "The Devil Wears Prada",
    "Inception",
    "Parasite"
]

# ─────────────────────────────────────────────
# Step 3: Print length description and full list
# ─────────────────────────────────────────────
print(f"The list movie_list includes my top {len(movie_list)} favorite movies.")
print(movie_list)

# ─────────────────────────────────────────────
# Step 4a: sorted() function — does NOT change the original list
# ─────────────────────────────────────────────
print("\n=== Step 4a: Using sorted() ===")
print(sorted(movie_list))   # prints a sorted copy
print(movie_list)           # original list is unchanged
# Notice: sorted() returns a new sorted list but leaves the original as-is

# ─────────────────────────────────────────────
# Step 4b: .sort() method — DOES change the original list
# ─────────────────────────────────────────────
print("\n=== Step 4b: Using .sort() ===")
movie_list.sort()
print(movie_list)           # list is now permanently sorted
# Notice: .sort() modifies the list in place — the original order is gone

# ─────────────────────────────────────────────
# Step 5: Add a new movie using .append()
# ─────────────────────────────────────────────
movie_list.append("Everything Everywhere All at Once")

print("\n=== Step 5: After .append() ===")
print(f"The list movie_list includes my top {len(movie_list)} favorite movies.")
print(movie_list)
