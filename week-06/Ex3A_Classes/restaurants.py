# Description: This script practices creating and using classes

class Restaurant:
    '''A class to represent a restaurant with a name and food type.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_types

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

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