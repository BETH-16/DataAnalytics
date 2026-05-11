# distance.py

import math

# Get coordinates from user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display result
print(f"The distance between the points is {distance:.2f}")