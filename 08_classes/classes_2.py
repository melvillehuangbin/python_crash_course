"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a
day of business.
"""

class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('The restaurant\'s name is ' + self.restaurant_name.title() + ' and it sells ' + self.cuisine_type.title() + ' cuisine')
    
    def open_restaurant(self):
        print('The restaurant is opened!')

    def set_number_served(self, new_number_served):
        self.number_served = new_number_served
    
    def increment_number_served(self, additional_number_served):
        self.number_served += additional_number_served

restaurant = Restaurant('macdonalds', 'western')
print('Total number of customers served: ' + str(restaurant.number_served))
restaurant.set_number_served(10)
print('Total number of customers served: ' + str(restaurant.number_served))
restaurant.increment_number_served(5)
print('Total number of customers served: ' + str(restaurant.number_served))

"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""
class User():

    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = 0

    def describe_restaurant(self):
        print('Summary of user\'s information: ')
        print('First name: ' + self.first_name)
        print('Last name: ' + self.last_name)
        for k, v in self.user_info.items():
            print(k.title() + ": " + v)

    def greet_user(self):
        print('Hi ' + self.first_name + '! Welcome!')

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('Bart', 'Simpson')
for i in range(1 ,10+1):
    user.increment_login_attempts()
print('Number of login attempts: ' + str(user.login_attempts))
user.reset_login_attempts()
print('Number of login attempts: ' + str(user.login_attempts))