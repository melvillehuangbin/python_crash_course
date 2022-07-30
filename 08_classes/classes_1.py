"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
"""
class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The restaurant\'s name is ' + self.restaurant_name.title() + ' and it sells ' + self.cuisine_type.title() + ' cuisine')
    
    def open_restaurant(self):
        print('The restaurant is opened!')

restaurant = Restaurant('macdonalds', 'fast food')
restaurant.describe_restaurant()
restaurant.open_restaurant()

"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""

macdonalds = Restaurant('macdonalds', 'fast food')
big_eater = Restaurant('big eater', 'chinese')
char_grill = Restaurant('char grill western bar', 'western')

macdonalds.describe_restaurant()
big_eater.describe_restaurant()
char_grill.describe_restaurant()


"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""

class User():

    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info

    def describe_restaurant(self):
        print('Summary of user\'s information: ')
        print('First name: ' + self.first_name)
        print('Last name: ' + self.last_name)
        for k, v in self.user_info.items():
            print(k.title() + ": " + v)

    def greet_user(self):
        print('Hi ' + self.first_name + '! Welcome!')

user = User('Bart', 'Simpson', color = 'yellow', personality = 'chubby')
user_2 = User('Elon', 'Musk', net_worth = '$100 Billion')

user.describe_restaurant()
user.greet_user()

user_2.describe_restaurant()
user_2.greet_user()