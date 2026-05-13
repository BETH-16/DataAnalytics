# Description: This script practices creating and using classes

class Restaurant:
    '''A class to represent a restaurant with a name and food type.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served    = 0
        self.customer_ratings = []
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")
    
    def add_num_served(self):
        served = int(input("How many customers served today? "))
        self.number_served += served  

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")
        
    def customer_rating(self):
        while True:
            rating_input = input("How would you rate your experience today on a scale of 1-5 (5 being excellent)? ")
            if not rating_input.isdigit():
                print("Invalid input! Please enter a whole number between 1 and 5.")
                continue
            rating = int(rating_input)
            if rating < 1 or rating > 5:
                print("Invalid input! Please enter a number between 1 and 5.")
                continue
            self.customer_ratings.append(rating)
            average = sum(self.customer_ratings) / len(self.customer_ratings)
            print(f"Your rating was {rating}. The average rating for {self.rest_name} is {average:.1f}")
            break


restaurant_1 = Restaurant('Olive Garden', 'Italian food')
restaurant_2 = Restaurant('Shake Shack', 'burgers and fries')
restaurant_3 = Restaurant('Nobu', 'Japanese cuisine')

restaurant_1.describe_rest()
restaurant_1.rest_open()

print()

restaurant_2.describe_rest()
restaurant_2.rest_open()

print()

restaurant_3.describe_rest()
restaurant_3.rest_open()


print("=== Olive Garden ===")
restaurant_1.print_num_served()
restaurant_1.add_num_served()
restaurant_1.add_num_served()
restaurant_1.print_num_served()

print("\n=== Shake Shack ===")
restaurant_2.print_num_served()
restaurant_2.add_num_served()
restaurant_2.print_num_served()

print("\n=== Nobu ===")
restaurant_3.print_num_served()
restaurant_3.add_num_served()
restaurant_3.print_num_served()

print("\n=== Ratings: Olive Garden ===")
restaurant_1.customer_rating()
restaurant_1.customer_rating()
restaurant_1.customer_rating()

print("\n=== Ratings: Shake Shack ===")
restaurant_2.customer_rating()
restaurant_2.customer_rating()

print("\n=== Ratings: Nobu ===")
restaurant_3.customer_rating()
restaurant_3.customer_rating()


