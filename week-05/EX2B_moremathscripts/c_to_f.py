# c_to_f.py

# Ask user for temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit using formula
fahrenheit = (celsius * 9 / 5) + 32

# Display the result
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")