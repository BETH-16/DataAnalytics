import random 
products = [
    'Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
    'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector'
]
# Product of the Day — picks one random item
product_of_the_day = random.choice(products)
print(f"Product of the Day: {product_of_the_day}")

# Usability Survey — picks 3 items without repeating
survey_products = random.sample(products, 3)
print(f"\nProducts selected for usability survey: {survey_products}")

# Randomized presentation — shuffles the whole list
random.shuffle(products)
print(f"\nProducts in randomized order: {products}")

# Simulated transaction count — picks a random number between 50 and 300
daily_transactions = random.randint(50, 300)
print(f"\nSimulated daily transaction count: {daily_transactions}")