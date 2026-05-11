# tiles.py

import math

# Get room dimensions
length = float(input("Enter the length of the room (feet): "))
width = float(input("Enter the width of the room (feet): "))

# Calculate total area (1 tile = 1 sq ft)
area = length * width

# Add 10% extra tiles
area_with_extra = area * 1.10

# Each box has 12 tiles → 12 sq ft per box
boxes_needed = math.ceil(area_with_extra / 12)

# Display result
print(f"You will need to buy {boxes_needed} boxes of tiles.")